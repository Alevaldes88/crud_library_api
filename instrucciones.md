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

# Crear una tabla llamada users

CREATE TABLE `library`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  `surname` VARCHAR(50) NOT NULL,
  `age` INT NOT NULL,
  `mail` VARCHAR(100) NOT NULL,
  `register_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `status` TINYINT NOT NULL DEFAULT 1,
  `password` VARCHAR(255) NOT NULL,
  `rol` ENUM('admin', 'user') NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `mail_UNIQUE` (`mail` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;

