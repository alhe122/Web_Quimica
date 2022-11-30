-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-11-2022 a las 17:56:32
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
-- Estructura de tabla para la tabla `datos_autoridades`
--

CREATE TABLE `datos_autoridades` (
  `id` int(11) NOT NULL,
  `cargo` text NOT NULL,
  `nombre` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `datos_autoridades`
--

INSERT INTO `datos_autoridades` (`id`, `cargo`, `nombre`) VALUES
(1, 'DECANO DE LA FACULTAD DE INGENIERÍA', 'Dr. Jesús Plácido Medina Salas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_comites`
--

CREATE TABLE `datos_comites` (
  `id` int(11) NOT NULL,
  `link_resolucion` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `datos_comites`
--

INSERT INTO `datos_comites` (`id`, `link_resolucion`) VALUES
(1, 'https://drive.google.com/file/d/1sJQMym_iECMRvqIQRHqdkwJJdIM6XG3Q/view');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_historica`
--

CREATE TABLE `datos_historica` (
  `id` int(11) NOT NULL,
  `texto` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `datos_historica`
--

INSERT INTO `datos_historica` (`id`, `texto`) VALUES
(1, 'Hola Mundo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_horarios`
--

CREATE TABLE `datos_horarios` (
  `id` int(11) NOT NULL,
  `texto` text NOT NULL,
  `link` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `datos_horarios`
--

INSERT INTO `datos_horarios` (`id`, `texto`, `link`) VALUES
(1, 'SEMESTRE 2022-II', 'https://www.facebook.com/ESIQUNJBG/posts/pfbid0DAzWJkLRVZCBLW6Ea887yqaJ2yis6JW6nzo9VSi8CCmphHC9WBCETjGpFDGkB8FLl?__cft__[0]=AZV5aNweM0xCb_LXn9BPvPYZEOFu7XodMvbcrLa4kUpBFeZltMYkWCFzP-41leSSHj61Y6MNmKPon2xHwjc_1iQMcXekiZXqNHLfwtFQu1qxkoJas9Gk4cZQjp8Db-bIClvfLkjmxdlRnzOPAUhTg3ThtAX8sA3oBFXmuXWP-45xCquSxKp7WjNygwXjWyrg64oWliDdi3S_q8oNsYRCkZIe&__tn__=%2CO%2CP-R');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_malla`
--

CREATE TABLE `datos_malla` (
  `id` int(11) NOT NULL,
  `texto` text NOT NULL,
  `link` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `datos_malla`
--

INSERT INTO `datos_malla` (`id`, `texto`, `link`) VALUES
(1, 'MALLA CURRICULAR DE LA E.P. DE INGENIERÍA QUÍMICA 2018', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_misionvision`
--

CREATE TABLE `datos_misionvision` (
  `id` int(11) NOT NULL,
  `mision_vision` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `datos_misionvision`
--

INSERT INTO `datos_misionvision` (`id`, `mision_vision`) VALUES
(1, '“Brindar formación profesional humanista, científica y tecnológica a los estudiantes universitarios con calidad y responsabilidad social.”'),
(2, '“Los peruanos acceden a una educación que les permite desarrollar su potencial desde la primera infancia y convertirse en ciudadanos que valoran su cultura, conocen sus derechos, y responsabilidades, desarrollan sus talentos y participan de manera innovadora, competitiva y comprometida en las dinámicas sociales, contribuyendo al desarrollo de sus comunidades y del país en su conjunto.”');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_objetivos`
--

CREATE TABLE `datos_objetivos` (
  `id` int(11) NOT NULL,
  `texto` text NOT NULL,
  `es_titulo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `datos_objetivos`
--

INSERT INTO `datos_objetivos` (`id`, `texto`, `es_titulo`) VALUES
(1, 'OBJETIVOS', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_plan-estudios`
--

CREATE TABLE `datos_plan-estudios` (
  `id` int(11) NOT NULL,
  `texto` text NOT NULL,
  `link` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `datos_plan-estudios`
--

INSERT INTO `datos_plan-estudios` (`id`, `texto`, `link`) VALUES
(1, 'Plan de estudios F1-2014', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_presentacion`
--

CREATE TABLE `datos_presentacion` (
  `id` int(11) NOT NULL,
  `presentacion` text NOT NULL,
  `Es_titulo` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `datos_presentacion`
--

INSERT INTO `datos_presentacion` (`id`, `presentacion`, `Es_titulo`) VALUES
(1, 'Descripción', 1),
(2, 'El Ingeniero Químico, tendrá una formación Integral en el campo científico y tecnológico; será capaz de comprender, incorporar, y enriquecer las denominadas tecnologías emergentes y de adaptarse a los campos tecnológicos.', 0),
(3, 'Estará capacitado para: planear, dimensionar, diseñar y simular plantas de procesos; formular, ejecutar y evaluar proyectos industriales; supervisar, administrar y controlar procesos industriales; investigar y desarrollar nuevos procesos; adecuar, modificar y optimizar los existentes; planificar, constituir y gerenciar empresas.', 0),
(4, 'DURACIÓN, GRADOS Y TÍTULOS', 1),
(5, 'Tiene una duración de 5 años.\r\nGrado Académico de Bachiller en Ciencias con mención en Ingeniería Química.\r\nTítulo Profesional de Ingeniero Químico.', 0),
(6, 'CAMPO OCUPACIONAL', 1),
(7, 'Comprende el amplio sector industrial: Refinación de Petróleo y gas natural, polímeros naturales y sintéticos, cemento cerámica y vidrio. Pinturas, lacas barnices y resinas.', 0),
(8, 'Fertilizantes y explosivos. Industria no metálica (refractarios, mayólica). Industria textil, industria biotecnológica, (fármacos, proteínas y enzimas) Industria de bebidas (cerveza, gaseosa, vinos). Oleorresinas de páprika y orégano. Productos cárnicos y lácteos, industria del papel, azúcar y colorantes. Industria metalúrgica, concentración, fundición y refinación de minerales no férreos. Industria del acero, hidrometalurgia, recubrimientos electroquímicos, sanidad y seguridad medioambiental (Tecnologías limpias, monitoreo, control y tratamientos de contaminante, sistema de seguridad industrial).', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_tutorias`
--

CREATE TABLE `datos_tutorias` (
  `id` int(11) NOT NULL,
  `texto` text NOT NULL,
  `link` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `datos_tutorias`
--

INSERT INTO `datos_tutorias` (`id`, `texto`, `link`) VALUES
(1, 'RESOLUCIÓN DE FACULTAD N°0000000', '');

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
-- Indices de la tabla `datos_autoridades`
--
ALTER TABLE `datos_autoridades`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `datos_comites`
--
ALTER TABLE `datos_comites`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `datos_historica`
--
ALTER TABLE `datos_historica`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `datos_horarios`
--
ALTER TABLE `datos_horarios`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `datos_malla`
--
ALTER TABLE `datos_malla`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `datos_misionvision`
--
ALTER TABLE `datos_misionvision`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `datos_objetivos`
--
ALTER TABLE `datos_objetivos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `datos_plan-estudios`
--
ALTER TABLE `datos_plan-estudios`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `datos_presentacion`
--
ALTER TABLE `datos_presentacion`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `datos_tutorias`
--
ALTER TABLE `datos_tutorias`
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
-- AUTO_INCREMENT de la tabla `datos_autoridades`
--
ALTER TABLE `datos_autoridades`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `datos_comites`
--
ALTER TABLE `datos_comites`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `datos_historica`
--
ALTER TABLE `datos_historica`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `datos_horarios`
--
ALTER TABLE `datos_horarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `datos_malla`
--
ALTER TABLE `datos_malla`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `datos_misionvision`
--
ALTER TABLE `datos_misionvision`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `datos_objetivos`
--
ALTER TABLE `datos_objetivos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `datos_plan-estudios`
--
ALTER TABLE `datos_plan-estudios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `datos_presentacion`
--
ALTER TABLE `datos_presentacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `datos_tutorias`
--
ALTER TABLE `datos_tutorias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `redes_sociales`
--
ALTER TABLE `redes_sociales`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;