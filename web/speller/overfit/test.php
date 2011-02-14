<?php
header("Content-Type: text/plain");
$query = $_GET['q'];

$dataset = file("dataset.txt");
$dictionary = array();
foreach ($dataset as $line) {
    $keyvalue = explode("\t", trim($line), 2); 
    $dictionary[$keyvalue[0]] = $keyvalue[1];
}
if (array_key_exists($query, $dictionary)) {
    $candidates = explode("\t", $dictionary[$query]);
    $first = array_shift($candidates);
    echo "$first\t1.0\n";
    foreach ($candidates as $cand) {
        echo "$cand\t0.0\n";
    }
} else {
    echo "$query\t1.0\n";
}
