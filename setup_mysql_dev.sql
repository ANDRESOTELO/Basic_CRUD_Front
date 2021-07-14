CREATE DATABASE IF NOT EXISTS izeven_db;
CREATE USER IF NOT EXISTS 'izeven_dev'@'localhost' IDENTIFIED BY 'izeven_pwd';
GRANT ALL PRIVILEGES ON `izeven_db`.* TO 'izeven_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'izeven_dev'@'localhost';
FLUSH PRIVILEGES;