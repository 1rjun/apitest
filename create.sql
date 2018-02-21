CREATE TABLE GEO_DATA(
    id VARCHAR PRIMARY KEY,
    place_name VARCHAR NOT NULL,
    admin_name VARCHAR NOT NULL,
    latitude DOUBLE PRECISION ,
    longitude DOUBLE PRECISION ,
    accuracy INTEGER 
);