DROP DATABASE microBlogDB;

CREATE DATABASE IF NOT EXISTS microBlogDB;
GRANT ALL PRIVILEGES ON microBlogDB.* to 'blogUser'@'localhost' 
identified by 'blogPassword';
USE microBlogDB;

CREATE TABLE posts
(
  name VARCHAR(25),
  entry VARCHAR(144)
);
  
INSERT INTO posts VALUES ('Ann', "Sparky, Call me!");
INSERT INTO posts VALUES ('De Lune', "I am not a morning person");
INSERT INTO posts VALUES ('Ann', "Sparky, PLEASE Call me!");
INSERT INTO posts VALUES ('Jerome', "Anyone interested should see me.");

