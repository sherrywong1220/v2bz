#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json


class V2bz(object):
    def __init__(self, user, password):
        self.loginurl = 'https://ss.v2bz.com/auth/login'
        self.signurl = 'https://ss.v2bz.com/user/checkin'
        self.userlogin = 'https://ss.v2bz.com/user'
        self.session = requests.Session()
        self.user = user
        self.password = password
        self.headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Content-Type':
            'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With':
            'XMLHttpRequest'
        }

    def login(self):
        r = self.session.get(self.loginurl)
        soup = BeautifulSoup(r.text, 'html.parser')
        remember_input = soup.find('input', attrs={'id': 'remember_me'})
        remember_me = remember_input['value']

        data = {
            'email': self.user,
            'passwd': self.password,
            'remember_me': remember_me
        }

        r = self.session.post(self.loginurl, data=data, headers=self.headers)

        response_json = json.loads(r.text)
        if response_json['ret'] == 1:
            print 'Succeed to login!'
        else:
            print 'Fail to login!'

    def sign(self):
        r = self.session.get(self.userlogin)
        if r.text.find(u'等一下下嘛') == -1:
            r = self.session.post(self.signurl, headers=self.headers)
            # response_json = json.loads(r.text)
            print 'Succeed to sign!'
        else:
            print 'Already signed before!'


v2bz = V2bz('xxxxxx@qq.com', '123456')
v2bz.login()
v2bz.sign()