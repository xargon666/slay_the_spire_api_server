DROP TABLE IF EXISTS relics;

CREATE TABLE relics (
    id serial PRIMARY KEY,
    name varchar(100) UNIQUE,
    rarity varchar(100),
    class_specific varchar(100),
    description varchar(250),
    flavor_text varchar(250),
    conditions_for_spawning varchar(100)
    );
