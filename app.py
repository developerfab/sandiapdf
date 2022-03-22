#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from convert import *

def menu():
    print("·-----------------------------------·")
    print("|       Convert images to pdf       |")
    print("·-----------------------------------·")
    print("| 1 - Convert an image              |")
    print("| 2 - Convert a folder with images  |")
    print("| 3 - Exit                          |")
    print("·-----------------------------------·")

entrada = 0
while entrada != 3:
    menu()
    entrada = input("> ")
