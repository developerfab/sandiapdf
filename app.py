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
    source_path = input("Folder where the images are store: ")
    output_file_name = input("Path and name of output file: ")

    # Showing files in the source path
    files_path = listdir(source_path)
    files_path.sort()
    list_files = []

    for files in files_path:
        # Validation for mac folders
        if files == '.DS_Store':
            next
        else:
            list_files.append(source_path+"/"+files)
            print(files)
    print(list_files)
    # Call the generator class
    convert = Convert(output_file_name)
    convert.generate(list_files)

def convert_image():
    image_path = input("Path and file name where the image is store: ")
    output_file_name = input("Path and name of output file: ")
    list_files = []
    list_files.append(image_path)
    # Call the generator class
    convert = Convert(output_file_name)
    convert.generate(list_files)

option = 0
while option != 3:
    menu()
    option = int(input("> "))
    if option == 1:
        os.system('cls')
        os.system('clear')
        convert_image()
    if option == 2:
        os.system('cls')
        os.system('clear')
        convert_folder()
    elif option == 3:
        print("Thanks for use the app, bye!")
        break
    else:
        print("This option isn't available :(")
