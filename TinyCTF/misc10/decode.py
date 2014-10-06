#!/usr/bin/env python
# encoding: utf-8

import re

def hexs2ascii(hexs):
    """
    HEX string to ascii character.
    """
    return chr(int(hexs, 16))

if __name__ == '__main__':
    string = '666c61677b68656c6c6f5f776f726c647d'
    flag = ''
    for i in re.findall('.{2}', string):
        flag += hexs2ascii(i)
    print flag

