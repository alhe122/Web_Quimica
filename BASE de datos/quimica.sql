-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-11-2022 a las 18:00:01
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
-- Estructura de tabla para la tabla `datoscontacto`
--

CREATE TABLE `datoscontacto` (
  `id` int(10) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `telefono` varchar(30) NOT NULL,
  `cel` varchar(20) NOT NULL,
  `direccion` varchar(60) NOT NULL,
  `facebook` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `datoscontacto`
--

INSERT INTO `datoscontacto` (`id`, `correo`, `telefono`, `cel`, `direccion`, `facebook`) VALUES
(1, 'esiq@unjbg.edu.pe', '(052)583000', '', 'Av. Miraflores S/N, Ciudad Universitaria', 'https://es-la.facebook.com/ESIQUNJBG/');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_presentacion`
--

CREATE TABLE `datos_presentacion` (
  `id` int(11) NOT NULL,
  `presentacion` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `datos_presentacion`
--

INSERT INTO `datos_presentacion` (`id`, `presentacion`) VALUES
(1, '¿QUIÉNES SOMOS?'),
(2, 'El Ingeniero Químico, tendrá una formación Integral en el campo científico y tecnológico; será capaz de comprender, incorporar, y enriquecer las denominadas tecnologías emergentes y de adaptarse a los campos tecnológicos.'),
(3, 'Estará capacitado para: planear, dimensionar, diseñar y simular plantas de procesos; formular, ejecutar y evaluar proyectos industriales; supervisar, administrar y controlar procesos industriales; investigar y desarrollar nuevos procesos; adecuar, modificar y optimizar los existentes; planificar, constituir y gerenciar empresas.'),
(4, 'DURACIÓN, GRADOS Y TÍTULOS'),
(5, 'Tiene una duración de 5 años.\r\nGrado Académico de Bachiller en Ciencias con mención en Ingeniería Química.\r\nTítulo Profesional de Ingeniero Químico.'),
(6, 'CAMPO OCUPACIONAL'),
(7, 'Comprende el amplio sector industrial: Refinación de Petróleo y gas natural, polímeros naturales y sintéticos, cemento cerámica y vidrio. Pinturas, lacas barnices y resinas.'),
(8, 'Fertilizantes y explosivos. Industria no metálica (refractarios, mayólica). Industria textil, industria biotecnológica, (fármacos, proteínas y enzimas) Industria de bebidas (cerveza, gaseosa, vinos). Oleorresinas de páprika y orégano. Productos cárnicos y lácteos, industria del papel, azúcar y colorantes. Industria metalúrgica, concentración, fundición y refinación de minerales no férreos. Industria del acero, hidrometalurgia, recubrimientos electroquímicos, sanidad y seguridad medioambiental (Tecnologías limpias, monitoreo, control y tratamientos de contaminante, sistema de seguridad industrial).');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `redes_sociales`
--

CREATE TABLE `redes_sociales` (
  `id` int(11) NOT NULL,
  `nombre_red` varchar(20) NOT NULL,
  `link` varchar(80) NOT NULL,
  `icono_bootstrap` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `redes_sociales`
--

INSERT INTO `redes_sociales` (`id`, `nombre_red`, `link`, `icono_bootstrap`) VALUES
(1, 'Facebook', 'https://es-la.facebook.com/ESIQUNJBG/', 'facebook-f');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `datoscontacto`
--
ALTER TABLE `datoscontacto`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `datos_presentacion`
--
ALTER TABLE `datos_presentacion`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `redes_sociales`
--
ALTER TABLE `redes_sociales`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `datoscontacto`
--
ALTER TABLE `datoscontacto`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `datos_presentacion`
--
ALTER TABLE `datos_presentacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `redes_sociales`
--
ALTER TABLE `redes_sociales`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
