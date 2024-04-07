#%%
from src import soporte as sp
#----
clientes = sp.leer_csv('files', 'clientes')
ventas = sp.leer_csv('files', 'ventas')
productos = sp.leer_csv('files', 'productos')
#----
sp.col_minuscula(clientes)
sp.col_minuscula(ventas)
sp.col_minuscula(productos)
#----
sp.explorar_duplicados(clientes)
sp.explorar_duplicados(ventas)
sp.explorar_duplicados(productos)
#----
sp.explorar_nulos(clientes)
sp.explorar_nulos(ventas)
sp.explorar_nulos(productos)
#----
sp.mostrar_tipos(clientes)
sp.mostrar_tipos(ventas)
sp.mostrar_tipos(productos)
#----
sp.valores_unicos(clientes, clientes.columns)
sp.valores_unicos(ventas, ventas.columns)
sp.valores_unicos(productos, productos.columns)
#----
sp.describir_columnas(clientes, clientes.columns)
sp.describir_columnas(ventas, ventas.columns)
sp.describir_columnas(productos, productos.columns)
#----
sp.rellenar_nulos(clientes, clientes.columns, 'desconocido')
sp.rellenar_nulos(productos, productos.columns, 'desconocido')
#----
sp.guardado(clientes, 'clientes')
sp.guardado(ventas, 'ventas')
sp.guardado(productos, 'productos')