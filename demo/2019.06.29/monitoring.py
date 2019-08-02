#!/usr/bin/python3
# encoding: utf-8
# @Time    : 2019/8/2 16:29
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : monitoring.py
"""
    FROM https://github.com/ITISFoundation/osparc-simcore/blob/3e80ce451352c906f2876113dbb6ae33e8574be1/packages/service-library/src/servicelib/monitoring.py
    &&  https://github.com/ITISFoundation/osparc-simcore/blob/3e80ce451352c906f2876113dbb6ae33e8574be1/packages/service-library/src/servicelib/monitoring.py
    setup_monitoring(app, app_name="app_name)
"""
import time

from prometheus_client import Gauge, make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from flask import request, current_app
from prometheus_client import Counter, Histogram


def setup_monitoring(app, app_name=None):
    if app_name is None:
        app_name = app.name

    def start_timer():
        request.start_time = time.time()
        current_app.extensions["prometheus"]['REQUEST_IN_PROGRESS'].labels(
            app_name, request.endpoint, request.method).inc()

    def record_request_data(response):
        resp_time = time.time() - request.start_time
        endpoint = request.endpoint
        ext_prometheus = current_app.extensions["prometheus"]
        ext_prometheus['REQUEST_LATENCY'].labels(app_name, endpoint).observe(resp_time)
        ext_prometheus['REQUEST_IN_PROGRESS'].labels(app_name, endpoint, request.method).dec()
        ext_prometheus['REQUEST_COUNT'].labels(app_name, request.method, endpoint, response.status).inc()
        return response

    app.before_request(start_timer)
    app.after_request(record_request_data)

    extensions_prometheus = dict()
    extensions_prometheus['app_name'] = app_name
    extensions_prometheus['REQUEST_COUNT'] = Counter(
        'http_requests_total', 'Total Request Count',
        ['app_name', 'method', 'endpoint', 'http_status']
    )

    # Latency of a request in seconds
    extensions_prometheus['REQUEST_LATENCY'] = Histogram(
        'http_request_latency_seconds', 'Request latency',
        ['app_name', 'endpoint']
    )

    extensions_prometheus['REQUEST_IN_PROGRESS'] = Gauge(
        'http_requests_in_progress_total', 'Requests in progress',
        ['app_name', 'endpoint', 'method']
    )

    app.extensions["prometheus"] = extensions_prometheus

    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        '/metrics': make_wsgi_app()
    })
