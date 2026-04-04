-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 03, 2026 at 12:52 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `prototype2`
--

-- --------------------------------------------------------

--
-- Table structure for table `weather`
--

CREATE TABLE `weather` (
  `id` int(11) NOT NULL,
  `city` varchar(100) NOT NULL,
  `temp` float NOT NULL,
  `humidity` float NOT NULL,
  `pressure` float NOT NULL,
  `wind` float NOT NULL,
  `wind_deg` float DEFAULT 0,
  `country` varchar(10) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `icon` varchar(10) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `weather`
--

INSERT INTO `weather` (`id`, `city`, `temp`, `humidity`, `pressure`, `wind`, `wind_deg`, `country`, `description`, `icon`, `created_at`) VALUES
(1, 'Portsmouth', 8.71, 95, 1017, 3.79, 159, 'GB', 'overcast clouds', '04d', '2026-01-18 10:49:11'),
(2, 'Biratnagar', 22.86, 35, 1010, 2.56, 257, 'NP', 'clear sky', '01d', '2026-01-18 10:50:12'),
(3, 'Portsmouth', 9.73, 92, 1016, 2.08, 140, 'GB', 'overcast clouds', '04n', '2026-01-18 16:46:29'),
(4, 'Kathmandu', 10.12, 87, 1016, 1.03, 0, 'NP', 'few clouds', '02n', '2026-01-18 16:46:47'),
(5, 'Delhi', 14.05, 88, 1014, 1.54, 80, 'IN', 'mist', '50n', '2026-01-18 16:46:52'),
(6, 'England', -3.25, 37, 1027, 3.14, 252, 'US', 'clear sky', '01d', '2026-01-18 16:47:01'),
(7, 'Beijing', -7.06, 22, 1037, 5.4, 7, 'CN', 'overcast clouds', '04n', '2026-01-18 16:47:14'),
(8, 'Damak', 16.99, 52, 1014, 2.45, 346, 'NP', 'clear sky', '01n', '2026-01-18 16:47:43'),
(9, 'Portsmouth', 9, 96, 1012, 3.6, 167, 'GB', 'overcast clouds', '04n', '2026-01-19 06:18:00'),
(10, 'Portsmouth', 10.3, 81, 999, 1.79, 225, 'GB', 'overcast clouds', '04d', '2026-01-31 12:57:23'),
(11, 'London', 10.39, 79, 999, 3.09, 180, 'GB', 'broken clouds', '04d', '2026-01-31 13:10:07'),
(12, 'Portsmouth', 9.17, 86, 1000, 3.58, 188, 'GB', 'overcast clouds', '04d', '2026-01-31 16:15:05'),
(13, 'Biratnagar', 16.89, 59, 1017, 2.83, 290, 'NP', 'overcast clouds', '04n', '2026-01-31 16:15:57'),
(14, 'Kathmandu', 11.12, 82, 1020, 1.54, 90, 'NP', 'scattered clouds', '03n', '2026-01-31 16:20:59'),
(15, 'Portsmouth', 7.79, 96, 1002, 1.34, 221, 'GB', 'light rain', '10d', '2026-02-01 09:02:41'),
(16, 'Kathmandu', 20.12, 40, 1014, 3.09, 230, 'NP', 'few clouds', '02d', '2026-02-01 09:03:11'),
(17, 'Portsmouth', 6.96, 86, 991, 3.13, 67, 'GB', 'overcast clouds', '04n', '2026-02-02 20:58:15'),
(18, 'Portsmouth', 5.93, 94, 990, 2.68, 69, 'GB', 'light rain', '10n', '2026-02-03 06:37:48'),
(19, 'Biratnagar', 25.89, 38, 1019, 2, 150, 'NP', 'broken clouds', '04d', '2026-02-03 06:39:17');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `weather`
--
ALTER TABLE `weather`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `weather`
--
ALTER TABLE `weather`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
