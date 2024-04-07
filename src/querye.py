query_bbdd = "CREATE SCHEMA IF NOT EXISTS `nuestra_tienda`;"

crear_tabla_clientes = """
                    CREATE TABLE IF NOT EXISTS `nuestra_tienda`.`clientes` (
                    `id` VARCHAR(100) INT NOT NULL,
                    `first_name` VARCHAR(100) NOT NULL,
                    `last_name` VARCHAR(100) NOT NULL,
                    `email` VARCHAR(100) NOT NULL,
                    `gender` VARCHAR(100),
                    `city` VARCHAR(100),
                    `country` VARCHAR(100),
                    `address` VARCHAR(100) 
                    PRIMARY KEY (`id`));
                    """
insertar_clientes = "INSERT INTO clientes (id, first_name, last_name, email, gender, city, country, address  ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

crear_tabla_ventas = """
                    CREATE TABLE IF NOT EXISTS `nuestra_tienda`.`ventas` (
                    `id_cliente` VARCHAR(100) INT NOT NULL,
                    `id_producto` VARCHAR(100) INT NOT NULL,
                    `fecha_venta` VARCHAR(100) DATE,
                    `cantidad`VARCHAR(100) INT,
                    `total` VARCHAR(100) FLOAT,
                   FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_Cliente),
                   FOREIGN KEY (ID_Producto) REFERENCES Productos(ID_Producto);
                    """
insertar_ventas = "INSERT INTO ventas (id_cliente, id_producto, fecha_venta, cantidad, total ) VALUES (%s, %s, %s, %s, %s)"

crear_tabla_productos = """
                    CREATE TABLE IF NOT EXISTS `nuestra_tienda`.`productos` (
                    `ID` VARCHAR(100) INT NOT NULL,
                    `Nombre_Producto` VARCHAR(100) INT NOT NULL,
                    `Categoría` VARCHAR(100),
                    `Precio` VARCHAR(100) FLOAT,
                    `Origen` VARCHAR(100),
                    `Descripción` VARCHAR(100); 
                    """ 
insertar_productos = "INSERT INTO productos ( ID, Nombre_Producto, Categoría, Precio, Origen, Descripción) VALUES (%s, %s, %s, %s, %s, %s)"


