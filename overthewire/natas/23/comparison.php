<?php
    $passwd = '11iloveyou';

    var_dump($passwd);
    $foo = strstr($passwd,"iloveyou");
    var_dump($foo);
    # http://php.net/manual/en/language.types.string.php#language.types.string.conversion
    #  http://php.net/manual/en/language.operators.comparison.php
    //var_dump('11aaa' > 10);
    $bar = ($passwd >10);
    var_dump($bar);

    if(strstr($passwd,"iloveyou") && ($passwd > 10 )){
        echo "<br>The credentials for the next level are:<br>";
        echo "<pre>Username: natas24 Password: <censored></pre>";
    }
    else{
        echo "<br>Wrong!<br>";
    }
    // morla / 10111
?>
