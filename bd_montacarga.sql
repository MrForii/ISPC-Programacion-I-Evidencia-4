-- Creamos la base de datos

CREATE DATABASE db_montacarga;

-- Usamos la base de datos

USE montacarga;

-- Creamos la tabla que contendra todos los datos de los montacargas

CREATE TABLE Montacargas (
    id SERIAL PRIMARY KEY,
    pasillo INT,
    pasillo_actual INT,
    carga_actual INT,
    carga_maxima INT,
    encendido BOOL
);

-- Insertamos 10 montacargas en la tabla

INSERT INTO Montacargas (pasillo, pasillo_actual, carga_actual, carga_maxima, encendido) VALUES (20, 5, 65, 100, TRUE);
INSERT INTO Montacargas (pasillo, pasillo_actual, carga_actual, carga_maxima, encendido) VALUES (50, 7, 35, 90, FALSE);
INSERT INTO Montacargas (pasillo, pasillo_actual, carga_actual, carga_maxima, encendido) VALUES (30, 15, 5, 60, TRUE);
INSERT INTO Montacargas (pasillo, pasillo_actual, carga_actual, carga_maxima, encendido) VALUES (50, 34, 55, 70, TRUE);
INSERT INTO Montacargas (pasillo, pasillo_actual, carga_actual, carga_maxima, encendido) VALUES (20, 17, 105, 150, FALSE);
INSERT INTO Montacargas (pasillo, pasillo_actual, carga_actual, carga_maxima, encendido) VALUES (30, 3, 48, 80, FALSE);
INSERT INTO Montacargas (pasillo, pasillo_actual, carga_actual, carga_maxima, encendido) VALUES (20, 9, 29, 65, TRUE);
INSERT INTO Montacargas (pasillo, pasillo_actual, carga_actual, carga_maxima, encendido) VALUES (10, 6, 97, 140, FALSE);
INSERT INTO Montacargas (pasillo, pasillo_actual, carga_actual, carga_maxima, encendido) VALUES (45, 43, 75, 110, FALSE);
INSERT INTO Montacargas (pasillo, pasillo_actual, carga_actual, carga_maxima, encendido) VALUES (30, 13, 98, 100, TRUE);

-- Realizamos 5 consultas SELECT

SELECT * FROM Montacargas;

SELECT * FROM Montacargas WHERE carga_maxima > 100;

SELECT * FROM Montacargas ORDER BY carga_actual DESC;

SELECT * FROM Montacargas WHERE encendido = TRUE;

SELECT AVG(carga_actual) AS carga_actual_promedio FROM Montacargas;
