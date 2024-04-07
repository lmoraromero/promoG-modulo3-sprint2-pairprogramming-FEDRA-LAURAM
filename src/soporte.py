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
       

def exploracion_dataframe(dataframe):
    """Esta función  imprime información sobre la forma, columnas, tipos de datos, valores nulos, duplicados, valores duplicados 
    de cada columna, valores únicos de cada columna, y realiza un resumen estadístico para las columnas numéricas 
    y categóricas. """

    #Nos enseña los duplicados en el DF
    print(f"Tenemos {dataframe.duplicated().sum()} duplicados en el conjunto de datos.")
    print("\n ----- \n")
    
    
    #Nos muestra un DataFrame para los valores nulos
    print("Los nulos que tenemos en el conjunto de datos son:")
    df_nulos = pd.DataFrame(dataframe.isnull().sum() / dataframe.shape[0] * 100, columns = ["%_nulos"])
    display(df_nulos[df_nulos["%_nulos"] > 0])
    
    print("\n ----- \n")
    #Nos muestra los tipos de columnas
    print(f"Los tipos de las columnas son:")
    display(pd.DataFrame(dataframe.dtypes, columns = ["tipo_dato"]))
    
    
    print("\n ----- \n")
    #Nos muestra los valores de las columnas categóricas
    print("Los valores que tenemos para las COLUMNAS CATEGÓRICAS son: ")
    dataframe_categoricas = dataframe.select_dtypes(include = "O")
    
    for col in dataframe_categoricas.columns:
        print(f"La columna {col.upper()} tiene las siguientes valores únicos:")
        display(pd.DataFrame(dataframe[col].value_counts()).head())    
    
    #Sacamos los principales estadísticos de cada una de las categorías

    columnas_numericas = dataframe.select_dtypes(include=['int', 'float']).columns
    columnas_categoricas = dataframe.select_dtypes(include='O').columns

    for col in columnas_categoricas:
        print("\n ----- \n")
        print(f"Los principales estadísticos de las COLUMNAS CATEGÓRICAS para el {col.upper()} son: ")
        display(dataframe[[col]].describe().T)

    for col in columnas_numericas:
        print("\n ----- \n")
        print(f"Los principales estadísticos de las COLUMNAS NUMÉRICAS para el {col.upper()} son: ")
        display(dataframe[[col]].describe().T)


def imputar_nulos(dataframe):
    """ funcion para imputar nulos"""

    for col in dataframe.columns:
        dataframe[col] = dataframe[col].fillna('desconocido')

    print("Después del reemplazo usando 'fillna' quedan los siguientes nulos")
    print(dataframe.isnull().sum())



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