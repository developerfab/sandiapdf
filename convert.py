#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
from PyPDF2 import PdfFileMerger
from os import listdir

import img2pdf
import os
import tempfile

class Convert:
    def __init__(self, output_file_name):
        self.output_file_name = output_file_name

    def generate(self, list_files):
        # files_b is a list that store each pdf file generated.
        files_b = []
        # It convert each file in the folder
        for file_name in list_files:
            # It open the image and apply an alias as `image`
            with Image.open(file_name) as image:
                # It creates a temporal empty file
                output_file = tempfile.TemporaryFile()
                # It converts the image to pdf format
                pdf_bytes = img2pdf.convert(image.filename)
                # It writes the conversion in the file
                output_file.write(pdf_bytes)
                # It adds the new file to the list
                files_b.append(output_file)

        # It creates a new instance of PdfFileMerger
        file_merged = PdfFileMerger()
        # It adds each file in the list in a file
        for file in files_b:
            file_merged.append(file)

        # It creates the output file
        file_merged.write(self.output_file_name)
        # It closes the file
        file_merged.close

        print("The file has been generated in the path specified")
