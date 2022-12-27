-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-12-2022 a las 18:04:29
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `quimica`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_presentacion`
--

CREATE TABLE `datos_presentacion` (
  `id` int(11) NOT NULL,
  `texto` text NOT NULL,
  `imagen1` text NOT NULL,
  `imagen2` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `datos_presentacion`
--

INSERT INTO `datos_presentacion` (`id`, `texto`, `imagen1`, `imagen2`) VALUES
(1, 'Descripción', '2022154433banner1.jpg', '2022154433banner1.jpg');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `datos_presentacion`
--
ALTER TABLE `datos_presentacion`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `datos_presentacion`
--
ALTER TABLE `datos_presentacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
