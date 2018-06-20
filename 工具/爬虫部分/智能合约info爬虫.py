import pymongo
import requests
from pyquery import PyQuery as pq
import settings

header =  {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
        }
db = pymongo.MongoClient(settings.DATABASE_HOST, 27017)["smart_contract"]["big_case"]
for i in db.find():
    info = {}
    address = i['address']
    req = requests.session()
    url1 = "https://etherscan.io/address/" + address
    rep1 = req.get(url1)
    q = pq(rep1.text)
    creat = q("#ContentPlaceHolder1_divSummary")("#ContentPlaceHolder1_trContract").find('a')
    for a in creat:
        info['address'] = i['address']
        info['creator'] = a.text
        break
    url2 = "https://etherscan.io/readContract?a={}&v={}".format(address,address)
    rep2 = req.get(url2)
    if 'Sorry"' in rep2.text:
        print("不存在")
        info = {"else":'未公开'}
    else:
        q = pq(rep2.text)
        table = q(".table-responsive")
        trs = q(table)(".table")('tbody').find('tr')
        #print(trs)
        for list in trs:
            text = q(list).text()
            if text[0].isalpha() or 'Query' in text:
                continue
            else:
                a = text.index('\n')
                text = text[:a]
                l = text.split(' ')
                info[l[1]] = l[3]
        print(info)
        #todo 插入数据库
