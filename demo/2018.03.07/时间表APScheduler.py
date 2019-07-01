#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2017/12/27 0027 14:32
# @author  : zza
# @Email   : 740713651@qq.com

# coding=utf-8
"""
Demonstrates how to use the background scheduler to schedule a job that executes on 3 second
intervals.
https://www.jianshu.com/p/427d095ce56c
"""

import os
import time
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler


def tick():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    # scheduler.add_job(tick,'interval', minutes=0.5)
    scheduler.add_job(tick, "cron", hour=14, minute=42)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
