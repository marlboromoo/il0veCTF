<?php
    $encodedSecret = "3d3d516343746d4d6d6c315669563362";
    # bin2hex(strrev(base64_encode($secret)));
    echo base64_decode(strrev(hex2bin($encodedSecret)));
?>
