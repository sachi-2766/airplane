-- MySQL dump 10.13  Distrib 5.5.27, for Win32 (x86)
--
-- Host: localhost    Database: passenger
-- ------------------------------------------------------
-- Server version	5.5.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE Database passenger;
use passenger;
--
-- Table structure for table `flights`
--

DROP TABLE IF EXISTS `flights`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `flights` (
  `flightno` int(50) DEFAULT NULL,
  `source` varchar(50) DEFAULT NULL,
  `destination` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flights`
--

LOCK TABLES `flights` WRITE;
/*!40000 ALTER TABLE `flights` DISABLE KEYS */;
INSERT INTO `flights` VALUES (1,'mumbai','kolkata'),(2,'mumbai','delhi'),(3,'mumbai','chennai'),(4,'kolkata','mumbai'),(5,'kolkata','delhi'),(6,'kolkata','chennai'),(7,'delhi','mumbai'),(8,'delhi','kolkata'),(9,'delhi','chennai'),(10,'chennai','mumbai'),(11,'chennai','kolkata'),(12,'chennai','delhi');
/*!40000 ALTER TABLE `flights` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `login` (
  `name` varchar(50) DEFAULT NULL,
  `age` int(10) DEFAULT NULL,
  `email_id` varchar(50) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES ('sachi',17,'xyz@gmail.com','z','z'),('sneha',12,'s2006@gmail.com','sd','sdf'),('sneha',12,'s@gmail.com','sd','sdf'),('sachi',17,'sachi@gmail.com','a','a'),('sneha',17,'s2006@gmail.com','s','s');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticketdetails`
--

DROP TABLE IF EXISTS `ticketdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ticketdetails` (
  `seatno` int(50) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `age` int(25) DEFAULT NULL,
  `flight` varchar(50) DEFAULT NULL,
  `sourceNdestination` varchar(50) DEFAULT NULL,
  `timeofflight` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticketdetails`
--

LOCK TABLES `ticketdetails` WRITE;
/*!40000 ALTER TABLE `ticketdetails` DISABLE KEYS */;
INSERT INTO `ticketdetails` VALUES (731399,'Sid','M',18,'1','7','4','2024-01-24');
/*!40000 ALTER TABLE `ticketdetails` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-16 19:30:29
