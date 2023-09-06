# Beca INTI/UNLZ 2022
# Andrea Seminario

import os
import pdfplumber
import scr


# corroboramos que sea un pdf
def PDF_Check(path_to_file):

    """
    In this function it is verified that the address of the sent file corresponds to a file with the extension .pdf

    Args:
        path_to_file (string): The path to the file to check if it is a pdf file.

    Returns:
        boolean: true or false.
    """

    if (os.path.splitext(path_to_file)[1] == ".pdf"):
        return True
    else:
        return False

# retornamos el nombre del pdf
def Vector_PDF_Names(direction):

    """
    The Vector_PDF_Names receives only one parameter, the directory of a subfolder where the files to be processed will be.
    In this function the name of each subdirectory is checked and if it is a file with a .pdf extension (using PDF_Check of this module) it will be added to a pdf names vector who will be
    returned.

    Args:
        direction (string): The path to the subfolder to collect pdf files.

    Returns:
        vector: return a strings vector, where each position have a pdf file name.
    """

    vector = []
    for entry in os.scandir(direction):
        if (entry.is_file()):
            if (PDF_Check(entry)):
                vector.append(entry.name)
    return vector

# imprimimos el pdf de tal direccion
def String_Subfolder(direction, n=-1):

    """
    The String_Subfolder function gets two parameters, a path to the subfolder (this folder contains the files to be processed) and a number that decides how many files to process per subfolder, then it will return a string with the pdf processed in the subfolders.


    Args:
        direction (string): The path to the subfolder to collect pdf files and later use this names.
        n (int, optional): The limit number of files to process. Defaults to -1. When the value is -1 the algorithm procces all files.

    Returns:
        string: The searched text in csv format (separated by commas) of each subfolder
    """

    vector = Vector_PDF_Names(direction)[:]
    stringContainer = ""
    try:
        if (n == -1):
            for i in range(len(vector)):
                stringContainer += '\n' + \
                    scr.Extract_Info(f'{direction}{vector[i]}')
        else:
            if(len(vector) >= n):
                for i in range(n):
                    stringContainer += '\n' + \
                        scr.Extract_Info(f'{direction}{vector[i]}')
            else:
                for i in range(len(vector)):
                    stringContainer += '\n' + \
                        scr.Extract_Info(f'{direction}{vector[i]}')
        return (stringContainer)
    except Exception as e:
        print(f'Reading Error My Friend - {e}')


# Lectura de Carpeta Prediagnosticos automatizada
def String_Folder(dir, n = -1):
    
    """
    The String_Folder function gets two parameters, a path to the parent folder and a number that decides how many files will be processed per subfolder, then it will return a string with the pdf processing in the subfolders.

    Args:
        dir (string): The path to the main folder.
        n (int, optional): The limit number of files to process. Defaults to -1. When the value is -1 the algorithm procces all files.

    Returns:
        string: The final string. All searched text in csv format (sepparated by commas) of each subfolder.
    """

    strFinal = ""
    for entry in os.scandir(dir):
        try:
            strFinal += String_Subfolder(f'{dir}{entry.name}/', n)
        except Exception as e:
            print(e)
    return strFinal