# -*- coding: utf-8 -*-
"""
Created on Thu May 27 20:54:15 2021

@author: juand
"""
import pandas as pd
import matplotlib.pyplot as plt

def cargar_datos(nombre: str)-> pd.DataFrame:
    
    datos= pd.read_csv(nombre)
    
    return datos

datos =cargar_datos("ICFES.CSV")
def distribucion_poblacion(datos: pd.DataFrame)-> None:
    
    nacionalidades= datos[(datos.NACIONALIDAD != "VENEZUELA") & (datos.NACIONALIDAD != "COLOMBIA")]
    contar= nacionalidades.NACIONALIDAD.value_counts()
    frecuencia= contar.sum()
    contar= contar.divide(frecuencia, fill_value=0).sort_index()
    contar.plot(kind= "bar", title="Distribución de Nacionalidad", xlabel="Nacionalidad", ylabel="Frecuencia")
    plt.show()

def poblacion_genero(datos: pd.DataFrame, estrato: str)-> None:
    
    frame_estratos= datos[datos.ESTRATO == estrato]
    frame_estratos= frame_estratos.GENERO.value_counts().plot(kind= "pie", title="Diagrama de torta para el " + estrato, ylabel= "Estudiantes", figsize=(5,5), autopct='%1.1f%%').legend()
    plt.show()
  
def mejores_10(datos: pd.DataFrame)-> None:
    
    nuevo_frame= datos.groupby("DEPARTAMENTO")["PUNT_GLOBAL"].mean()
    nuevo_frame= nuevo_frame.nlargest(10).iloc[::-1].plot(kind= "barh", title="Top 10 Departamentos con mejor promedio", xlabel="Puntaje global promedio", ylabel="Departamentos")
    plt.show()
    
def peores_5_municipios(datos: pd.DataFrame, departamento: str)-> None:
    
    dept= datos[datos.DEPARTAMENTO == departamento]
    municipios= dept.groupby("MUNICIPIO")["PUNT_LECTURA_CRITICA"].mean()
    punt_mat= dept["PUNT_MATEMATICAS"].mean()
    punt_nat= dept["PUNT_NATURALES"].mean()
    punt_soc= dept["PUNT_SOCIALES"].mean()
    punt_ing= dept["PUNT_INGLES"].mean()
    municipios= pd.DataFrame(municipios)
    municipios["PUNT_MATEMATICAS"]= punt_mat
    municipios["PUNT_NATURALES"]= punt_nat
    municipios["PUNT_SOCIALES"]= punt_soc
    municipios["PUNT_INGLES"]= punt_ing
    
    municipios= municipios.nsmallest(5, ["PUNT_MATEMATICAS", "PUNT_SOCIALES", "PUNT_NATURALES", "PUNT_INGLES", "PUNT_LECTURA_CRITICA"]).plot(kind= "barh", xlabel="Puntaje", ylabel="Municipio", figsize=(10, 5))
    municipios.legend(loc="upper left")
    plt.show()

def top_10municipios(datos: pd.DataFrame, categoria: str)-> None:
    
    if(categoria=="MATEMATICAS") or (categoria=="NATURALES") or (categoria=="INGLES") or (categoria=="SOCIALES"):
        categoria= "PUNT_" + categoria
    else:
        categoria= "PUNT_" + categoria + "_CRITICA"
    
    nuevo_frame= datos.groupby("MUNICIPIO")[categoria].mean()
    nuevo_frame= nuevo_frame.nlargest(10).iloc[::-1].plot(kind= "barh", title="Top 10 Municipios con mejor promedio en " + categoria, xlabel="Puntaje global promedio", ylabel="Departamentos")
    plt.show()

def nutricion_categoria(datos: pd.DataFrame, puntaje: str, alimento: str)->None:
    
    datos.loc[:, [alimento, puntaje]].boxplot(by= alimento, figsize=[11, 7])
    datos.set_index([alimento],inplace=True)
    plt.show()
    
def diagramas_caja(datos: pd.DataFrame)-> None:
    
    datos.loc[:, ["ESTRATO", "PUNT_GLOBAL"]].boxplot(by="ESTRATO")
    plt.show()

def crear_matriz(datos: pd.DataFrame) -> tuple:
    '''
    La función debe retornar una tupla que contenga la matriz, el diccionario de filas y el diccionario de columnas.
    Para esta función ya se le proporciona el código para construir los diccionarios. Su tarea es construir la matriz
    como se indica en el enunciado
    :param datos: DataFrame a leer para la consturcción de la matriz
    :return: Tupla de la forma (matriz, dict_filas, dict_columnas)
    '''
    estratos = datos["ESTRATO"].unique()
    estratos.sort()
    estratos_dict = dict(list(enumerate(estratos)))
    lectura = datos["LECTURA_DIARIA"].unique()
    lectura.sort()
    aux = lectura[2]
    lectura[2] = lectura[1]
    lectura[1] = aux
    lectura_dict = dict(list(enumerate(lectura)))
    # TODO: Completar la construcción de la matriz
    
    matriz = [[None] * len(lectura) for i in range(len(estratos))]
    test= datos[["ESTRATO", "LECTURA_DIARIA"]].apply('.'.join, axis=1).value_counts().sort_index()
    lista= test.values.copy()

    for n in range(len(test)):
        
        if(n%5 == 2):
            aux = lista[n]
            lista[n] = lista[n-1]
            lista[n-1] = aux 
    count= 0

    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            matriz[x][y]= lista[count]
            count+=1
   
    return (matriz, estratos_dict, lectura_dict)


def estudiantes_estrato(tupla: tuple, estrato: str)-> int:
    
    estratos_dict= tupla[1]
    matriz= tupla[0]
    for key in estratos_dict:
        
        if estratos_dict[key] == estrato:
            res = key
            
    y=0
    respuesta= 0
    
    while y < len(matriz[res]):
        
        respuesta+=matriz[res][y] 
        y+=1
    
    return respuesta

def estudiantes_lectura_establecida(tupla: tuple, horas_diarias: str)-> int:
    
    lectura_dict= tupla[2]
    matriz= tupla[0]
    for key in lectura_dict:
        
        if lectura_dict[key] == horas_diarias:
            res= key
            
    x= 0
    respuesta= 0
    
    while x < len(matriz):
        
        respuesta+= matriz[x][res]
        x+=1

    return respuesta

def estrato_mas_estudiantes(tupla: tuple)-> str:
    matriz= tupla[0]
    estratos_dict= tupla[1]
    dict_estratos= {}
    x= 0
    for cada_llave in estratos_dict:
        
        dict_estratos[estratos_dict[cada_llave]]= 0
        
    while x < len(matriz):
        y= 0
        while y < len(matriz[x]):
            
            dict_estratos[estratos_dict[x]]+= matriz[x][y]
            y+=1
            
        x+=1
    
    max_key = max(dict_estratos, key=dict_estratos.get)
    
    return max_key

def estrato_lectura_mas_estudiantes(tupla: tuple)-> tuple:
    matriz= tupla[0]
    estratos_dict= tupla[1]
    lectura_dict= tupla[2]
    x= 0
    max_value= 0
    while x < len(matriz):
        y=0
        while y < len(matriz[x]):
            
            if(matriz[x][y] > max_value):
                
                max_value= matriz[x][y]
                lista=[x, y]
            y+=1
        x+=1
    
    res1= estratos_dict[lista[0]]
    res2= lectura_dict[lista[1]]
  
    return (res1, res2)
