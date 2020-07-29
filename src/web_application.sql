DROP DATABASE IF EXISTS `web_application`;
CREATE DATABASE `web_application` DEFAULT CHARACTER SET utf8;
USE `web_application`;

CREATE TABLE `Admins` (
  `id` INT AUTO_INCREMENT,
  `username` VARCHAR(254) UNIQUE NOT NULL,
  `password` TEXT NOT NULL,
  `token` CHAR(32) UNIQUE NOT NULL,
  `database_username` TEXT DEFAULT NULL,
  `database_password` TEXT DEFAULT NULL,
  PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8;
