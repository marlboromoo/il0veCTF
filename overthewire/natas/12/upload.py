#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import requests

NATAS_USER='natas12'
NATAS_PASS='EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'
NATAS_URL='http://natas12.natas.labs.overthewire.org/index.php'

def upload(path, size=1000):
    if not os.path.exists(path):
        return None

    filename = os.path.basename(path)
    print "Upload %s..." % (filename)

    data = {
        'MAX_UPLOAD_SIZE' : size,
        'filename' : filename,
    }
    #auth = requests.auth.HTTPBasicAuth(NATAS_USER, NATAS_PASS)
    auth = (NATAS_USER, NATAS_PASS)
    files = {'uploadedfile' : (filename, open(path, 'rb'))}
    result = requests.post(NATAS_URL, auth=auth, data=data, files=files)
    return result

if __name__ == '__main__':
    f = sys.argv[1]
    if f:
        result = upload(f)
        print result
        print result.text


