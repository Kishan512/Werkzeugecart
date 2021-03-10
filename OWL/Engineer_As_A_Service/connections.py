#!/usr/bin/env python3
import psycopg2

from psycopg2 import Error


class Connection():

    def __init__(self):
        print('>>> connection')
        self.create_connection('postgres')
        self.db_name = 'engineer_as_a_service'
        db_check = "SELECT 1 FROM pg_database WHERE datname='%s'" % self.db_name
        self.cr.execute(db_check)
        if not len(self.cr.fetchall()):
            self.cr.execute('CREATE DATABASE %s' % self.db_name)
            self.connection.close()
            self.create_connection(self.db_name)
            user = '''CREATE TABLE users(
                id SERIAL PRIMARY KEY,
                email varchar  NOT NULL unique,
                password varchar NOT NULL,
                session varchar,
                mobile_no varchar NOT NULL
            );'''
            self.cr.execute(user);
        else:
            self.create_connection(self.db_name)

    def create_connection(self, db_name):
        self.connection = psycopg2.connect(user="postgres", password="postgres", host="127.0.0.1", port="5432", database=db_name)
        self.connection.autocommit = True
        self.cr = self.connection.cursor()
    
    def chk_eml(self, data):
        self.cr.execute("SELECT id FROM users WHERE email='%s'" % (data['email']))
        return self.cr.fetchone()

    def chk_pass(self, data):
        self.cr.execute("SELECT id FROM users WHERE password='%s'" % (data['password']))
        return self.cr.fetchone()

    def create_user(self, dictn):
        user = """INSERT INTO users (email, password, mobile_no) VALUES ('%s', '%s', '%s')""" % (dictn['email'], dictn['password'], dictn['mobno']);
        self.cr.execute(user)

    def user_exists(self, data):
        self.cr.execute("SELECT id FROM users WHERE email='%s' and password='%s'" % (data['email'], data['password']))
        return self.cr.fetchone()

    def create_user_session(self, session_id, user_id):
        self.cr.execute("UPDATE users set session='%s' where id=%s" % (session_id, user_id))

    def session_validate(self, data):
        self.cr.execute("SELECT id FROM users WHERE session='%s'" % (data['session_id']))
        return self.cr.fetchone()

    def user_logout(self, data):
        print(data)
        self.cr.execute("UPDATE users set session=null where session='%s'" % (data['session_id']))
