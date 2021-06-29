# encoding: utf-8
# @Time   : 2021/6/29
"""
idea form https://www.v2ex.com/t/786366#reply10

To do:

* 工作一百年到手工资数
* 离下班还有多久

To package `pyinstaller -F 工作幸福进度条.py`
"""
import datetime
import sys
import time

base = int(input("输入工资base(千元) [10]") or 10) * 1000
start_time = int(input("早上几点上班？[9]") or 9)
end_time = int(input("预计几点下班？(十二小时制) [6]") or 6) + 12
work_days = int(input("一周几天呀？[5]") or 5)

sleep_day = 365 / 7 * (7 - work_days)
work_day_of_month = (365 - sleep_day) / 12
one_day_pay = base / work_day_of_month

today = datetime.datetime.fromisoformat(datetime.date.today().isoformat())
start_t = today + datetime.timedelta(hours=start_time)
end_t = today + datetime.timedelta(hours=end_time)
all_t = (end_t - start_t).seconds

print("\n" * 100)
while True:
    now = datetime.datetime.now()
    pass_t = (now - start_t).seconds
    percentage = (pass_t / all_t)
    get_paid = round(one_day_pay * percentage, 3)
    msg = "\r今天已经赚了 {:.3f}元/{:.3f}元: {:2.3f}%: ".format(get_paid, one_day_pay, percentage * 100)
    process = "[{}|{}]".format("+" * (int(percentage * 100) // 2), "-" * (int((1 - percentage) * 100) // 2))
    print(msg, process, end="")
    sys.stdout.flush()
    time.sleep(1)
