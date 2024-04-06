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
                    `id_cliente` INT NOT NULL,
                    `id_producto` INT NOT NULL,
                    `fecha_venta` DATE,
                    `cantidad` INT,
                    `total` FLOAT,
                   FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_Cliente),
                   FOREIGN KEY (ID_Producto) REFERENCES Productos(ID_Producto);
                    """
insertar_ventas = "INSERT INTO ventas (id_cliente, id_producto, fecha_venta, cantidad, total ) VALUES (%s, %s, %s, %s, %s)"





CONSTRAINT fk_cliente FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_Cliente),
            CONSTRAINT fk_producto FOREIGN KEY (ID_Producto) REFERENCES Productos(ID_Producto)