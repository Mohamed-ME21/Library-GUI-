-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 07, 2024 at 09:28 PM
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
-- Database: `borrow`
--

-- --------------------------------------------------------

--
-- Table structure for table `borr`
--

CREATE TABLE `borr` (
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `book` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `time` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `borr`
--

INSERT INTO `borr` (`name`, `email`, `phone`, `gender`, `book`, `type`, `author`, `time`) VALUES
('Mohamed', 'mhtf12485@gmail.com', '01214556', 'Male', 'Garden Rols', 'Fiction', 'Omar', '1 week'),
('Ana', 'ana12248@gmail.com', '12317952', 'Femal', 'My Hero', 'Fiction', 'Jacson', '2 week'),
('Khaled', 'khaled1459@@gmail.com', '011234841', 'Male', 'Languge Gods', 'Finance', 'Francec', '5 Days'),
('Fatema', 'fat1245@gmail.com', '0111234785', 'Female', 'The Subtle art', 'self help', 'Mark', '10 Days'),
('Sama', 'sama2002@gmail.com', '01111452357', 'Female', 'Emirya', 'Fiction', 'John', '5 Days');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
