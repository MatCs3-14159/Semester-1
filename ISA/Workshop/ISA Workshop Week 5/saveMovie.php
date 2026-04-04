<?php
require "db.php";

$data = json_decode(file_get_contents("php://input"), true);

$title  = $data["title"];
$year   = $data["year"];
$poster = $data["poster"];

$stmt = $conn->prepare(
    "INSERT INTO movies (title, year, poster) VALUES (?, ?, ?)"
);
$stmt->bind_param("sss", $title, $year, $poster);
$stmt->execute();

echo json_encode(["status" => "saved"]);
?>
