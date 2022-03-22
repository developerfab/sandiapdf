#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
from PyPDF2 import PdfFileMerger
from os import listdir

import img2pdf
import os
import tempfile

folder_path = input("Ingrese la ruta de la carpeta que contiene las imagenes: ")
output_file_name = input("Ingrese la ruta de salida del archivo y el nombre: ")

print(f'Carpeta: {folder_path}')

archivos_path = listdir(folder_path)
archivos_path.sort()
for files in archivos_path:
    print(files)

files_b = []
for fname in archivos_path:
    with Image.open(folder_path+'/'+fname) as image:
        archivo_salida = tempfile.TemporaryFile()
        pdf_bytes = img2pdf.convert(image.filename)
        archivo_salida.write(pdf_bytes)
        files_b.append(archivo_salida)

# Merge the generated files
mezclador = PdfFileMerger()
for file in files_b:
    mezclador.append(file)

mezclador.write(output_file_name)
mezclador.close

print("Archivo generado exitosamente")
