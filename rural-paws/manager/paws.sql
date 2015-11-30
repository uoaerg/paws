-- phpMyAdmin SQL Dump
-- version 3.4.11.1deb2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 17, 2014 at 04:27 PM
-- Server version: 5.5.33
-- PHP Version: 5.4.4-14+deb7u7

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `paws`
--

-- --------------------------------------------------------

--
-- Table structure for table `global_approved_domains`
--

CREATE TABLE IF NOT EXISTS `global_approved_domains` (
  `domain` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `global_approved_domains`
--

INSERT INTO `global_approved_domains` (`domain`) VALUES
('.ac.uk'),
('.gov.uk'),
('.judiciary.uk'),
('.mod.uk'),
('.nhs.uk'),
('.parliament.uk'),
('.police.uk'),
('.sch.uk'),
('.bl.uk'),
('.british-library.uk'),
('.jspc.uk'),
('.nls.uk'),
('.supremecourt.uk');

-- --------------------------------------------------------

--
-- Table structure for table `global_settings`
--

CREATE TABLE IF NOT EXISTS `global_settings` (
  `key` varchar(60) NOT NULL,
  `value` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `global_settings`
--

INSERT INTO `global_settings` (`key`, `value`) VALUES
('device_speed', 64000),
('link_speed', 256000);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
