#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from convert import *

def menu():
    print("·-----------------------------------·")
    print("|       Convert images to pdf       |")
    print("·-----------------------------------·")
    print("| 1 - Convert an image              |")
    print("| 2 - Convert a folder with images  |")
    print("| 3 - Exit                          |")
    print("·-----------------------------------·")

def convert_folder():
    # Request the data to the user
    source_path = input("Ingrese la ruta de la carpeta que contiene las imagenes: ")
    output_file_name = input("Ingrese la ruta de salida del archivo y el nombre: ")

    # Showing files in the source path
    archivos_path = listdir(source_path)
    archivos_path.sort()
    list_files = []

    for files in archivos_path:
        list_files.append(source_path+"/"+files)
        print(files)
    # Call the generator class
    convert = Convert(source_path, output_file_name)
    convert.generate(list_files)

entrada = 0
while entrada != 3:
    menu()
    entrada = int(input("> "))
    if entrada == 2:
        os.system('cls')
        os.system('clear')
        convert_folder()
    elif entrada == 3:
        print("Gracias por usar la app, adios!")
        break
    else:
        print("Opción no valida")
