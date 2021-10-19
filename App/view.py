"""
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
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronologicamente los aristas")
    print("3- Dar las n obras mas antiguas de un medio especifico")
    print("5- Contar el número de obras de una nacionalidad")

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
        system("cls")
        
    elif int(inputs[0]) == 2:
        
        anho_inicial = int(input("Digite el año inicial: "))
        anho_final = int(input("Digite el año final: "))
        
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
        #print('El tiempo de ejecución fue de: ', rango_ordenado[0], ' ms.')

        input()
        system("cls")
        
    if int(inputs[0]) == 3:
        
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
