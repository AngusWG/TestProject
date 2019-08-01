#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2019/7/31 17:36
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : prometheus_client_ttt.py
from prometheus_client import start_http_server, Summary
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')


# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        pass
        # process_request(random.random())
