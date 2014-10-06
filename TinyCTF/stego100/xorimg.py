#!/usr/bin/env python
# encoding: utf-8

"""
REF: http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_core/py_image_arithmetics/py_image_arithmetics.html
"""

import sys
import cv2

if __name__ == '__main__':
    print len(sys.argv)
    if not len(sys.argv) >= 3:
        exit(0)
    img1 = cv2.imread(sys.argv[1])
    img2 = cv2.imread(sys.argv[2])
    dst = cv2.bitwise_xor(img1, img2)
    cv2.imwrite('xor.png', dst)

    #. show the image file
    #cv2.imshow('dst',dst)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
