sudo apt update
sudo apt install mysql-server

sudo mysql <<EOF
DROP USER IF EXISTS 'hlcrud'@'localhost';
CREATE USER 'hlcrud'@'localhost' IDENTIFIED BY 'hlcrud2020';
GRANT ALL PRIVILEGES ON * . * TO 'hlcrud'@'localhost';
FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS hl;
USE hl;

DROP TABLE IF EXISTS data;
CREATE TABLE data (
  BoardSN double DEFAULT NULL,
  CompName text,
  Type text,
  cModel text,
  DLinference_result text,
  directory text,
  ConfirmDefect text,
  MachineDefect text,
  Status text,
  image_name text,
  LightingCondition text,
  image_scantime text,
  BoardRESULT text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
EOF

pip3 install -r requirements.txt