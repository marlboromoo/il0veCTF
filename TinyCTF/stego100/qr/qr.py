#!/usr/bin/env python
# encoding: utf-8

from qrtools import QR

if __name__ == '__main__':
    qr = QR(filename='./qr-fix.png')
    if qr.decode():
        print qr.data
