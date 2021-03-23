#!/usr/bin/env python3

import json
import psycopg2
import threading
import time
import uuid

from connections import Connection
from http.server import SimpleHTTPRequestHandler, HTTPServer
from psycopg2 import Error
from urllib.parse import parse_qs

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
        elif self.path == '/do_signup_engineer':  
            data = self.rfile.read(int(self.headers.get('Content-Length')))
            data = json.loads(data)
            chk_eml = self.db_connection.chk_eml(data)
            if chk_eml is None: 
                user_data = self.db_connection.create_user_engineer(data)
                return self.wfile.write(json.dumps({'credentials': True}).encode())
            else:
                return self.wfile.write(json.dumps({'credentials': False}).encode())     
        elif self.path == '/do_login':
            data = self.rfile.read(int(self.headers.get('Content-Length')))
            data = json.loads(data)
            user_data = self.db_connection.user_exists(data)
            get_user_role = self.db_connection.get_user_role(data)
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
                if "client" in get_user_role:
                    return self.wfile.write(json.dumps({'session_id': session_id, 'user_id': user_data[0], 'is_valid': True, 'role':"client"}).encode())
                else:
                    return self.wfile.write(json.dumps({'session_id': session_id, 'user_id': user_data[0], 'is_valid': True, 'role':"engineer"}).encode())


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
            return self.wfile.write(json.dumps({'logout': "success"}).encode())
        elif self.path == '/book_engineer':
            data = self.rfile.read(int(self.headers.get('Content-Length')))
            data = json.loads(data)
            get_engineer_info = self.db_connection.get_engineer_info(data)
            book_engineer = self.db_connection.book_engineer(get_engineer_info)
            return self.wfile.write(json.dumps({'book_engineer': "success"}).encode())


           
            

     



    def do_GET(self):
        if self.path in ['/', '/signup', '/signupEngineer', '/login', '/homee', '/engineers', '/jobs', '/new_jobs', '/profile', '/home', '/engineerslist', '/engineerslist','/orders']:
            with open('index.html') as f:
                Cookie = self.headers.get('Cookie')
                session_id = False  
                html = f.read()
                session_info = {
                    'user_id': None,
                    'is_valid': False,
                }
                if Cookie:
                    session_cookie = parse_qs(Cookie.replace(' ', ''))
                    if session_cookie.get('session_id'):
                        session_id = session_cookie.get('session_id')[0]
                        user = self.db_connection.session_validate({'session_id': session_id})
                        role = self.db_connection.get_user_role_session_val({'session_id': session_id})
                        e_list = self.db_connection.get_engineer_list()
                        order = self.db_connection.get_order_list()
                        if user and len(user):
                            session_info = {
                                'user_id': user[0],
                                'is_valid': True,
                                'session_id': session_id,
                                'role':role[0]
                            }
                        if e_list and len(e_list):
                            data_list = list()
                            for engineer_list in e_list:                                
                                engineer_list={
                                    'engineer_id': engineer_list[0],
                                    'email': engineer_list[2],
                                    'mobile_no': engineer_list[6],
                                    'specialist': engineer_list[7],
                                    'experience': engineer_list[8],
                                }
                                data_list.append(engineer_list)
                        if order and len(order):
                            final_order_list = list()
                            for order_list in order: 
                                order_list={
                                    'engineer_id': order_list[0],
                                    'email': order_list[1],
                                    'specialist': order_list[2],
                                    'mobile_no': order_list[3],
                                    'experience': order_list[4],
                                }
                                final_order_list.append(order_list)
                html = html.replace('$session_info', json.dumps(session_info))
                html = html.replace('$data_list', json.dumps(data_list))
                html = html.replace('$final_order_list', json.dumps(final_order_list))
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(html.encode())
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