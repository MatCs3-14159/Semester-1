<?php
$conn = new mysqli("localhost", "root", "", "netplix");

if ($conn->connect_error) {
    die("Database connection failed");
}
?>
