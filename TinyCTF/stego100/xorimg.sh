#!/bin/bash

#
# Ref: http://stackoverflow.com/questions/8504882/searching-for-a-way-to-do-bitwise-xor-on-images
#


if [[ -z "$2" ]]; then
    exit 0
fi

convert $1 $2 -fx "(((255*u)&(255*(1-v)))|((255*(1-u))&(255*v)))/255" xor.png
