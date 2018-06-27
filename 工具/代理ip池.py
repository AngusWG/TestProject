import os
import sys

import pymongo

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))).replace("\\", "/", 100)
rootsub = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace("\\", "/", 100)
sys.path.append(root)
sys.path.append(rootsub)
import requests
from pyquery import PyQuery as pq
import threading
# from ldzhuaqu.db.SqlFactory import SqlFactory
import time


class 代理ip池:
    ip = "127.0.0.1"
    # port = "27017"
    port = int("27017")
    database = "WL_scrapy"
    tablename = "ip代理池"

    def __init__(self):
        re = pymongo.MongoClient(self.ip, self.port)[self.database]
        # re.authenticate("test", "123456")
        self.ip代理池 = re[self.tablename]

    def main(self):
        try:
            print("正在启动ip数据获取")
            one = threading.Thread(target=self.ipGetData, args=(1,))
            one.start()
            print("正在启动ip时效性检测")
            two = threading.Thread(target=self.jianceip, args=(2,))
            two.start()

        except Exception as e:
            print("Error: 无法启动线程")
        pass

    def jianceip(self, num):
        print("ip时效性检测启动成功")
        # ip代理池 = SqlFactory.getMong(self.ip, self.port, self.database).db[self.tablename]
        # re = pymongo.MongoClient(self.ip, self.port)[self.database]
        # re.authenticate("test", "123456")
        ip代理池 = self.ip代理池
        while True:
            try:
                alldata = ip代理池.find({})
                for index, data in enumerate(alldata):
                    results = self.yanZhengIp(data["ip"] + ":" + data["port"], data["type"])
                    if results is None or results == "":
                        ip代理池.delete_one({"ip": data["ip"], "port": data["port"]})
                        print("ip地址：" + data["ip"] + ":" + data["port"] + "已经失效，已删除")
                    else:
                        print("ip正常")
            except Exception as e:
                print(e)
            time.sleep(10)
            print("一次循环完毕")

    def ipGetData(self, num):
        print("ip数据获取启动成功")
        ip代理池 = self.ip代理池
        while True:
            try:
                headers = {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                    "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9",
                    "Cache-Control": "max-age=0",
                    "If-None-Match": 'W/"8af0b700956e4c37b5fd98c27260de46"',
                    "Host": "www.xicidaili.com", "Upgrade-Insecure-Requests": "1",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
                }
                rep = requests.get("http://www.xicidaili.com/nn", headers=headers)
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
                                    result = ip代理池.find_one({"ip": ip, "port": port, "type": ifgn})
                                    if result is None:
                                        ip代理池.insert_one({"ip": ip, "port": port, "type": ifgn})
                                        print("获取ip：" + ip + ":" + port + "数据成功")
                        except Exception as e:
                            print(e)
                            pass
            except Exception as e:
                print(e)
                pass
            time.sleep(60 * 20)
        pass

    @staticmethod
    def yanZhengIp(ip, type):
        try:
            rep = None
            if type == "http" or type == "HTTP":
                rep = requests.get('http://www.baidu.com', proxies={"http": "http://" + ip}, timeout=1)
            else:
                rep = requests.get('http://www.baidu.com', proxies={"https": "https://" + ip}, timeout=1)
            if rep.status_code == 200:
                return ip
        except Exception as e:
            pass
        return ""


if __name__ == "__main__":
    c = 代理ip池()
    c.main()
