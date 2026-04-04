<?php
require "db.php";

$result = $conn->query("SELECT * FROM movies ORDER BY searched_at DESC");

echo "<h2>Saved Movies:</h2>";
echo "<table border='1' cellpadding='10'>";
echo "<tr><th>ID</th><th>Title</th><th>Year</th><th>Poster</th><th>Searched At</th></tr>";

while ($row = $result->fetch_assoc()) {
    echo "<tr>
            <td>".$row['id']."</td>
            <td>".$row['title']."</td>
            <td>".$row['year']."</td>
            <td><img src='".$row['poster']."' width='50'></td>
            <td>".$row['searched_at']."</td>
          </tr>";
}

echo "</table>";
?>