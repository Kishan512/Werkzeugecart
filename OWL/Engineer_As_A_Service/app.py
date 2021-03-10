#!/usr/bin/env python3

import json
import psycopg2
import threading
import time
import uuid

from connections import Connection
from http.server import SimpleHTTPRequestHandler, HTTPServer
from psycopg2 import Error


class myHandler(SimpleHTTPRequestHandler):
    db_connection = Connection()

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        if self.path == '/do_signup':
            data = self.rfile.read(int(self.headers.get('Content-Length')))
            data = json.loads(data)
            chk_eml = self.db_connection.chk_eml(data)
            if chk_eml is None: 
                user_data = self.db_connection.create_user(data)
                return self.wfile.write(json.dumps({'credentials': True}).encode()) 
            else:
                return self.wfile.write(json.dumps({'credentials': False}).encode())            
        elif self.path == '/do_login':
            data = self.rfile.read(int(self.headers.get('Content-Length')))
            data = json.loads(data)
            user_data = self.db_connection.user_exists(data)
            if user_data is None:
                chk_eml = self.db_connection.chk_eml(data)
                chk_pass = self.db_connection.chk_pass(data)
                if chk_eml is None:
                    return self.wfile.write(json.dumps({'email': False}).encode())
                elif chk_pass is None:
                    return self.wfile.write(json.dumps({'pass': False}).encode())
            else:
                session_id = str(uuid.uuid4())
                self.db_connection.create_user_session(session_id, user_data[0])
                return self.wfile.write(json.dumps({'session_id': session_id}).encode())
        elif self.path == '/session_validate':
            data = self.rfile.read(int(self.headers.get('Content-Length')))
            data = json.loads(data)
            user = self.db_connection.session_validate(data)
            if user is None:
                return self.wfile.write(json.dumps({'valid': True}).encode())
            else:
                return self.wfile.write(json.dumps({'valid': False}).encode())
      
        elif self.path == '/do_logout':
            data = self.rfile.read(int(self.headers.get('Content-Length')))
            data = json.loads(data)
            user_data = self.db_connection.user_logout(data)
            return self.wfile.write(json.dumps({'logout': "done"}).encode())



    def do_GET(self):
        if self.path in ['/', '/signup', '/login', '/home', '/engineers'] :
            with open('index.html') as f:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f.read().encode())
        else:
            super(myHandler, self).do_GET()
           
def start_server():
   SimpleHTTPRequestHandler.extensions_map['.js'] = 'application/javascript'
   httpd = HTTPServer(('0.0.0.0', 3600), myHandler)
   httpd.serve_forever()

url = 'http://127.0.0.1:3600'

if __name__ == "__main__":
   print("----------------------")
   print("----------------------")
   print("Server running on: {}".format(url))
   threading.Thread(target=start_server, daemon=True).start()

   while True:
       try:
           time.sleep(1)
       except KeyboardInterrupt:
           httpd.server_close()
           quit(0)