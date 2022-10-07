DROP TABLE IF EXISTS records;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  countnry VARCHAR(255)
);

CREATE TABLE records (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  artist_id INT NOT NULL REFERENCES artists(id),
  genre VARCHAR(255),
  year INT,
  buying_cost FLOAT,
  price FLOAT 
);
