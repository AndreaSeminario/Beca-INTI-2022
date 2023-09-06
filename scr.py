# Beca INTI/UNLZ 2022
# Andrea Seminario

import pdfplumber
import re
import csv

def Extract_Info(direction):

    """
    In this function, the text of each page stored in the pdf is extracted to later search for the terms already structured in the code, finally a string is returned where said data is separated by commas.

    Args:
        direction (string): The path to the pdf file to collect the searched information.

    Returns:
        string: The searched text in csv format (separated by commas) of each subfolder pdf files
    """

    try:
        pdf = pdfplumber.open(direction)
    except:
        print("ERROR")

    text = ""
    numberOfPages = len(pdf.pages)

    # bucle para que .pages lea las 9 paginas del pdf
    for i in range(numberOfPages):
        try:
            page = pdf.pages[i]
            text = text + page.extract_text()
        except:
            print("ERROR 2")
    
    newStr = ""
    
    try:
        newStr = newStr + \
            re.search('1.2 CUIT \(sin guiones\) (.*)\n', text).group(1)

    except:
        newStr = newStr + 'error'

    try:
        newStr = newStr + "," + re.search('1.7 País (.*)\n', text).group(1)
    except:
        newStr = newStr + "," + 'error'

    try:
        newStr = newStr + "," + \
        "\"" + \
            re.search('1.8 Provincia (.*)\n', text).group(1) + \
        "\""

    except:
        newStr = newStr + "," + 'error'

    try:
        newStr = newStr + "," + \
        "\"" + \
            re.search('1.11 Sector industrial (.*)\n', text).group(1) + \
        "\""

    except:
        newStr = newStr + "," + 'error'

    try:
        newStr = newStr + "," + \
            re.search('1.12 Inicio de Actividad \(Año\) (.*)\n', text).group(1)
    except:
        newStr = newStr + "," + 'error'

    # sentencias PARTE 4
    try:
        newStr = newStr + "," + \
            re.search('4.1 Personal directivo (.*)\n', text).group(1)
    except:
        newStr = newStr + "," + 'error'

    try:
        newStr = newStr + "," + \
            re.search('4.2 Mandos medios (.*)\n', text).group(1)
    except:
        newStr = newStr + "," + 'error'

    try:
        newStr = newStr + "," + \
            re.search('4.3 Personal operativo (.*)\n', text).group(1)
    except:
        newStr = newStr + "," + 'error'

    try:
        newStr = newStr + "," + \
            re.search('4.4 Personal administrativo (.*)\n', text).group(1)
    except:
        newStr = newStr + "," + 'error'

    try:
        newStr = newStr + "," + \
            re.search(
                '4.5 Personal IT \(Tecnologías de la Información\) (.*)\n', text).group(1)
    except:
        newStr = newStr + "," + 'error'

    try:
        newStr = newStr + "," + re.search('TOTAL (.*)\n', text).group(1)
    except:
        newStr = newStr + "," + 'error'
    # sentencias PARTE 6.2
    # condicion logica: si la busqueda da 'x' si, sino no.
    try:
        if (re.search('No se registran datos de proceso(.*)\n', text).group(1) == " x"):
            newStr = newStr + "," + "si"
        else:
            newStr = newStr + "," + "no"
    except:
        newStr = newStr + "," + 'error'

    try:
        if (re.search('Se registran datos del proceso pero no se analizan(.*)\n', text).group(1) == " x"):
            newStr = newStr + "," + "si"
        else:
            newStr = newStr + "," + "no"
    except:
        newStr = newStr + "," + 'error'

    try:
        if (re.search('Se registran y analizan datos del proceso(.*)\n', text).group(1) == " x"):
            newStr = newStr + "," + "si"
        else:
            newStr = newStr + "," + "no"
    except:
        newStr = newStr + "," + 'error'

    # if(re.search('Los registros del proceso se analizan y la información resultante(.*)\n', text).group(1) == " x"):
       # newStr = newStr + "," + "si"
    # else:
       # newStr = newStr + "," + "no"

    try:
        if (re.search('se utiliza para la toma de decisiones(.*)\n', text).group(1) == " x"):
            newStr = newStr + "," + "si"
        else:
            newStr = newStr + "," + "no"
    except:
        newStr = newStr + "," + 'error'

    # sentencias PARTE 6.3
    try:
        if (re.search('Papel(.*)\n', text).group(1) == " x"):
            newStr = newStr + "," + "si"
        else:
            newStr = newStr + "," + "no"
    except:
        newStr = newStr + "," + 'error'

    try:
        if (re.search('Planillas de cálculo(.*)\n', text).group(1) == " x"):
            newStr = newStr + "," + "si"
        else:
            newStr = newStr + "," + "no"
    except:
        newStr = newStr + "," + 'error'

    try:
        if (re.search('Software de gestión(.*)\n', text).group(1) == " x"):
            newStr = newStr + "," + "si"
        else:
            newStr = newStr + "," + "no"
    except:
        newStr = newStr + "," + 'error'

    try:
        if (re.search('Sensorización(.*)\n', text).group(1) == " x"):
            newStr = newStr + "," + "si"
        else:
            newStr = newStr + "," + "no"
    except:
        newStr = newStr + "," + 'error'

    # sentencias PARTE 6.4

    try:
        if (re.search('En tiempo real(.*)\n', text).group(1) == " x"):
            newStr = newStr + "," + "si"
        else:
            newStr = newStr + "," + "no"
    except:
        newStr = newStr + "," + 'error'

    try:
        if (re.search('Diariamente(.*)\n', text).group(1) == " x"):
            newStr = newStr + "," + "si"
        else:
            newStr = newStr + "," + "no"
    except:
        newStr = newStr + "," + 'error'

    try:
        if (re.search('Semanalmente(.*)\n', text).group(1) == " x"):
            newStr = newStr + "," + "si"
        else:
            newStr = newStr + "," + "no"
    except:
        newStr = newStr + "," + 'error'

    try:
        if (re.search('Mensualmente(.*)\n', text).group(1) == " x"):
            newStr = newStr + "," + "si"
        else:
            newStr = newStr + "," + "no"
    except:
        newStr = newStr + "," + 'error'

        # sentencias PARTE 12.1

    try:
        newStr = newStr + "," + \
            re.search('ERP o software de gestión\)\? (.*)\n', text).group(1)
    except:
        newStr = newStr + "," + 'error'

        # sentencias PARTE 15
    try:
        newStr = newStr + "," + \
            re.search(
                '\nCondiciones de orden y limpieza (.*)\n', text).group(1)
    except:
        try:
            newStr = newStr + "," + \
                re.search(
                    'Condiciones de orden y limpieza (.*)\nRegistros e indicadores', text).group(1)
        except:
            newStr = newStr + "," + 'error'

    try:
        newStr = newStr + "," + \
            re.search(
                '\nRegistros e indicadores (.*)', text).group(1)
    except:
        try:
            newStr = newStr + "," + \
                re.search(
                    'Registros e indicadores (.*)\nDigitalización de Registros e indicadores', text).group(1)
        except:
            newStr = newStr + "," + 'error'

    try:
        newStr = newStr + "," + \
            re.search('Estandarización de procesos (.*)\n', text).group(1)
    except:
        newStr = newStr + "," + 'error'

    try:
        newStr = newStr + "," + \
            re.search(
                'Conocimiento de herramientas de Kaizen (.*)\nPrograma de Mejora Continua', text).group(1)
    except:
        newStr = newStr + "," + 'error'

    try:
        newStr = newStr + "," + \
            re.search(
                '\nPrograma de Mejora Continua (.*)\n', text).group(1)
    except:
        newStr = newStr + "," + 'error'

    try:
        newStr = newStr + "," + \
            re.search('Nivel Kaizen asignado a la empresa: (.*)\n',text).group(1)
    except:
        newStr = newStr + "," + 'error'

        
 # Cerrar el archivo PDF después de haberlo procesado
    pdf.close()
        # print(newStr)
    return newStr