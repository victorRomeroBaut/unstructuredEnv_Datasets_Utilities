#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 10:19:03 2023

@Name: rename image sequences
@author: Victor Romero B.
@Description: 


"""

import os 


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

def ChangeFileName(fileNames, path, offset):
    # receive list of name files
    for i in range(len(fileNames)):
        oldName = os.path.join(path, fileNames[i])                   # get filename
        newName = os.path.join(path, (fileNames[i])[offset:])        # adjust to new filename
        os.rename(oldName, newName)                                  # rename file
    print("OK!")


if __name__ == "__main__":
    """sec_path = "/home/victor/Datasets/Rosario/rgb/"
    secs_img = ReadFiles([sec_path])
    
    # verify all names are equal lenght
    lengthN = len(secs_img[0])
    for i in range(1, len(secs_img)):
        lengthN2 = len(secs_img[i])
        if (lengthN2 > lengthN) or (lengthN2 < lengthN):
            print("no equal name sequence")
            break
        
    print("Equal lenght sequence image names")
    ChangeFileName(secs_img, sec_path, 5)"""
    