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
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    system("cls")
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Dar las n obras mas antiguas de un medio especifico")

catalogo = None

def initCatalogo():
    """
    Inicializa el catalogo del modelo
    """
    return controller.initCatalogo()

def cargarDatos(catalogo):
    """
    Carga las obras y los artistas en la estructura de datos
    """
    controller.cargarDatos(catalogo)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    
    if int(inputs[0]) == 1:
            
        print("Cargando información de los archivos ....")
        catalogo = controller.initCatalogo(tipo_lista = 'ARRAY_LIST')
        cargarDatos(catalogo)

        system("cls")
        

    elif int(inputs[0]) == 2:
        
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

    else:
        system("cls")
        sys.exit(0)
sys.exit(0)
