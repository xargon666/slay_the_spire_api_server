DROP TABLE IF EXISTS relics;

CREATE TABLE relics (
    id serial PRIMARY KEY,
    name varchar(100) UNIQUE,
    rarity varchar(100),
    class-specific varchar(100),
    description varchar(250),
    flavor-text varchar(100),
    conditions-for-spawning varchar(100)
