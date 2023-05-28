#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 15:03:12 2023

@Name:        Generate image sequence
@author:      Victor Romero B.
@Description: Generate the master sequence

"""


import os
import numpy as np

def ReadFiles(path):
    archivos = []
    for i in range(len(path)):
        # leer todas las imagenes dentro de la carpeta
        for root,dirs,files in os.walk(path[i]):
            print('root: ', path[i])
            for infile in [f for f in files if f.lower().endswith('.png')]:
                file,ext = os.path.splitext(infile)
                try:
                    full_path = os.path.join(root,infile)
                except IOError:
                    print("No se pudo leer la imagen",infile)
        archivos.append(files)
    # reducir a una lista
    imgs = []
    for i in range(len(archivos)):
        for j in range(len(archivos[i])):
            imgs.append(archivos[i][j]) # path[i] + 
    return imgs

def TimestampName(fileNames, offset):
    # receive list of name files
    timestamp = []
    for i in range(len(fileNames)):
        timestamp.append((fileNames[i])[:offset])         # adjust to new filename
    return timestamp

def AddPath(path, filenames):
    imagePath = []
    for i in range(len(filenames)):
        imagePath.append(path + filenames[i])
    return imagePath


if __name__ == "__main__":
    sec_path = "/home/victor/Datasets/Rosario/rgb/"
    localPath = "rgb/"
    imgs_name = ReadFiles([sec_path])
    
    imgs_name.sort()                                      # sort name
    timestamp = TimestampName(imgs_name, 17)              # generate timestamp name
    imagePath = AddPath(localPath, imgs_name)
    fileData = [timestamp, imagePath]
    file = open("ts.txt", "w")
    for i in range(len(fileData[0])):
        fila = [str(timestamp[i]), str(imagePath[i])]
        file.write(' '.join(fila))
        file.write("\n")
    file.close()
        