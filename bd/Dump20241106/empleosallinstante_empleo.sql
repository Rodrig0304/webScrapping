-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: empleosallinstante
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `empleo`
--

DROP TABLE IF EXISTS `empleo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empleo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tituloEmpleo` varchar(255) NOT NULL,
  `nombreEmpresa` varchar(255) NOT NULL,
  `ubicacionEmpleo` varchar(255) NOT NULL,
  `salario` varchar(150) NOT NULL,
  `fechaPublicacion` varchar(50) NOT NULL,
  `enlaceOferta` text NOT NULL,
  `tipoTrabajo` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleo`
--

LOCK TABLES `empleo` WRITE;
/*!40000 ALTER TABLE `empleo` DISABLE KEYS */;
INSERT INTO `empleo` VALUES (52,'Desarrollador Full Stack Jr','Instituto Nacional Electoral','Ciudad de México DF, Iztapalapa','No disponible','Hace  1  hora','https://mx.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-desarrollador-full-stack-jr-en-iztapalapa-28DD764F3470D8FD61373E686DCF3405#lc=ListOffers-Score4-0','No disponible'),(53,'Desarrollador Full Stack','Instituto Nacional Electoral','Ciudad de México DF, Iztapalapa','No disponible','Hace  1  hora','https://mx.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-desarrollador-full-stack-en-iztapalapa-1AC5CBE0E942979461373E686DCF3405#lc=ListOffers-Score4-1','No disponible'),(54,'Desarrollador/a','SMARTSOFT AMERICA BUSINESS APPLICATIONS','Tlaxcala, Chiautempan','No disponible','Hace  1  hora','https://mx.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-desarrolladora-completo-en-chiautempan-C3774DB556A5D42F61373E686DCF3405#lc=ListOffers-Score4-2','No disponible'),(55,'Desarrollador Jr.','PROGRESO ECONOMICO ELEVA','Querétaro, Querétaro','No disponible','Hace  7  horas','https://mx.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-desarrollador-jr-experiencia-en-aplicativos-moviles-en-queretaro-935C3CF151CD18AD61373E686DCF3405#lc=ListOffers-Score4-3','No disponible'),(56,'Desarrollador/a','GN3 Software','Estado de México, Cuautitlán Izcalli','No disponible','Hace  7  horas','https://mx.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-desarrolladora-movil-en-cuautitlan-izcalli-FFCF02A084734AA761373E686DCF3405#lc=ListOffers-Score4-4','No disponible'),(57,'Programador Frontend Proactivo con Conocimientos en HTML, JavaScript y CSS, trabajo remoto','Commrs','Ciudad de México DF, Miguel Hidalgo','No disponible','Ayer','https://mx.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-programador-frontend-proactivo-con-conocimientos-en-html-javascript-y-css-en-miguel-hidalgo-F1E25625ADAAFCCF61373E686DCF3405#lc=ListOffers-Score4-5','No disponible'),(58,'Analista programador','Tecnológico de Estudios Superiores Ecatepec','Estado de México, Ecatepec de Morelos','No disponible','Ayer','https://mx.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-analista-programador-en-ecatepec-de-morelos-E6DEFDF9E96F192E61373E686DCF3405#lc=ListOffers-Score4-6','No disponible'),(59,'Programador JR','Grupo Médico Internacional, S.C. \"PRO-MED GRUPO MEDICO\"','Baja California, Mexicali','No disponible','Hace  1  hora','https://mx.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-programador-jr-con-experiencia-en-mexicali-FFD9B41B3DE504E061373E686DCF3405#lc=ListOffers-Score4-7','No disponible'),(60,'Programador CNC','Indeinn','Aguascalientes, Aguascalientes','No disponible','Hace  1  hora','https://mx.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-programador-cnc-en-aguascalientes-6027600F5BB6AA1C61373E686DCF3405#lc=ListOffers-Score4-8','No disponible'),(61,'Desarrollador','Empresa no disponible','Ciudad de México DF, Tlalpan','No disponible','Hace  1  hora','https://mx.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-desarrollador-en-tlalpan-C5931205E442899761373E686DCF3405#lc=ListOffers-Score4-9','No disponible'),(62,'Desarrollador Backend / vacante híbrida','Pentafon Contact Center & BPO','Estado de México, Nezahualcóyotl','No disponible','Hace  1  hora','https://mx.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-desarrollador-backend-vacante-hibrida-en-nezahualcoyotl-D810128142B4305C61373E686DCF3405#lc=ListOffers-Score4-10','No disponible'),(63,'Desarrollador Backend / vacante híbrida','Pentafon Contact Center & BPO','Estado de México, Tlalnepantla de Baz','No disponible','Hace  1  hora','https://mx.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-desarrollador-backend-vacante-hibrida-en-tlalnepantla-de-baz-6D5A89B148DB404D61373E686DCF3405#lc=ListOffers-Score4-11','No disponible'),(64,'Desarrollador Backend / vacante híbrida','Pentafon Contact Center & BPO','Estado de México, Ecatepec de Morelos','No disponible','Hace  1  hora','https://mx.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-desarrollador-backend-vacante-hibrida-en-ecatepec-de-morelos-04E3BF3C98D82D4561373E686DCF3405#lc=ListOffers-Score4-12','No disponible'),(65,'Desarrollador Backend / vacante híbrida','Pentafon Contact Center & BPO','Estado de México, Naucalpan de Juárez','No disponible','Hace  1  hora','https://mx.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-desarrollador-backend-vacante-hibrida-en-naucalpan-de-juarez-57370F1268BAE85761373E686DCF3405#lc=ListOffers-Score4-13','No disponible'),(66,'Desarrollador Jr','Consultoria y Entrenamiento de Puebla','Ciudad de México DF, Gustavo A. Madero','No disponible','Hace  1  hora','https://mx.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-desarrollador-jr-experiencia-minima-en-gustavo-a-madero-1FFFF6C54D39C4B661373E686DCF3405#lc=ListOffers-Score4-14','No disponible'),(67,'Desarrollador iOS','Asteci','Ciudad de México DF, Tlalpan','No disponible','Hace  1  hora','https://mx.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-desarrollador-ios-en-tlalpan-9D20FC9D35206C0261373E686DCF3405#lc=ListOffers-Score4-15','No disponible'),(68,'Desarrollador Oracle Plsql','Asteci','Ciudad de México DF, Tlalpan','No disponible','Hace  1  hora','https://mx.computrabajo.com/ofertas-de-trabajo/oferta-de-trabajo-de-desarrollador-oracle-plsql-en-tlalpan-DB494F04FF8BB1A861373E686DCF3405#lc=ListOffers-Score4-16','No disponible');
/*!40000 ALTER TABLE `empleo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-06 21:00:25
