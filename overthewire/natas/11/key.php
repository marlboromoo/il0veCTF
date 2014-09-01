<?php
$input = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));

// curl --head  http://natas11:U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK@natas11.natas.labs.overthewire.org/index.php
$output = base64_decode('ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=');

function find_xor_encrypt_key($in, $out) {
    $key = $out;
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    print $text[$i] . " ^ " . $key[$i % strlen($key)] . "\n";
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

print find_xor_encrypt_key($input, $output);


?>
