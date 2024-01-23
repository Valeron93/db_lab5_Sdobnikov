CREATE TABLE Authors
(
  author_id SERIAL NOT NULL,
  author_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (author_id),
  UNIQUE (author_name)
);

CREATE TABLE Genres
(
  genre_id SERIAL NOT NULL,
  genre_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (genre_id)
);

CREATE TABLE Poems
(
  poem_id SERIAL NOT NULL,
  poem_name VARCHAR(255) NOT NULL,
  genre_id INT NOT NULL,
  PRIMARY KEY (poem_id),
  FOREIGN KEY (genre_id) REFERENCES Genres(genre_id)
);

CREATE TABLE PoemsAuthors
(
  authors_id SERIAL NOT NULL,
  author_id INT NOT NULL,
  poem_id INT NOT NULL,
  PRIMARY KEY (authors_id),
  FOREIGN KEY (author_id) REFERENCES Authors(author_id),
  FOREIGN KEY (poem_id) REFERENCES Poems(poem_id)
);