-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 07, 2024 at 09:26 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mylibrary`
--

-- --------------------------------------------------------

--
-- Table structure for table `mylib`
--

CREATE TABLE `mylib` (
  `id` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `country` varchar(100) NOT NULL,
  `rating` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mylib`
--

INSERT INTO `mylib` (`id`, `name`, `type`, `author`, `country`, `rating`) VALUES
(1, 'Gardn Rols', 'fictions', 'omar', 'EG', '⭐⭐⭐⭐'),
(2, 'Rich dad and poor dad', 'Financ', 'Robort', 'UK', '⭐⭐⭐⭐'),
(3, 'Pride and Prejudice', 'Criticism', 'Jane Austen', 'UK', '⭐⭐⭐'),
(4, 'Zekol\'s land', 'fictions', 'omar', 'EG', '⭐⭐⭐⭐');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mylib`
--
ALTER TABLE `mylib`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
