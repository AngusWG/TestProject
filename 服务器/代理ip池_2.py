import json
import os
import random
import sys
from logging.handlers import RotatingFileHandler

import redis

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))).replace("\\", "/", 100)
rootsub = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace("\\", "/", 100)
sys.path.append(root)
sys.path.append(rootsub)
import requests
from pyquery import PyQuery as pq
import threading
import time
import logging  # 引入logging模块
import os.path
import time

# 第一步，创建一个logger
logger = logging.getLogger()
logging.getLogger('requests').setLevel(logging.ERROR)
logger.setLevel(logging.INFO)  # Log等级总开关
# 第二步，创建一个handler，用于写入日志文件
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
log_path = os.getcwd() + '/Logs/'
log_name = log_path + "代理池" + '.log'
logfile = log_name

formatter = logging.Formatter("%(message)s")
error_file_handler = RotatingFileHandler(logfile, mode='a', maxBytes=1024 * 1024 * 512, backupCount=5,
                                         encoding='utf-8')
error_file_handler.setLevel(logging.INFO)
error_file_handler.setFormatter(formatter)
# 第四步，将logger添加到handler里面
logger.addHandler(error_file_handler)


def cprint(msg):
    print(msg)
    logger.info(msg)



class 代理ip池:
    # 检查ip时间
    sleep_time = 60
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "If-None-Match": 'W/"8af0b700956e4c37b5fd98c27260de46"',
        "Host": "www.xicidaili.com", "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    }
    USER_AGENTS = [
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
    ]

    def __init__(self):
        self.ip代理池 = redis.Redis('localhost', 6379)

    def main(self):
        try:
            cprint("正在启动ip数据获取")
            one = threading.Thread(target=self.ipGetData, args=(1,))
            one.start()
            cprint("正在启动ip时效性检测")
            two = threading.Thread(target=self.jianceip, args=(1,))
            two.start()

        except Exception as e:
            cprint("Error: 无法启动线程")
        pass

    def jianceip(self, num):
        cprint("ip时效性检测启动成功")
        while True:
            try:
                alldata = self.ip代理池.hgetall("代理池")
                cprint("ip池存在 {} 条ip".format(len(alldata)))
                for index, data in enumerate(alldata):
                    data = json.loads(data.decode().replace("'", "\""))
                    results = self.yanZhengIp(data["ip"] + ":" + data["port"], data["type"])
                    if results is None or results == "":
                        self.ip代理池.hdel("代理池", data)
                        cprint("ip地址：" + data["ip"] + ":" + data["port"] + "已经失效，已删除")
                    else:
                        pass
            except Exception as e:
                cprint(e)
            time.sleep(self.sleep_time)
            cprint("一次循环完毕")

    def ipGetData(self, num):
        while True:
            cprint("ip数据获取启动成功")
            page = 50
            for i in range(1, page):
                # 休眠
                try:
                    self.waiting_trough()
                    self.headers['User-Agent'] = random.choice(self.USER_AGENTS)
                    self.get_page_proxy(self.headers, i)
                except Exception as e:
                    cprint(e)
                    cprint("出现错误 休息5秒")
                    time.sleep(5)
                    pass

    def waiting_trough(self):
        num = len(self.ip代理池.hgetall("代理池"))
        while num > 350:
            cprint("代理池种有{}条ip，暂停爬取30s".format(num))
            time.sleep(60)
            num = len(self.ip代理池.hgetall("代理池"))

    def get_page_proxy(self, headers, page):
        cprint("正在获取第{}页的代理ip".format(page))
        rep = requests.get("http://www.xicidaili.com/nn/" + str(page), headers=headers)
        if rep.status_code == 200:
            p = pq(rep.text)
            trs = p("#ip_list").find("tr")
            for tr in trs:
                try:
                    tds = p(tr).find("td")
                    if len(tds) > 6:
                        ip = p(tds[1]).text().replace(" ", "")
                        port = p(tds[2]).text().replace(" ", "")
                        ifgn = p(tds[5]).text().replace(" ", "")
                        resultip = self.yanZhengIp(ip + ":" + port, ifgn)
                        if resultip == "" or resultip == '':
                            continue
                        else:
                            result = self.ip代理池.hget("代理池", {"ip": ip, "port": port, "type": ifgn})
                            if result is None:
                                self.ip代理池.hset("代理池", {"ip": ip, "port": port, "type": ifgn}, 0)
                                cprint("第" + str(page) + "页 " + "获取ip：" + ip + ":" + port + " 数据成功")
                except Exception as e:
                    cprint(e)
                    pass

    @staticmethod
    def yanZhengIp(ip, type):
        try:
            if type == "http" or type == "HTTP":
                rep = requests.get('https://www.baidu.com/', proxies={"http": "http://" + ip}, timeout=1)
            else:
                rep = requests.get('https://www.baidu.com/', proxies={"https": "https://" + ip}, timeout=1)
            if rep.status_code == 200:
                return ip
        except Exception as e:
            pass
        return ""


def init():
    cprint("代理池启动")
    c = 代理ip池()
    c.main()


if __name__ == "__main__":
    c = 代理ip池()
    c.main()
