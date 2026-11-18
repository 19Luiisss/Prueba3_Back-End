DROP DATABASE IF EXISTS sportvault_db;
CREATE DATABASE sportvault_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE sportvault_db;
SELECT COUNT(*) FROM catalogo_categoria;
SELECT COUNT(*) FROM catalogo_articulo;

SELECT a.id, a.nombre, c.nombre AS categoria 
FROM catalogo_articulo a 
INNER JOIN catalogo_categoria c ON a.categoria_id = c.id;