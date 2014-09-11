#!/usr/bin/env python
# encoding: utf-8

import sys

def s2oct(s):
    return int(oct(ord(s)))

def str2oct(str):
    str #+= '\n'
    r = ''
    for i in str:
        #print i
        r += "\\\\%s" % (s2oct(i))
    return r


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        exit(1)
    print 'printf "%s"' % (str2oct(sys.argv[1]))

