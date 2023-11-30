-- list table 
CREATE TABLE IF NOT EXISTS second_table (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(256) NOT NULL,
  score INT NOT NULL
);
INSERT INTO second_table (name, score) VALUES ('John', 10);
INSERT INTO second_table (name, score) VALUES ('Alex', 3);
INSERT INTO second_table (name, score) VALUES ('Bob', 14);
INSERT INTO second_table (name, score) VALUES ('George', 8);

