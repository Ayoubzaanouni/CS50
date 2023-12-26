-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 28, 2022 at 02:52 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gestion_seances`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `aemail` varchar(255) NOT NULL,
  `apassword` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`aemail`, `apassword`) VALUES
('zaanouniab@gmail.com', '123');

-- --------------------------------------------------------

--
-- Table structure for table `kine`
--

CREATE TABLE `kine` (
  `idk` int(11) NOT NULL,
  `nomk` varchar(255) DEFAULT NULL,
  `prenomk` varchar(255) DEFAULT NULL,
  `emailk` varchar(255) DEFAULT NULL,
  `mdpk` varchar(255) DEFAULT NULL,
  `telk` varchar(15) DEFAULT NULL,
  `ville` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `kine`
--

INSERT INTO `kine` (`idk`, `nomk`, `prenomk`, `emailk`, `mdpk`, `telk`, `ville`) VALUES
(15, '1', 'physio', 'physio1@gmail.com', '123', '987654', 'sousse'),
(16, '2', 'physio', 'physio2@gmail.com', '123', '98765431', 'monastir');

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `idp` int(11) NOT NULL,
  `nomp` varchar(255) DEFAULT NULL,
  `prenomp` varchar(255) DEFAULT NULL,
  `numtelp` varchar(15) DEFAULT NULL,
  `emailp` varchar(255) DEFAULT NULL,
  `mdpp` varchar(255) DEFAULT NULL,
  `ville` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`idp`, `nomp`, `prenomp`, `numtelp`, `emailp`, `mdpp`, `ville`) VALUES
(18, '1', 'patient', '82618022', 'patient1@gmail.com', '123', 'sousse'),
(19, '2', 'patient', '832901', 'patient2@gmail.com', '123', 'sfax'),
(20, '3', 'patient', '765432112', 'patient3@gmail.com', '123', 'tunisia');

-- --------------------------------------------------------

--
-- Table structure for table `seance`
--

CREATE TABLE `seance` (
  `id` int(11) NOT NULL,
  `idk` int(11) NOT NULL,
  `idp` int(11) NOT NULL,
  `dates` date NOT NULL,
  `heurs` time NOT NULL,
  `idso` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `seance`
--

INSERT INTO `seance` (`id`, `idk`, `idp`, `dates`, `heurs`, `idso`) VALUES
(51, 16, 18, '2022-12-15', '17:36:00', 11),
(54, 16, 19, '2022-12-09', '08:35:00', 11),
(55, 16, 19, '2022-12-28', '21:36:00', 10),
(57, 16, 20, '2022-12-29', '17:41:00', 1),
(58, 16, 18, '2022-12-27', '18:39:00', 1),
(63, 15, 18, '2022-12-27', '21:15:00', 11);

-- --------------------------------------------------------

--
-- Table structure for table `soins`
--

CREATE TABLE `soins` (
  `idso` int(11) NOT NULL,
  `names` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `soins`
--

INSERT INTO `soins` (`idso`, `names`) VALUES
(1, 'respiratoire'),
(2, 'cardio-vasculaire'),
(3, 'la neurologie'),
(4, 'vestibulaire'),
(5, 'post-chirurgie'),
(6, 'l’accompagnement post-cancer'),
(7, 'la pédiatrie'),
(8, 'la gériatrie'),
(9, 'Rééducation du genou'),
(10, 'Rééducation de l’épaule'),
(11, 'Rééducation de la main'),
(12, 'Rééducation de la cheville et du pied');

-- --------------------------------------------------------

--
-- Table structure for table `webuser`
--

CREATE TABLE `webuser` (
  `email` varchar(255) NOT NULL,
  `usertype` varchar(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `webuser`
--

INSERT INTO `webuser` (`email`, `usertype`) VALUES
('patient1@gmail.com', 'p'),
('patient2@gmail.com', 'p'),
('patient3@gmail.com', 'p'),
('physio1@gmail.com', 'k'),
('physio2@gmail.com', 'k'),
('zaanouniab@gmail.com', 'a');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`aemail`);

--
-- Indexes for table `kine`
--
ALTER TABLE `kine`
  ADD PRIMARY KEY (`idk`),
  ADD UNIQUE KEY `UC_email_kine` (`emailk`),
  ADD UNIQUE KEY `UC_tel_kine` (`telk`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`idp`),
  ADD UNIQUE KEY `UC_email_patient` (`emailp`),
  ADD UNIQUE KEY `UC_tel_patient` (`numtelp`);

--
-- Indexes for table `seance`
--
ALTER TABLE `seance`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idk` (`idk`),
  ADD KEY `idp` (`idp`),
  ADD KEY `idso` (`idso`);

--
-- Indexes for table `soins`
--
ALTER TABLE `soins`
  ADD PRIMARY KEY (`idso`);

--
-- Indexes for table `webuser`
--
ALTER TABLE `webuser`
  ADD PRIMARY KEY (`email`),
  ADD UNIQUE KEY `UC_email_users` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `kine`
--
ALTER TABLE `kine`
  MODIFY `idk` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `patient`
--
ALTER TABLE `patient`
  MODIFY `idp` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `seance`
--
ALTER TABLE `seance`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `seance`
--
ALTER TABLE `seance`
  ADD CONSTRAINT `idk` FOREIGN KEY (`idk`) REFERENCES `kine` (`idk`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `idp` FOREIGN KEY (`idp`) REFERENCES `patient` (`idp`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `idso` FOREIGN KEY (`idso`) REFERENCES `soins` (`idso`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `seance_ibfk_1` FOREIGN KEY (`idp`) REFERENCES `patient` (`idp`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `seance_ibfk_2` FOREIGN KEY (`idso`) REFERENCES `soins` (`idso`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
