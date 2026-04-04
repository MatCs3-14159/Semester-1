<?php
header("Content-Type: application/json");
date_default_timezone_set("UTC");

/* ---------- DATABASE CONFIG ---------- */
$serverName = "185.27.134.213";
$userName   = "if0_41041221";
$password   = "kSaDaMElkf";
$dbName     = "prototype2";

/* ---------- CONNECT ---------- */
$conn = mysqli_connect($serverName, $userName, $password);

if (!$conn) {
    http_response_code(500);
    echo json_encode(["error" => "Database connection failed"]);
    exit;
}

/* ---------- CREATE DATABASE ---------- */
mysqli_query($conn, "CREATE DATABASE IF NOT EXISTS $dbName");
mysqli_select_db($conn, $dbName);

/* ---------- CREATE TABLE ---------- */
$createTable = "
CREATE TABLE IF NOT EXISTS weather (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(100) NOT NULL,
    temp FLOAT NOT NULL,
    humidity FLOAT NOT NULL,
    pressure FLOAT NOT NULL,
    wind FLOAT NOT NULL,
    wind_deg FLOAT DEFAULT 0,
    country VARCHAR(10),
    description VARCHAR(255),
    icon VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);";
mysqli_query($conn, $createTable);

/* ---------- GET PARAMETERS ---------- */
$cityName = $_GET['q'] ?? null;
$lat      = $_GET['lat'] ?? null;
$lon      = $_GET['lon'] ?? null;

$apiKey = "bc4cc58fb2239af96dc490982442ddc4"; // Your OpenWeatherMap API key

/* ---------- DECIDE DATA SOURCE ---------- */
if ($lat && $lon && is_numeric($lat) && is_numeric($lon)) {
    // Coordinates provided, fetch from API
    $url = "https://api.openweathermap.org/data/2.5/weather?lat=$lat&lon=$lon&appid=$apiKey&units=metric";
} else {
    // Use city name or default
    $cityName = $cityName ?? "Portsmouth";
    $citySafe = mysqli_real_escape_string($conn, $cityName);

    // Check cached data in DB (less than 2 hours old)
    $selectData = "
        SELECT * FROM weather
        WHERE city = '$citySafe'
        AND created_at >= NOW() - INTERVAL 2 HOUR
        ORDER BY created_at DESC
        LIMIT 1
    ";
    $result = mysqli_query($conn, $selectData);

    if (mysqli_num_rows($result) > 0) {
        // Return cached data
        $row = mysqli_fetch_assoc($result);
        $output = [
            "name" => $cityName,
            "sys" => ["country" => $row['country']],
            "main" => [
                "temp" => $row['temp'],
                "pressure" => $row['pressure'],
                "humidity" => $row['humidity']
            ],
            "wind" => [
                "speed" => $row['wind'],
                "deg" => $row['wind_deg']
            ],
            "weather" => [
                [
                    "description" => $row['description'],
                    "icon" => $row['icon']
                ]
            ]
        ];
        echo json_encode($output);
        exit;
    }

    // Fetch from API if no cached data
    $apiCity = urlencode($cityName);
    $url = "https://api.openweathermap.org/data/2.5/weather?q=$apiCity&appid=$apiKey&units=metric";
}

/* ---------- FETCH DATA FROM API ---------- */
$response = file_get_contents($url);
$data = json_decode($response, true);

if (!$data || $data['cod'] != 200) {
    http_response_code(404);
    echo json_encode(["error" => "City or location not found"]);
    exit;
}

// Extract data
$cityName    = $data['name'];
$citySafe    = mysqli_real_escape_string($conn, $cityName);
$temp        = $data['main']['temp'];
$humidity    = $data['main']['humidity'];
$pressure    = $data['main']['pressure'];
$wind        = $data['wind']['speed'];
$windDeg     = $data['wind']['deg'] ?? 0;
$country     = $data['sys']['country'];
$description = $data['weather'][0]['description'];
$icon        = $data['weather'][0]['icon'];

/* ---------- INSERT OR UPDATE CACHE ---------- */
$insertData = "
    INSERT INTO weather (city, temp, humidity, pressure, wind, wind_deg, country, description, icon)
    VALUES ('$citySafe', '$temp', '$humidity', '$pressure', '$wind', '$windDeg', '$country', '$description', '$icon')
";
mysqli_query($conn, $insertData);

/* ---------- RETURN JSON ---------- */
$output = [
    "name" => $cityName,
    "sys" => ["country" => $country],
    "main" => [
        "temp" => $temp,
        "pressure" => $pressure,
        "humidity" => $humidity
    ],
    "wind" => [
        "speed" => $wind,
        "deg" => $windDeg
    ],
    "weather" => [
        [
            "description" => $description,
            "icon" => $icon
        ]
    ]
];

echo json_encode($output);
exit;
?>
