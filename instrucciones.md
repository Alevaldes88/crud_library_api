# Crear una bbdd MySQL llamada library y una tabla llamada books

CREATE TABLE `library`.`books` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NOT NULL,
  `author` VARCHAR(255) NOT NULL,
  `isbn` VARCHAR(25) NOT NULL UNIQUE,
  `year` INT NOT NULL,
  `publisher` VARCHAR(255) NOT NULL,
  `genre` VARCHAR(100) NOT NULL,
  `language` VARCHAR(50) NOT NULL,
  `status` TINYINT NOT NULL DEFAULT 1,
  `pages` INT NOT NULL,
  PRIMARY KEY (`id`)
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;
