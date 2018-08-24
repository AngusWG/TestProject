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
    }

    User_Agent = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
        'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER) ',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)']

    def __init__(self):
        self.crawler_sleep_time = 60
        self.POOL_NUM = 100
        self.ip代理池 = redis.Redis('localhost', 6379)

    def main(self):
        try:
            cprint("正在启动ip数据获取")
            one = threading.Thread(target=self.ipGetData, args=(1,))
            one.start()
            cprint("正在启动ip时效性检测")
            two = threading.Thread(target=self.jianceip, args=(1,))
            two.start()

            # self.ipGetData(1)
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
            start = random.randint(0, 300)
            page = 50
            for i in range(start, start + page):
                # 休眠
                try:
                    self.waiting_trough()
                    self.headers['User-Agent'] = random.choice(self.User_Agent)
                    self.get_page_proxy(self.headers, i)
                except Exception as e:
                    cprint(e)
                    cprint("出现错误 休息5秒")
                    time.sleep(5)
                    pass

    def waiting_trough(self):
        num = len(self.ip代理池.hgetall("代理池"))
        while num > self.POOL_NUM:
            cprint("代理池种有{}条ip，暂停爬取30s".format(num))
            time.sleep(self.crawler_sleep_time)
            num = len(self.ip代理池.hgetall("代理池"))

    def get_page_proxy(self, headers, page):
        cprint("正在获取第{}页的代理ip".format(page))
        rep = requests.get("https://www.kuaidaili.com/free/inha/" + str(page), headers=headers)
        if rep.status_code == 200:
            p = pq(rep.text)
            ips = p('[data-title="IP"]').text().split(" ")
            ports = p('[data-title="PORT"]').text().split(" ")
            ifgns = p('[data-title="类型"]').text().split(" ")
            for i in range(len(ips)):
                try:
                    ip = ips[i]
                    port = ports[i]
                    ifgn = ifgns[i]
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
                rep = requests.get('http://www.baidu.com', proxies={"http": "http://" + ip}, timeout=1)
            else:
                rep = requests.get('https://www.baidu.com', proxies={"https": "https://" + ip}, timeout=1)
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
