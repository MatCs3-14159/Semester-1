<?php
session_start();

$host = "localhost";          // InfinityFree: use provided DB host
$user = "root";               // Change in hosting
$pass = "";
$db   = "derivix_db";

$conn = new mysqli($host, $user, $pass, $db);

if ($conn->connect_error) {
    http_response_code(500);
    die(json_encode(["error" => "Database connection failed"]));
}

header("Content-Type: application/json");
?>
