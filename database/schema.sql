CREATE DATABASE library;

CREATE TABLE authors(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL
);

CREATE TABLE books(
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  publisher TEXT NOT NULL,
  year INT NOT NULL,
  author_id INT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES authors(id)
);