#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    html = open('shop.html', 'r').read()
    data = open('product.json', 'r').read()
    response = Response(html % {'data': str(json.loads(data))})
    response.status = '200 OK'
    response.headers['content-type'] = 'text/html'
    return response

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 5000, application)
