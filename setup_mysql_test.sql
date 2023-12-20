-- Mysql server for testing should be prepared in the same way, but with different user and database names.

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS `hbnb_test`@`localhost` IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO `hbnb_test`@`localhost`;
GRANT SELECT ON `performance_schema`.* TO `hbnb_test`@`localhost`;
FLUSH PRIVILEGES;
