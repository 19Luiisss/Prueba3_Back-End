DROP DATABASE IF EXISTS tienda_futbol;
CREATE DATABASE tienda_futbol CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE tienda_futbol;
SELECT COUNT(*) FROM catalogo_categoria;
SELECT COUNT(*) FROM catalogo_articulo;