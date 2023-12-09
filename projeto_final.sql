-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: bancoatleta
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `adicionaalimentodieta`
--

DROP TABLE IF EXISTS `adicionaalimentodieta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `adicionaalimentodieta` (
  `fk_Alimento_ID` int DEFAULT NULL,
  `fk_DietaMontada_ID` int DEFAULT NULL,
  `Refeicao` varchar(25) DEFAULT NULL,
  `AlimentoDieta_ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`AlimentoDieta_ID`),
  KEY `FK_AdicionaAlimentoDieta_1` (`fk_Alimento_ID`),
  KEY `FK_AdicionaAlimentoDieta_2` (`fk_DietaMontada_ID`),
  CONSTRAINT `FK_AdicionaAlimentoDieta_1` FOREIGN KEY (`fk_Alimento_ID`) REFERENCES `alimento` (`ID`) ON DELETE RESTRICT,
  CONSTRAINT `FK_AdicionaAlimentoDieta_2` FOREIGN KEY (`fk_DietaMontada_ID`) REFERENCES `dietamontada` (`ID`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adicionaalimentodieta`
--

LOCK TABLES `adicionaalimentodieta` WRITE;
/*!40000 ALTER TABLE `adicionaalimentodieta` DISABLE KEYS */;
/*!40000 ALTER TABLE `adicionaalimentodieta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `adicionaexerciciotreino`
--

DROP TABLE IF EXISTS `adicionaexerciciotreino`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `adicionaexerciciotreino` (
  `fk_Exercicio_ID` int DEFAULT NULL,
  `fk_TreinoMontado_ID` int DEFAULT NULL,
  `Dia` char(1) DEFAULT NULL,
  `ExercicioTreino_ID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ExercicioTreino_ID`),
  KEY `FK_AdicionaExercicioTreino_1` (`fk_Exercicio_ID`),
  KEY `FK_AdicionaExercicioTreino_2` (`fk_TreinoMontado_ID`),
  CONSTRAINT `FK_AdicionaExercicioTreino_1` FOREIGN KEY (`fk_Exercicio_ID`) REFERENCES `exercicio` (`ID`) ON DELETE RESTRICT,
  CONSTRAINT `FK_AdicionaExercicioTreino_2` FOREIGN KEY (`fk_TreinoMontado_ID`) REFERENCES `treinomontado` (`ID`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adicionaexerciciotreino`
--

LOCK TABLES `adicionaexerciciotreino` WRITE;
/*!40000 ALTER TABLE `adicionaexerciciotreino` DISABLE KEYS */;
/*!40000 ALTER TABLE `adicionaexerciciotreino` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alimento`
--

DROP TABLE IF EXISTS `alimento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alimento` (
  `Proteina` int DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  `Caloria` int DEFAULT NULL,
  `Carboidrato` int DEFAULT NULL,
  `Gordura` int DEFAULT NULL,
  `Nome` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alimento`
--

LOCK TABLES `alimento` WRITE;
/*!40000 ALTER TABLE `alimento` DISABLE KEYS */;
/*!40000 ALTER TABLE `alimento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alimentoconsumido`
--

DROP TABLE IF EXISTS `alimentoconsumido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alimentoconsumido` (
  `Quantidade` int DEFAULT NULL,
  `ID_AlimentoConsumido` int NOT NULL AUTO_INCREMENT,
  `fk_Atleta_Cpf` varchar(14) DEFAULT NULL,
  `fk_Alimento_ID` int DEFAULT NULL,
  `Data_Registro` date DEFAULT NULL,
  `Caloria_Total` int DEFAULT NULL,
  PRIMARY KEY (`ID_AlimentoConsumido`),
  KEY `FK_AlimentoConsumido_2` (`fk_Atleta_Cpf`),
  KEY `FK_AlimentoConsumido_3` (`fk_Alimento_ID`),
  CONSTRAINT `FK_AlimentoConsumido_2` FOREIGN KEY (`fk_Atleta_Cpf`) REFERENCES `atleta` (`Cpf`),
  CONSTRAINT `FK_AlimentoConsumido_3` FOREIGN KEY (`fk_Alimento_ID`) REFERENCES `alimento` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alimentoconsumido`
--

LOCK TABLES `alimentoconsumido` WRITE;
/*!40000 ALTER TABLE `alimentoconsumido` DISABLE KEYS */;
/*!40000 ALTER TABLE `alimentoconsumido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `atleta`
--

DROP TABLE IF EXISTS `atleta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `atleta` (
  `Nome` varchar(255) DEFAULT NULL,
  `Peso` float DEFAULT NULL,
  `Sexo` char(1) DEFAULT NULL,
  `Idade` int DEFAULT NULL,
  `Objetivo` varchar(255) DEFAULT NULL,
  `Cpf` varchar(14) NOT NULL,
  `Altura_cm` int DEFAULT NULL,
  PRIMARY KEY (`Cpf`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `atleta`
--

LOCK TABLES `atleta` WRITE;
/*!40000 ALTER TABLE `atleta` DISABLE KEYS */;
/*!40000 ALTER TABLE `atleta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dietamontada`
--

DROP TABLE IF EXISTS `dietamontada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dietamontada` (
  `Data_Registro` date DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  `fk_Atleta_Cpf` varchar(14) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `FK_DietaMontada_2` (`fk_Atleta_Cpf`),
  CONSTRAINT `FK_DietaMontada_2` FOREIGN KEY (`fk_Atleta_Cpf`) REFERENCES `atleta` (`Cpf`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dietamontada`
--

LOCK TABLES `dietamontada` WRITE;
/*!40000 ALTER TABLE `dietamontada` DISABLE KEYS */;
/*!40000 ALTER TABLE `dietamontada` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `execiciorealizado`
--

DROP TABLE IF EXISTS `execiciorealizado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `execiciorealizado` (
  `Data_Registro` date DEFAULT NULL,
  `ID_ExercicioRealizado` int NOT NULL AUTO_INCREMENT,
  `Repeticoes` int DEFAULT NULL,
  `Series` int DEFAULT NULL,
  `Carga` int DEFAULT NULL,
  `fk_Atleta_Cpf` varchar(14) DEFAULT NULL,
  `fk_Exercicio_ID` int DEFAULT NULL,
  PRIMARY KEY (`ID_ExercicioRealizado`),
  KEY `FK_ExecicioRealizado_2` (`fk_Atleta_Cpf`),
  KEY `FK_ExecicioRealizado_3` (`fk_Exercicio_ID`),
  CONSTRAINT `FK_ExecicioRealizado_2` FOREIGN KEY (`fk_Atleta_Cpf`) REFERENCES `atleta` (`Cpf`),
  CONSTRAINT `FK_ExecicioRealizado_3` FOREIGN KEY (`fk_Exercicio_ID`) REFERENCES `exercicio` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `execiciorealizado`
--

LOCK TABLES `execiciorealizado` WRITE;
/*!40000 ALTER TABLE `execiciorealizado` DISABLE KEYS */;
/*!40000 ALTER TABLE `execiciorealizado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exercicio`
--

DROP TABLE IF EXISTS `exercicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exercicio` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Grupo_Muscular` varchar(50) DEFAULT NULL,
  `Nome` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exercicio`
--

LOCK TABLES `exercicio` WRITE;
/*!40000 ALTER TABLE `exercicio` DISABLE KEYS */;
/*!40000 ALTER TABLE `exercicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `treinomontado`
--

DROP TABLE IF EXISTS `treinomontado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `treinomontado` (
  `Data_Registro` date DEFAULT NULL,
  `ID` int NOT NULL AUTO_INCREMENT,
  `fk_Atleta_Cpf` varchar(14) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `FK_TreinoMontado_2` (`fk_Atleta_Cpf`),
  CONSTRAINT `FK_TreinoMontado_2` FOREIGN KEY (`fk_Atleta_Cpf`) REFERENCES `atleta` (`Cpf`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `treinomontado`
--

LOCK TABLES `treinomontado` WRITE;
/*!40000 ALTER TABLE `treinomontado` DISABLE KEYS */;
/*!40000 ALTER TABLE `treinomontado` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-06 21:47:30
