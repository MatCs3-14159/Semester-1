CREATE DATABASE netplix;

USE netplix;

CREATE TABLE movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    year VARCHAR(10),
    poster TEXT,
    searched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);