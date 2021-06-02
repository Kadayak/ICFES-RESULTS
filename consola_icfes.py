# -*- coding: utf-8 -*-
"""
Created on Mon May 31 13:36:52 2021

@author: juand
"""
import pandas as pd
import resultados_icfes as res

def ejecutar_cargar_datos()->pd.DataFrame:

    datos= None
    archivo= input("Por favor ingrese el nombre del archivo .CSV con los resultados del ICFES: ")
    datos= res.cargar_datos(archivo)
    
    if(len(datos)==0):
        print("El nombre del archivo no es válido, inténtelo de nuevo.")
    else:
        print("Se cargaron los datos exitosamente.")

    return datos

def ejecutar_distribucion_poblacion(datos: pd.DataFrame)-> None:
    
    print("***** Ejecutando 'análisis de la distribución de la población' según la nacionalidad *****")
    res.distribucion_poblacion(datos)
    print("Por favor, vea la ventana 'plot' para ver las gráficas")

def ejecutar_poblacion_genero(datos: pd.DataFrame)-> None:
    
    print("***** Ejecutando 'análisis de la distribución de la población' según el género y el estrato *****")
    estrato= input("Digite el estrato del cual desea saber la distribución: ")
    res.poblacion_genero(datos, estrato)
    print("Por favor, vea la ventana 'plot' para ver las gráficas")

def ejecutar_mejores_10(datos: pd.DataFrame)-> None:
    
    print("***** Ejecutando 'desempeño de los mejores 10 departamentos' *****")
    res.mejores_10(datos)
    print("Por favor, vea la ventana 'plot' para ver las gráficas")
    
def ejecutar_peores_5_municipios(datos: pd.DataFrame)-> None:
    
    print("***** Ejecutando 'desempeño de los peores 5 municipios por departamento' *****")
    departamento= input("Digite el departamento del cual desea conocer los puntajes de sus peores 5 municipios: ")
    res.peores_5_municipios(datos, departamento)
    print("Por favor, vea la ventana 'plot' para ver las gráficas")
    
def ejecutar_top_10municipios(datos: pd.DataFrame)-> None:
    
    print("***** Ejecutando 'desempeño de los mejores 10 municipios por categoría' *****")
    categoria= input("Digite la categoría de la cual desea saber sus 10 mejores municipios (Ej. 'MATEMATICAS'): ")
    res.top_10municipios(datos, categoria)
    print("Por favor, vea la ventana 'plot' para ver las gráficas")

def ejecutar_diagramas_caja(datos: pd.DataFrame)-> None:
    
    print("***** Ejecutando 'ver diagramas de caja según estrato' *****")
    res.diagramas_caja(datos)
    print("Por favor, vea la ventana 'plot' para ver las gráficas")
    
def ejecutar_nutricion_categoria(datos: pd.DataFrame)-> None:
    
    print("***** Ejecutando 'desempeño de estudiantes según el tipo de puntaje y su nutrición' *****")
    puntaje= input("Digite el tipo de puntaje sobre el cual desea ver el diagrama de cajas (Ej. 'PUNT_MATEMATICAS'): ")
    alimento= input("Escriba el tipo de alimento sobre el cual desea ver el diagrama de cajas(Ej. 'FRUTOS'): ")
    res.nutricion_categoria(datos, puntaje, alimento)
    print("Por favor, vea la ventana 'plot' para ver las gráficas")
    
def ejecutar_crear_matriz(datos: pd.DataFrame)-> tuple:
    
    print("***** Ejecutando 'crear matriz' *****")
    respuesta= res.crear_matriz(datos)
    print("La matriz es la siguiente:", respuesta[0])
    return respuesta

def ejecutar_estudiantes_estrato(tupla: tuple)-> None:
    
    print("***** Ejecutando 'número de estudiantes que presentaron la prueba según el estrato' *****")
    estrato= input("Digite el estrato (Ej. 'Estrato 1') del cual desea saber el número de estudiantes que presentaron la prueba: ")
    respuesta= res.estudiantes_estrato(tupla, estrato)
    print("El número de estudiantes del " + estrato + " que presentaron la prueba es de:", respuesta)
    
def ejecutar_estudiantes_lectura_establecida(tupla: tuple)-> None:
    
    print("***** Ejecutando 'número de estudiantes que leyeron un cierto número de tiempo establecido.' *****")
    horas_diarias= input("Escriba el tiempo establecido del cual desea conocer el número de estudiantes (Ej. '30 minutos o menos'). ")
    print("El número de estudiantes que leyeron " + horas_diarias + " fue de", res.estudiantes_lectura_establecida(tupla, horas_diarias))
    
def ejecutar_estrato_mas_estudiantes(tupla: tuple)-> None:
    
     print("***** Ejecutando 'Estrato con más estudiantes' *****")
     print("El estrato con más estudiantes que presentaron la prueba fue el " + res.estrato_mas_estudiantes(tupla))
     
def ejecutar_estrato_lectura_mas_estudiantes(tupla: tuple)-> None:
    
     print("***** Ejecutando 'Estrato y tiempo de lectura con mayor número de estudiantes' *****")
     respuesta= res.estrato_lectura_mas_estudiantes(tupla)
     print("El tiempo de lectura y el estrato donde más estudiantes hubo fue el " + respuesta[0] + " con " + respuesta[1] + ".")
     
def mostrar_menu():
    print("\nOpciones")
    print("1. Cargar el archivo con los resultados del ICFES.")
    print("2. Ver la gráfica de análisis de población según su nacionalidad.")
    print("3. Consultar la distribución de acuerdo con su género para un estrato.")
    print("4. Consultar desempeño mejores 10 departamentos.")
    print("5. Consultar los 5 municipios con un puntaje más bajo de un departamento.")
    print("6. Consultar los mejores 10 municipios dada una categoría de evaluación.")
    print("7. Consultar diagramas de caja según el estrato.")
    print("8. Consultar diagramas de caja por nutrición y categoría.")
    print("9. Construir una matriz que contenga los datos organizados por estrato y tiempo de lectura")
    print("10. Consutlar el número de estudiantes que presentaron la prueba según su estrato.")
    print("11. Consultar el número de estudiantes dado un tiempo de lectura diaria.")
    print("12. Consultar el estrato con mayor número de estudiantes.")
    print("13. Consultar el estrato y tiempo de lectura con mayor número de estudiantes.")
    print("14. Salir de la aplicacion")

def iniciar_aplicacion():
    
    continuar  = True
    datos = None
    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opción: "))
        if opcion_seleccionada == 1:
            datos = ejecutar_cargar_datos()
        elif opcion_seleccionada == 2:
            ejecutar_distribucion_poblacion(datos)
        elif opcion_seleccionada == 3:
            ejecutar_poblacion_genero(datos)
        elif opcion_seleccionada == 4:
            ejecutar_mejores_10(datos)
        elif opcion_seleccionada == 5:
            ejecutar_peores_5_municipios(datos)
        elif opcion_seleccionada == 6:
            ejecutar_top_10municipios(datos)
        elif opcion_seleccionada == 7:
            ejecutar_diagramas_caja(datos)
        elif opcion_seleccionada == 8:
            ejecutar_nutricion_categoria(datos)
        elif opcion_seleccionada == 9:
            tupla= ejecutar_crear_matriz(datos)
        elif opcion_seleccionada == 10:
            ejecutar_estudiantes_estrato(tupla)
        elif opcion_seleccionada == 11:
            ejecutar_estudiantes_lectura_establecida(tupla)
        elif opcion_seleccionada == 12:
            ejecutar_estrato_mas_estudiantes(tupla)
        elif opcion_seleccionada == 13:
            ejecutar_estrato_lectura_mas_estudiantes(tupla)
        elif opcion_seleccionada == 14:
            continuar = False
        else:
            print("Por favor ingrese una opcion válida")


iniciar_aplicacion()
