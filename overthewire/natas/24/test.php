<?php

# Ref: http://tw1.php.net/manual/en/function.strcmp.php
#      http://us.php.net/manual/en/faq.html.php#faq.html.arrays
#

$result = strcmp('foobarspam', Array());
echo 'var_dump(strcpm("foobarspam", Array())) == ';
var_dump($result);
echo 'var_dump(!Null) == ';
var_dump(!Null);

//if (!strcmp('foobarspam', Array())) {
//    var_dump(True);
//} else {
//    var_dump(False);
//}


?>
