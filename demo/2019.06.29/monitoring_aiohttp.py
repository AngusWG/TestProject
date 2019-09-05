#!/usr/bin/python3
# encoding: utf-8
# @Time    : 2019/9/5 16:36
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : monitoring.py
"""
FROM:
    https://github.com/cloud-cds/cds-stack/blob/4243cd9b2e878f16a251d05afb2d202d71e41dce/api/monitoring.py
    https://github.com/DD-DeCaF/gene-to-reactions/blob/3af42110433edf8495810e6a95a516368464e179/src/gene_to_reactions/app.py

    setup_monitoring(app, "app_name")
"""
import time
import asyncio
from aiohttp import web
from prometheus_client import multiprocess, generate_latest
from prometheus_client import CONTENT_TYPE_LATEST, CollectorRegistry, Histogram, Counter, Gauge


def prom_middleware(app_name):
    @asyncio.coroutine
    def factory(app, handler):
        @asyncio.coroutine
        def middleware_handler(request):
            try:
                request['start_time'] = time.time()
                request.app['REQUEST_IN_PROGRESS'].labels(
                    app_name, request.path, request.method).inc()
                response = yield from handler(request)
                resp_time = time.time() - request['start_time']
                request.app['REQUEST_LATENCY'].labels(app_name, request.path).observe(resp_time)
                request.app['REQUEST_IN_PROGRESS'].labels(app_name, request.path, request.method).dec()
                request.app['REQUEST_COUNT'].labels(
                    app_name, request.method, request.path, response.status).inc()
                return response
            except Exception as ex:
                raise

        return middleware_handler

    return factory


async def metrics(request):
    resp = web.Response(body=generate_latest(multiprocess.MultiProcessCollector(CollectorRegistry())))
    resp.content_type = CONTENT_TYPE_LATEST
    return resp


def setup_monitoring(app, app_name):
    app['REQUEST_COUNT'] = Counter(
        'requests_total', 'Total Request Count',
        ['app_name', 'method', 'endpoint', 'http_status']
    )
    app['REQUEST_LATENCY'] = Histogram(
        'request_latency_seconds', 'Request latency',
        ['app_name', 'endpoint']
    )

    app['REQUEST_IN_PROGRESS'] = Gauge(
        'requests_in_progress_total', 'Requests in progress',
        ['app_name', 'endpoint', 'method']
    )

    app.middlewares.insert(0, prom_middleware(app_name))
    app.router.add_get("/metrics", metrics)
