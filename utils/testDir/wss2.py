import random

import pymongo

typec = "cycle"
mongoDB = pymongo.MongoClient("127.0.0.1", 27017)
from datetime import datetime, timedelta


def save_single_cu_market_activity_index_to_mongodb(currency, single_cu_market_activity_index, timestamp, remarks=None):
    db = mongoDB["test"]
    data = {
        'timestamp': timestamp,
        "currency": currency,
        "single_cu_market_activity_index": single_cu_market_activity_index,
        "remarks": remarks,

    }
    db["single_cu_market_activity_index"].update_one(
        {
            'timestamp': timestamp,
            "currency": currency,
        },
        {
            "$set": data,
        },
        upsert=True, )
    return True


def get_exchangr(currency, endtimestamp):
    db = mongoDB["test"]
    starttimestamp = endtimestamp - timedelta(hours=2)
    # res = db["single_cu_market_activity_index"].find(
    #     {"timestamp": {'$$gt': timestamp}, "timestamp": {'$lte': timestamp}, "currency": currency})
    res = db["single_cu_market_activity_index"].find(
        {"timestamp": {'$lte': endtimestamp, '$gt': starttimestamp}, "currency": currency}).sort(
        "timestamp", -1)
    # "currency": currency
    if res.count() == 1:
        return res[0]
    if res.count() == 0:
        # 计算 自调
        return get_exchangr(currency, endtimestamp)
    if res.count()>1:
        print("warning")
        return res[0]


def sheng_cheng_shu_ju():
    cu_list = ["BTC", "ETH", "LTC", "ETC", "BCH", "XRP", "ETP", "NEO", "IOTA", "OMG", "DASH", "ZEC", "XMR", "EOS",
               "SAN", "EDO", "AVT", "BCU", "BT1", "BT2", "QTM", "RRT", "BCC"]
    for hour in range(200):
        t = datetime.now()
        timestamp = datetime(t.year, t.month, t.day, t.hour) - timedelta(hours=hour)
        for cu in cu_list:
            save_single_cu_market_activity_index_to_mongodb(cu, int(random.random() * 1000), timestamp)


if __name__ == '__main__':
    t = datetime.now()
    timestamp = datetime(t.year, t.month, t.day, t.hour) - timedelta(5)
    x = get_exchangr("BTC", timestamp)
    # for i in x:
    #     print(i)
    print(x.count())
    # random.random()
    # sheng_cheng_shu_ju()
