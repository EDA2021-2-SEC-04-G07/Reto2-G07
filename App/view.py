﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
from os import system
from datetime import date, time, datetime
import time
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from App import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la operación solicitada
"""

def printMenu():
    system("cls")
    #print("1- Cargar información en el catálogo")
    #print("2- Dar las n obras mas antiguas de un medio especifico")
    #print("3- Contar el número de obras de una nacionalidad")
    
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Lista cronólógica de los artistas")
    print("3- Lista cronológica de las adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Transportar obras de un departamento ")
    print("7- Crear nueva exposición")

catalogo = None

def initCatalogo():
    """
    Inicializa el catalogo del modelo
    """
    return controller.initCatalogo1()

def cargarDatos1(catalogo):
    """
    Carga las obras y los artistas en la estructura de datos
    """
    controller.cargarDatos1(catalogo)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    
    if int(inputs[0]) == 1:
        tiempo_inicial = time.process_time()    
        print("Cargando información de los archivos ....")

        catalogo = controller.initCatalogo1()
        cargarDatos1(catalogo)
        tiempo_final = time.process_time()
        duracion = (tiempo_final - tiempo_inicial)*1000
        
        print(f"El tiempo de carga de datos es: {duracion} milisegundos")
        input()
        system("cls")
        
        

    elif int(inputs[0]) == 2:
        
        anho_inicial = int(input("Digite el año inicial: "))
        anho_final = int(input("Digite el año final: "))
        
        tiempo_inicial = time.process_time()
        
        rango_artistas = controller.rangoArtistasPorAnho(catalogo, anho_inicial, anho_final)
        info_artistas = lt.newList(datastructure='ARRAY_LIST')
        
        for i in lt.iterator(rango_artistas):
            for j in lt.iterator(i):
                lt.addLast(info_artistas, j)
                
        primeros_3 = lt.subList(info_artistas, 1, 3)  
        ultimos_3 = lt.subList(info_artistas, (lt.size(info_artistas)-2), 3)  
        resultado_1 = 'Hay {} artistas nacidos entre {} y {}'.format(lt.size(info_artistas), str(anho_inicial), str(anho_final))
        
        print(resultado_1)
        print('========================================================')
        
        print('Los primeros 3 artistas en el rango son: ')
        print('        Nombre         | Fecha de Nacimiento | Fecha de muerte |   Nacionalidad   |    Género   ')
        print('==================================================================================================')
        for i in lt.iterator(primeros_3):
            print('{} \t\t\t {}  \t\t    {}   \t  {}\t\t  {}'.format(i['nombre'], i['fecha_nacimiento'], i['fecha_muerte'], i['nacionalidad'], i['genero']))
        print(' ')  
        print('Los últimos 3 artistas en el rango son: ')
        print('        Nombre         | Fecha de Nacimiento | Fecha de muerte |   Nacionalidad   |    Género   ')
        print('==================================================================================================')
        for i in lt.iterator(ultimos_3):
            print('{} \t\t\t {}  \t\t    {}   \t  {}\t\t  {}'.format(i['nombre'], i['fecha_nacimiento'], i['fecha_muerte'], i['nacionalidad'], i['genero']))
        print('==================================================================================================')    
        
        tiempo_final = time.process_time()
        duracion = (tiempo_final - tiempo_inicial)*1000
        
        print('El tiempo de ejecución fue de: ', duracion, ' ms.')

        input()
        system("cls")
        
        
        
    elif int(inputs[0]) == 3:
        pass
    
    
    
    elif int(inputs[0]) == 4:
        
        nombre_artista = input("Digite el nombre del artista: ")
        
        tiempo_inicial = time.process_time()
        
        entry_artista = mp.get(catalogo['artistas'], nombre_artista)
        info_artista = me.getValue(entry_artista)
        obras_artista = info_artista['obras']
        info_obras = lt.newList(datastructure='ARRAY_LIST')
        idArtista = info_artista['id']
        lista_medios = lt.newList(datastructure='ARRAY_LIST')
        lista_todos_medios = lt.newList(datastructure='ARRAY_LIST')
        lista_todos_medios = []
        
        for i in lt.iterator(obras_artista):
            entry_medio = mp.get(catalogo['obras'], i)
            info_medio = me.getValue(entry_medio)
            medio = info_medio['medio']
            
            if lt.isPresent(lista_medios, medio) == 0:
                lt.addLast(lista_medios, medio)
                
            lista_todos_medios.append(medio)
            lt.addLast(info_obras, info_medio)
            
        obras_artista_ordenada = controller.llamarQuicksort(info_obras, identificador=2)
        mayor = 0
        medio_mayor = None
            
        for i in lista_todos_medios:
            cont = lista_todos_medios.count(i)
            
            if cont > mayor:
                mayor = cont
                medio_mayor = i
            
        print("Clasificando ...")       
        print(('{} con MOMA Id {} tiene {} obras a su nombre en el museo.').format(nombre_artista, idArtista, lt.size(obras_artista)))
        print(('Existen {} medios/técnicas diferentes en su trabajo.').format(lt.size(lista_medios)))
        print('Su técnica más utilizada es {} con {} obras.'.format(medio_mayor, mayor))    
        print('')   
        print('\tTítulo \t |Fecha de la obra|    Técnica    |    \t\t Dimensiones    ')  
        print('==================================================================================================')      
        for i in lt.iterator(obras_artista_ordenada[1]):
            entry_cada_obra = mp.get(catalogo['obras'], i['titulo'])
            info_cada_obra = me.getValue(entry_cada_obra)
            
            if info_cada_obra['medio'] == medio_mayor:
                print('{}\t   {} \t\t {} \t\t {}'.format(info_cada_obra['titulo'], info_cada_obra['fecha'], info_cada_obra['medio'], info_cada_obra['dimensiones']))
        print('')
        
        tiempo_final = time.process_time()
        duracion = (tiempo_final - tiempo_inicial)*1000
        
        print('El tiempo de ejecución fue de: ', duracion, ' ms.')
        
        input()
        system("cls")  
        
        
    #elif int(inputs[0]) == 3:
        
        medio = input('Digite el medio a analizar: ')
        n = int(input('Digite el número de obras que quiere analizar: '))        
        datos = catalogo.copy()

        if mp.contains(catalogo['medios'], medio):
            entry = mp.get(catalogo['medios'], medio)
            obras_medio = me.getValue(entry)
            lista_obras = obras_medio['obras']
            controller.llamarOrdenarObras(lista_obras, 3) 
            a=0
            print(f'Las {n} obras mas antiguas de este medio son :\n')
            for obra in lt.iterator(lista_obras):
                print(obra)
                a=a+1
                if a == n:
                    break                
        else:
            print('Ese medio no se encuentra en el museo')
            input()
            break

        input()
        system("cls")

    if int(inputs[0]) == 4:
        input()

    if int(inputs[0]) == 5:
        nacionalidad = input("Escriba la nacionalidad: ")
        lista_nacionalidades = catalogo['nacionalidades']
        entri = mp.get(lista_nacionalidades, nacionalidad)
        lista_filtrada = me.getValue(entri)
        print('Existen {} obras en la nacionalidad mencionada'.format(lt.size(lista_filtrada)))
        input()
        system("cls")

    if int(inputs[0]) == 6:
        input()

    else:
        system("cls")

sys.exit(0)
