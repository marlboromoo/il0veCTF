<?php
$defaultdata = array( "showpassword"=>"yes", "bgcolor"=>"#000000");
//$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

function xor_encrypt($in) {
    $key = 'qw8J';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    print $text[$i] . " ^ " . $key[$i % strlen($key)] . "\n";
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

if (preg_match('/^#(?:[a-f\d]{6})$/i', $defaultdata['bgcolor'])) {
    $res = base64_encode(xor_encrypt(json_encode($defaultdata)));
    print "$res\n";
    $orig = json_decode(xor_encrypt(base64_decode($res)), true);
    print $orig['showpassword'] . " " . $orig['bgcolor'] . "\n";
}

?>
