# LIBRERÍAS NECESARIAS

# Tratamiento de datos
import pandas as pd
import numpy as np
import re


def apertura(ruta):
    
    """
    Esta función carga un archivo CSV ubicado en la ruta especificada 

    Parámetros:
    ruta (str): La ruta del archivo CSV a cargar.

    Devoluciones:
    DataFrame: El DataFrame cargado desde el archivo CSV.

    Esta función carga el archivo CSV especificado en 'ruta', elimina la columna 'Unnamed: 0' si existe
    """
    
    df = pd.read_csv(ruta)

    # Si al cargar el dataframe se creó una columna de unnamed, la elimina
    if 'Unnamed: 0' in df.columns:
        df.drop('Unnamed: 0', axis = 1, inplace=True)

def leer_csv(carpeta, nombre_archivo):
    '''
    Abre y lee los documentos CSV. 
        Si el archivo se encuentra, lo abre en un DataFrame de pandas y lo devuelve. 
        Si el archivo no se encuentra, la función imprime un mensaje indicando que el archivo no se encontró y devuelve None.
    
    Esta función toma el nombre de una carpeta y el nombre de archivo como entrada y lee el archivo CSV.
    
    Args:
        carpeta (str): El nombre de la carpeta donde se encuentra el archivo.
        nombre_archivo (str): El nombre del archivo csv sin la extensión.
        

    Returns:
        pd.DataFrame: Un DataFrame que contiene los datos del archivo csv, o None si el archivo no se encuentra.
    '''
    try:
        df = pd.read_csv(f'{carpeta}/{nombre_archivo}.csv', error_bad_lines=False, warn_bad_lines=False)
        return df
    except FileNotFoundError:
        print('No se ha encontrado el archivo')
        return None
    
def col_minuscula(dataframe):
    '''
    Pone en minúscula los nombres de las columnas del DataFrame.
    Esta función toma un DataFrame y cambia todos los nombres de las columnas y los pone en minúscula.

    Args:
        df (pd.DataFrame): El DataFrame que se desea modificar.

    Returns:
        None: La función modifica el DataFrame directamente cambiando el formato de sus nombres de columnas.
    '''
    print("Nombres de las columnas antes del cambio:")
    print(dataframe.columns)

    dataframe.columns = dataframe.columns.str.lower()

    print("----")
    print("\nNombres de las columnas después del cambio:")
    print(dataframe.columns)

def mostrar_tipos(dataframe):
    """
    Muestra el dtype de cada columna de un DataFrame.
    
    Args:
        dataframe (pandas.DataFrame): El DataFrame del que se mostrarán los dtypes de las columnas.
    """
    for columna in dataframe.columns:
        print(f"Columna '{columna}': {dataframe[columna].dtype}")

def valores_unicos(dataframe, columnas):
    '''
    Muestra los valores únicos de las columnas numéricas de un DataFrame.

    Args:
        dataframe (pd.DataFrame): El DataFrame del que se mostrarán los valores únicos.
        columnas (str o list): Un string o lista de strings que contiene los nombres de las columnas numéricas.

    Returns:
        None: La función imprime los valores únicos para cada columna numérica.
    '''
    for col in columnas:
        print(f"La columna {col.upper()} tiene los siguientes valores únicos:")
        display(pd.DataFrame(dataframe[col].value_counts()).head())
        print("----")

def describir_columnas(dataframe, columnas):
    '''
    Muestra las estadísticas descriptivas de las columnas especificadas de un DataFrame.

    Args:
        dataframe (pd.DataFrame): El DataFrame del que se mostrarán las estadísticas descriptivas.
        columnas (str o list): Un string o lista de strings que contiene los nombres de las columnas.

    Returns:
        None: La función imprime las estadísticas descriptivas para cada columna especificada.
    '''
    for col in columnas:
        print(f"Descripción de la columna {col.upper()}:")
        display(dataframe[[col]].describe().T)
        print("\n ----- \n")

def explorar_duplicados(dataframe):
    """
    Esta función muestra la cantidad de duplicados en el conjunto de datos.

    Args:
        dataframe (pandas.DataFrame): El DataFrame que se va a explorar en busca de duplicados.

    Returns:
        None
    """
    print(f"Tenemos {dataframe.duplicated().sum()} duplicados en el conjunto de datos.")

def eliminar_duplicados(dataframe):
    """
    Elimina los duplicados de un DataFrame.

    Args:
        df (pd.DataFrame): DataFrame de pandas.

    Returns:
        None
    """

    print(f"Antes de realizar la eliminación tenemos {dataframe.shape[0]} filas.")
    dataframe.drop_duplicates(inplace=True)
    print(f"Después de la eliminación de duplicados tenemos {dataframe.duplicated().sum()} duplicados en el conjunto de datos.")
    print(f"Después de realizar la eliminación tenemos {dataframe.shape[0]} filas.")

def explorar_nulos(dataframe):
    """
    Esta función presenta un DataFrame que contiene el porcentaje de valores nulos para cada columna.

    Args:
        dataframe (pandas.DataFrame): El DataFrame que se va a explorar en busca de valores nulos.

    Returns: 
        None
    """
    # Nos muestra un DataFrame para los valores nulos
    print("Los nulos que tenemos en el conjunto de datos son:")
    df_nulos = pd.DataFrame(dataframe.isnull().sum() / dataframe.shape[0] * 100, columns=["%_nulos"])
    display(df_nulos[df_nulos["%_nulos"] > 0])

def rellenar_nulos(dataframe, columnas, valor):
    '''
    Rellena los valores nulos en las columnas especificadas de un DataFrame con un valor específico.

    Args:
        dataframe (pd.DataFrame): El DataFrame en el que se van a rellenar los valores nulos.
        columnas (str o list): Un string o lista de strings que contiene los nombres de las columnas en las que se van a rellenar los valores nulos.
        valor (int, float, str, etc.): El valor con el que se van a rellenar los valores nulos.

    Returns:
        None: La función modifica el DataFrame original inplace.
    '''
    dataframe[columnas] = dataframe[columnas].fillna(valor)
    print(f"El total de nulos en las columnas {columnas} después de aplicar .fillna() es: {dataframe[columnas].isna().sum()}")


def guardado(dataframe, nombre):
    """ para guardar los dataframe a formato csv"""

    try:
        dataframe.to_csv(f'files/{nombre}_limpio.csv')
        print('El dataframe ha sido guardado con éxito.')
    except Exception as e:
        print(f'Error en el guardado: {e}')

def creacion_bbdd_tablas(query, contraseña, nombre_bbdd=None):
    """
    Crea una conexión a la base de datos MySQL y ejecuta una consulta para crear una tabla.
    Args:
    - query (str): Consulta SQL para crear la tabla en la base de datos.
    - contraseña (str): Contraseña para acceder a la base de datos.
    - nombre_bbdd (str): Nombre de la base de datos a la que se conectará.
    Returns:
        - None
    """
    if nombre_bbdd is not None:
        cnx = mysql.connector.connect(
            user="root",
            password=contraseña,
            host="127.0.0.1"
        )
        mycursor = cnx.cursor()
        try:
            mycursor.execute(query)
            print(mycursor)
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
    else:
        cnx = mysql.connector.connect(
            user="root",
            password=contraseña,
            host="127.0.0.1",
            database=nombre_bbdd
        )
        mycursor = cnx.cursor()
        try:
            mycursor.execute(query)
            print(mycursor)
            cnx.close()
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
            cnx.close()

def convertir_float(lista_tuplas):
    """
    Convierte los elementos de una lista de tuplas a float cuando sea posible.
    Args:
    - lista_tuplas (list): Una lista que contiene tuplas con elementos que pueden ser convertidos a float.
    Returns:
    - list: Una nueva lista con las mismas tuplas de entrada, pero con los elementos convertidos a float si es posible.
    """
    datos_tabla_caract_def = []
    for tupla in lista_tuplas:
        lista_intermedia = []
        for elemento in tupla:
            try:
                lista_intermedia.append(float(elemento))
            except:
                lista_intermedia.append(elemento)
        datos_tabla_caract_def.append(tuple(lista_intermedia))
    return datos_tabla_caract_def



def insertar_datos(query, contraseña, nombre_bbdd, lista_tuplas):
    """
    Inserta datos en una base de datos utilizando una consulta y una lista de tuplas como valores.
    Args:
    - query (str): Consulta SQL con placeholders para la inserción de datos.
    - contraseña (str): Contraseña para la conexión a la base de datos.
    - nombre_bbdd (str): Nombre de la base de datos a la que se conectará.
    - lista_tuplas (list): Lista que contiene las tuplas con los datos a insertar.
    Returns:
    - None: No devuelve ningún valor, pero inserta los datos en la base de datos.
    This function connects to a MySQL database using the given credentials, executes the query with the provided list of tuples, and commits the changes to the database. In case of an error, it prints the error details.
    """
    cnx = mysql.connector.connect(
        user="root",
        password=contraseña,
        host="127.0.0.1", database=nombre_bbdd
    )
    mycursor = cnx.cursor()
    try:
        mycursor.executemany(query, lista_tuplas)
        cnx.commit()
        print(mycursor.rowcount, "registro/s insertado/s.")
        cnx.close()
    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
        cnx.close()