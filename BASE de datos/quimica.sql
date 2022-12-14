-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-01-2023 a las 06:11:23
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.1.12

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_autoridades`
--

INSERT INTO `datos_autoridades` (`id`, `cargo`, `nombre`) VALUES
(1, 'DECANO DE LA FACULTAD DE INGENIERÍA', 'Dr. Jesús Plácido Medina Salas'),
(3, 'autoridad 2', 'nombre'),
(4, 'autoridad 3', 'nombre'),
(5, 'autoridad 4', 'nombre');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_comites`
--

CREATE TABLE `datos_comites` (
  `id` int(11) NOT NULL,
  `link` text NOT NULL,
  `texto_boton` text NOT NULL DEFAULT 'Resolución'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_comites`
--

INSERT INTO `datos_comites` (`id`, `link`, `texto_boton`) VALUES
(1, 'https://drive.google.com/file/d/1sJQMym_iECMRvqIQRHqdkwJJdIM6XG3Q/view', 'Resolución');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_estudiantes-egresados`
--

CREATE TABLE `datos_estudiantes-egresados` (
  `id` int(11) NOT NULL,
  `año` int(11) NOT NULL,
  `matriculados` int(11) NOT NULL,
  `egresados` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_estudiantes-egresados`
--

INSERT INTO `datos_estudiantes-egresados` (`id`, `año`, `matriculados`, `egresados`) VALUES
(1, 2023, 500, 24),
(2, 2022, 450, 30);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_faq`
--

CREATE TABLE `datos_faq` (
  `id` int(11) NOT NULL,
  `texto` text NOT NULL,
  `link` text NOT NULL,
  `texto_boton` text NOT NULL DEFAULT 'Ver',
  `titulo_pregunta` text NOT NULL DEFAULT 'Pregunta'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_faq`
--

INSERT INTO `datos_faq` (`id`, `texto`, `link`, `texto_boton`, `titulo_pregunta`) VALUES
(1, 'sin boton', '', 'Ver', 'Pregunta 1'),
(2, '', 'index', 'Ver', 'Pregunta 2'),
(3, 'con boton y text', 'index', 'Ver', 'Pregunta 3');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_historica`
--

CREATE TABLE `datos_historica` (
  `id` int(11) NOT NULL,
  `texto` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_historica`
--

INSERT INTO `datos_historica` (`id`, `texto`) VALUES
(1, 'Texto de ejemplo\r\nTexto de ejemplo\r\nTexto de ejemplo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_horarios`
--

CREATE TABLE `datos_horarios` (
  `id` int(11) NOT NULL,
  `texto_boton` text NOT NULL,
  `link` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_horarios`
--

INSERT INTO `datos_horarios` (`id`, `texto_boton`, `link`) VALUES
(1, 'https://www.facebook.com/ESIQUNJBG/posts/pfbid02H5BopF7eXodVCkd1KyvhzaGwPE8SRQwHecGJHZ4ZXjgdpdpKnHX6afSoxoTMFYCul', 'Horario');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_index`
--

CREATE TABLE `datos_index` (
  `id` int(11) NOT NULL,
  `foto` varchar(5000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_index`
--

INSERT INTO `datos_index` (`id`, `foto`) VALUES
(1, 'El Ingeniero Químico, tendrá una formación Integral en el campo científico y tecnológico; será capaz de comprender, incorporar, y enriquecer las denominadas tecnologías emergentes y de adaptarse a los campos tecnológicos.\r\nEstará capacitado para: planear, dimensionar, diseñar y simular plantas de procesos; formular, ejecutar y evaluar proyectos industriales; supervisar, administrar y controlar procesos industriales; investigar y desarrollar nuevos procesos; adecuar, modificar y optimizar los existentes; planificar, constituir y gerenciar empresas.'),
(10, '2022154754d41ae5b0-aa4b-4fd1-b53b-f7b1b155df771.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_lineas-inv`
--

CREATE TABLE `datos_lineas-inv` (
  `id` int(11) NOT NULL,
  `titulo` text NOT NULL,
  `texto` text NOT NULL,
  `link` text NOT NULL,
  `texto_boton` text NOT NULL DEFAULT 'Ver'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_lineas-inv`
--

INSERT INTO `datos_lineas-inv` (`id`, `titulo`, `texto`, `link`, `texto_boton`) VALUES
(1, 'título 1', 'descripción', '', 'Resolución'),
(2, 'titulo 2', '', '', 'Ver');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_malla`
--

CREATE TABLE `datos_malla` (
  `id` int(11) NOT NULL,
  `texto` text NOT NULL,
  `link` text NOT NULL,
  `texto_boton` text NOT NULL,
  `imagen` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_malla`
--

INSERT INTO `datos_malla` (`id`, `texto`, `link`, `texto_boton`, `imagen`) VALUES
(1, 'MALLA CURRICULAR DE LA E.P. DE INGENIERÍA QUÍMICA 2018', '', 'Malla Curricular', '20231830082022180446d41ae5b0-aa4b-4fd1-b53b-f7b1b155df771.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_misionvision`
--

CREATE TABLE `datos_misionvision` (
  `id` int(11) NOT NULL,
  `mision_vision` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
  `imagen` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_objetivos`
--

INSERT INTO `datos_objetivos` (`id`, `texto`, `imagen`) VALUES
(1, '- Objetivo 1\r\n- Objetivo 2\r\n- Objetivo 3', '2022181107d41ae5b0-aa4b-4fd1-b53b-f7b1b155df771.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_organizacion`
--

CREATE TABLE `datos_organizacion` (
  `id` int(11) NOT NULL,
  `texto` text NOT NULL,
  `imagen` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_organizacion`
--

INSERT INTO `datos_organizacion` (`id`, `texto`, `imagen`) VALUES
(1, 'Organigrama de la Escuela Profesional de Ingeniería Química', '20232328272023232548parallax1.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_personal-administrativo`
--

CREATE TABLE `datos_personal-administrativo` (
  `id` int(11) NOT NULL,
  `cargo` text NOT NULL DEFAULT 'Personal',
  `nombre` text NOT NULL DEFAULT 'Nombre Personal',
  `correo` text NOT NULL DEFAULT '@unjbg.edu.pe'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_personal-administrativo`
--

INSERT INTO `datos_personal-administrativo` (`id`, `cargo`, `nombre`, `correo`) VALUES
(1, 'Personal 1', 'Nombre Personal 1', '@unjbg.edu.pe'),
(2, 'Personal 2', 'Nombre Personal 2', '@unjbg.edu.pe 2');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_personal-docente`
--

CREATE TABLE `datos_personal-docente` (
  `id` int(11) NOT NULL,
  `link` text NOT NULL,
  `texto_boton` text NOT NULL DEFAULT 'Periodo 20XX-I'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_personal-docente`
--

INSERT INTO `datos_personal-docente` (`id`, `link`, `texto_boton`) VALUES
(1, '', 'Periodo 2022-II'),
(2, '', 'Periodo 2023-I');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_plan-estudios`
--

CREATE TABLE `datos_plan-estudios` (
  `id` int(11) NOT NULL,
  `link` text NOT NULL,
  `texto_boton` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_plan-estudios`
--

INSERT INTO `datos_plan-estudios` (`id`, `link`, `texto_boton`) VALUES
(1, '', 'Plan de estudios F1-2014'),
(2, '', 'Plan de estudios F2-2018');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_planes`
--

CREATE TABLE `datos_planes` (
  `id` int(11) NOT NULL,
  `titulo` text NOT NULL DEFAULT 'Plan',
  `link` text NOT NULL,
  `texto_boton` text NOT NULL DEFAULT 'Ver Plan'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_planes`
--

INSERT INTO `datos_planes` (`id`, `titulo`, `link`, `texto_boton`) VALUES
(1, 'Plan 1', '', 'Ver Plan'),
(2, 'Plan 2', '', 'Ver Plan');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_postulantes-ingresantes`
--

CREATE TABLE `datos_postulantes-ingresantes` (
  `id` int(11) NOT NULL,
  `año` int(11) NOT NULL,
  `postulantes_ingresantes` tinyint(1) NOT NULL DEFAULT 0,
  `CEPU_I` int(11) NOT NULL,
  `CEPU_II` int(11) NOT NULL,
  `CEPU_III` int(11) NOT NULL,
  `FASE_I` int(11) NOT NULL,
  `FASE_II` int(11) NOT NULL,
  `COLEGIOS` int(11) NOT NULL,
  `TRASLADO_EXTERNO` int(11) NOT NULL,
  `TRASLADO_INTERNO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_postulantes-ingresantes`
--

INSERT INTO `datos_postulantes-ingresantes` (`id`, `año`, `postulantes_ingresantes`, `CEPU_I`, `CEPU_II`, `CEPU_III`, `FASE_I`, `FASE_II`, `COLEGIOS`, `TRASLADO_EXTERNO`, `TRASLADO_INTERNO`) VALUES
(1, 2022, 0, 489, 490, 491, 100, 101, 102, 5, 5),
(2, 2022, 1, 5, 6, 7, 8, 9, 10, 1, 2),
(3, 2023, 0, 300, 301, 302, 303, 304, 45, 6, 7);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_presentacion`
--

CREATE TABLE `datos_presentacion` (
  `id` int(11) NOT NULL,
  `texto` text NOT NULL,
  `imagen1` text NOT NULL,
  `imagen2` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_presentacion`
--

INSERT INTO `datos_presentacion` (`id`, `texto`, `imagen1`, `imagen2`) VALUES
(1, 'DURACIÓN, GRADOS Y TÍTULOS\r\n\r\nTiene una duración de 5 años.\r\nGrado Académico de Bachiller en Ciencias con mención en Ingeniería Química.\r\nTítulo Profesional de Ingeniero Químico.\r\n\r\nCAMPO OCUPACIONAL\r\n\r\nComprende el amplio sector industrial: Refinación de Petróleo y gas natural, polímeros naturales y sintéticos, cemento cerámica y vidrio. Pinturas, lacas barnices y resinas.\r\nFertilizantes y explosivos. Industria no metálica (refractarios, mayólica). Industria textil, industria biotecnológica, (fármacos, proteínas y enzimas) Industria de bebidas (cerveza, gaseosa, vinos). Oleorresinas de páprika y orégano. Productos cárnicos y lácteos, industria del papel, azúcar y colorantes. Industria metalúrgica, concentración, fundición y refinación de minerales no férreos. Industria del acero, hidrometalurgia, recubrimientos electroquímicos, sanidad y seguridad medioambiental (Tecnologías limpias, monitoreo, control y tratamientos de contaminante, sistema de seguridad industrial).', '2022172843banner1.jpg', '2022172909logo-sm.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_protocolos`
--

CREATE TABLE `datos_protocolos` (
  `id` int(11) NOT NULL,
  `titulo` text NOT NULL DEFAULT 'Protocolo',
  `link` text NOT NULL,
  `texto_boton` text NOT NULL DEFAULT 'Ver'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_protocolos`
--

INSERT INTO `datos_protocolos` (`id`, `titulo`, `link`, `texto_boton`) VALUES
(1, 'Protocolo 1', '', 'Ver Protocolo '),
(2, 'Protocolo 2', '', 'Ver Protocolo ');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_proyectos-inv`
--

CREATE TABLE `datos_proyectos-inv` (
  `id` int(11) NOT NULL,
  `titulo` text NOT NULL,
  `link` text NOT NULL,
  `texto_boton` text NOT NULL DEFAULT 'Ver Proyecto'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_proyectos-inv`
--

INSERT INTO `datos_proyectos-inv` (`id`, `titulo`, `link`, `texto_boton`) VALUES
(1, 'Proyecto 1', '', 'Ver Proyecto'),
(2, 'Proyecto 2', '', 'Ver Proyecto');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_reglamento`
--

CREATE TABLE `datos_reglamento` (
  `id` int(11) NOT NULL,
  `link` text NOT NULL,
  `texto_boton` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_reglamento`
--

INSERT INTO `datos_reglamento` (`id`, `link`, `texto_boton`) VALUES
(1, 'http://unjbg.edu.pe/transparenciainst/reglamentoacademico.php', 'Reglamento Académico');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_repositorio-tesis`
--

CREATE TABLE `datos_repositorio-tesis` (
  `id` int(11) NOT NULL,
  `link` text NOT NULL,
  `texto_boton` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_repositorio-tesis`
--

INSERT INTO `datos_repositorio-tesis` (`id`, `link`, `texto_boton`) VALUES
(1, 'http://repositorio.unjbg.edu.pe/handle/UNJBG/814', 'Repositorio de Tesis');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_seguridad`
--

CREATE TABLE `datos_seguridad` (
  `id` int(11) NOT NULL,
  `titulo` text NOT NULL DEFAULT 'Reglamento',
  `link` text NOT NULL,
  `texto_boton` text NOT NULL DEFAULT 'Ver'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_seguridad`
--

INSERT INTO `datos_seguridad` (`id`, `titulo`, `link`, `texto_boton`) VALUES
(1, 'Reglamento 1', '', 'Ver'),
(2, 'Reglamento 2', '', 'Ver');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_tramites`
--

CREATE TABLE `datos_tramites` (
  `id` int(11) NOT NULL,
  `link` text NOT NULL,
  `boton_texto` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_tramites`
--

INSERT INTO `datos_tramites` (`id`, `link`, `boton_texto`) VALUES
(1, 'TEXTO PRUEBA', ''),
(2, '', 'Boton 1');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_tutorias`
--

CREATE TABLE `datos_tutorias` (
  `id` int(11) NOT NULL,
  `texto_boton` text NOT NULL,
  `link` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_tutorias`
--

INSERT INTO `datos_tutorias` (`id`, `texto_boton`, `link`) VALUES
(1, 'RESOLUCIÓN DE FACULTAD N°0000001', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `redes_sociales`
--

CREATE TABLE `redes_sociales` (
  `id` int(11) NOT NULL,
  `nombre_red` varchar(20) NOT NULL,
  `link` varchar(80) NOT NULL,
  `icono_bootstrap` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `redes_sociales`
--

INSERT INTO `redes_sociales` (`id`, `nombre_red`, `link`, `icono_bootstrap`) VALUES
(1, 'Facebook', 'https://es-la.facebook.com/ESIQUNJBG/', 'facebook-f');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` char(102) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `username`, `password`) VALUES
(1, 'admin', 'pbkdf2:sha256:260000$YLoK7eglLcpfp9I6$9f7badf5482358cac756a9633e95fe83396a1431da8c3cdc195be4a01a2e190a');

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
-- Indices de la tabla `datos_estudiantes-egresados`
--
ALTER TABLE `datos_estudiantes-egresados`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `datos_faq`
--
ALTER TABLE `datos_faq`
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
-- Indices de la tabla `datos_index`
--
ALTER TABLE `datos_index`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `datos_lineas-inv`
--
ALTER TABLE `datos_lineas-inv`
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
-- Indices de la tabla `datos_organizacion`
--
ALTER TABLE `datos_organizacion`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `datos_personal-administrativo`
--
ALTER TABLE `datos_personal-administrativo`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `datos_personal-docente`
--
ALTER TABLE `datos_personal-docente`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `datos_plan-estudios`
--
ALTER TABLE `datos_plan-estudios`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `datos_planes`
--
ALTER TABLE `datos_planes`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `datos_postulantes-ingresantes`
--
ALTER TABLE `datos_postulantes-ingresantes`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `datos_presentacion`
--
ALTER TABLE `datos_presentacion`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `datos_protocolos`
--
ALTER TABLE `datos_protocolos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `datos_proyectos-inv`
--
ALTER TABLE `datos_proyectos-inv`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `datos_reglamento`
--
ALTER TABLE `datos_reglamento`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `datos_repositorio-tesis`
--
ALTER TABLE `datos_repositorio-tesis`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `datos_seguridad`
--
ALTER TABLE `datos_seguridad`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `datos_tramites`
--
ALTER TABLE `datos_tramites`
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
-- Indices de la tabla `user`
--
ALTER TABLE `user`
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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `datos_comites`
--
ALTER TABLE `datos_comites`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `datos_estudiantes-egresados`
--
ALTER TABLE `datos_estudiantes-egresados`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `datos_faq`
--
ALTER TABLE `datos_faq`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

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
-- AUTO_INCREMENT de la tabla `datos_index`
--
ALTER TABLE `datos_index`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `datos_lineas-inv`
--
ALTER TABLE `datos_lineas-inv`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `datos_organizacion`
--
ALTER TABLE `datos_organizacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `datos_personal-administrativo`
--
ALTER TABLE `datos_personal-administrativo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `datos_personal-docente`
--
ALTER TABLE `datos_personal-docente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `datos_plan-estudios`
--
ALTER TABLE `datos_plan-estudios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `datos_planes`
--
ALTER TABLE `datos_planes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `datos_postulantes-ingresantes`
--
ALTER TABLE `datos_postulantes-ingresantes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `datos_presentacion`
--
ALTER TABLE `datos_presentacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `datos_protocolos`
--
ALTER TABLE `datos_protocolos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `datos_proyectos-inv`
--
ALTER TABLE `datos_proyectos-inv`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `datos_reglamento`
--
ALTER TABLE `datos_reglamento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `datos_repositorio-tesis`
--
ALTER TABLE `datos_repositorio-tesis`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `datos_seguridad`
--
ALTER TABLE `datos_seguridad`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `datos_tramites`
--
ALTER TABLE `datos_tramites`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `datos_tutorias`
--
ALTER TABLE `datos_tutorias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `redes_sociales`
--
ALTER TABLE `redes_sociales`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
