-- ---
-- Globals
-- ---

-- SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
-- SET FOREIGN_KEY_CHECKS=0;

-- ---
-- Table 'users'
--
-- ---

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `login` VARCHAR(255) NULL DEFAULT NULL,
  `password` VARCHAR(32) NULL DEFAULT NULL,
  UNIQUE KEY (`id`)
);

-- ---
-- Table 'tasks'
--
-- ---

DROP TABLE IF EXISTS `tasks`;

CREATE TABLE `tasks` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `user_id` INTEGER NULL DEFAULT NULL,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `parent_id` INTEGER(11) NULL DEFAULT NULL,
  `deadline` DATE NULL DEFAULT NULL,
  `progress` INTEGER(1) NULL DEFAULT NULL,
  `description` MEDIUMTEXT NULL DEFAULT NULL,
  `priority` INTEGER NULL DEFAULT 3,
  PRIMARY KEY (`id`)
);

-- ---
-- Table 'sessions'
--
-- ---

DROP TABLE IF EXISTS `sessions`;

CREATE TABLE `sessions` (
  `id` INTEGER NOT NULL AUTO_INCREMENT,
  `token` VARCHAR(255) NULL DEFAULT NULL,
  `user_id` INTEGER NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
);

-- ---
-- Foreign Keys
-- ---

ALTER TABLE `tasks` ADD FOREIGN KEY (user_id) REFERENCES `users` (`id`);
ALTER TABLE `sessions` ADD FOREIGN KEY (user_id) REFERENCES `users` (`id`);

-- ---
-- Table Properties
-- ---

-- ALTER TABLE `users` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `tasks` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `sessions` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ---
-- Test Data
-- ---

-- INSERT INTO `users` (`id`,`login`,`password`) VALUES
-- ('','','');
-- INSERT INTO `tasks` (`id`,`user_id`,`name`,`parent_id`,`deadline`,`progress`,`description`,`priority`) VALUES
-- ('','','','','','','','');
-- INSERT INTO `sessions` (`id`,`token`,`user_id`) VALUES
-- ('','','');
