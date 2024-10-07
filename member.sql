-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 07, 2024 at 09:29 PM
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
-- Database: `registration`
--

-- --------------------------------------------------------

--
-- Table structure for table `member`
--

CREATE TABLE `member` (
  `frist name` varchar(100) NOT NULL,
  `middle name` varchar(100) NOT NULL,
  `last name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `con_password` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `member`
--

INSERT INTO `member` (`frist name`, `middle name`, `last name`, `email`, `password`, `con_password`, `gender`) VALUES
('John', 'Nichlos', 'Klos', 'klos4587@gmail.com', '1234', '1234', 'Male'),
('Sara', 'Josaf', 'Barkola', 'sara1485@gmail.com', 'sara123', 'sara123', 'Femal'),
('John', 'Seimony', 'Xiav', 'john4581@gmail.com', 'john4581', 'john4581', 'Male'),
('Ana', 'De', 'Armes', 'ana1457@gmail.com', 'ana1457', 'ana1457', 'Femal'),
('Mohamud', 'Ahmed', 'Wrshana', 'mohamud1248@gmail.com', 'mohamud123', 'mohamud123', 'Male'),
('Salma', 'Saad', 'Gaoud', 'salma1458@gmail.com', 'salma123', 'salma123', 'Femal');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
