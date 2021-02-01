#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from tempfile import gettempdir
from werkzeug.contrib.sessions import FilesystemSessionStore
from werkzeug.routing import Map, Rule
from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    html = open('index.html', 'r').read()
    data = open('main.js', 'r').read()
    
    response = Response(html)
    response.status = '200 OK'
    response.headers['content-type'] = 'text/html';
    response.headers['content-type'] = 'text/js';
    return response


if __name__ == '__main__':
    run_simple('localhost', 4000, application)
