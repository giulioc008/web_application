CREATE DATABASE IF NOT EXISTS `web_application` DEFAULT CHARACTER SET utf8;
USE `web_application`;

DROP TABLE IF EXISTS `Admins`;
CREATE TABLE IF NOT EXISTS `Admins` (
  `id` INT AUTO_INCREMENT,
  `username` VARCHAR(254) UNIQUE NOT NULL,
  `password` TEXT NOT NULL,
  `token` CHAR(32) UNIQUE NOT NULL,
  `database_username` TEXT DEFAULT NULL,
  `database_password` TEXT DEFAULT NULL,
  PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8;

INSERT INTO `Admins` (`username`, `password`, `token`, `database_username`, `database_password`) VALUES
('giuliocoa', 'pbkdf2:sha256:150000$GIb7152M$825a89385e9340972c503e20a0e787b859c4cf070327072fc6ba398336fdbef0', 'c24027b9ce670ecbfbf24a940668901f', 'giuliocoa', 'ivo.c@tiscali.it'),
('phpmyadmin', 'pbkdf2:sha256:150000$GIb7152M$825a89385e9340972c503e20a0e787b859c4cf070327072fc6ba398336fdbef0', '12bdca10be958e2b6e512de889beb5c9', 'phpmyadmin', 'ivo.c@tiscali.it'),
('root', 'pbkdf2:sha256:150000$GIb7152M$825a89385e9340972c503e20a0e787b859c4cf070327072fc6ba398336fdbef0', '773dba161c9c4da890e44eff7cefffd6', 'root', 'ivo.c@tiscali.it');
