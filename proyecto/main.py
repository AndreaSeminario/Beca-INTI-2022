# Beca INTI/UNLZ 2022
# Andrea Seminario

import scr2
import analisys

def CSV_Generate(dir, n = -1):

    """
    This function takes two parameters, a root directory and a number. Basically, it calls String_Folder and gets the same data, but also generates a .csv file and its headers.

    Args:
        dir (string): The path to the main folder.
        n (int, optional): The limit number of files to process. Defaults to -1. When the value is -1 the algorithm procces all files.
    """

    csv_string = scr2.String_Folder(dir, n)
    #Cargamos los encabezados
    campos = "CUIT,"\
         "País,"\
         "Provincia,"\
         "Sector industrial,"\
         "Inicio de Actividad (Año),"\
         "Personal directivo,"\
         "Mandos medios,"\
         "Personal operativo,"\
         "Personal administrativo,"\
         "Personal IT (Tecnologías de la Información),"\
         "TOTAL,"\
         "No se registran datos de proceso,"\
         "Se registran datos del proceso pero no se analizan,"\
         "Los registros del proceso se analizan y la información resultante,"\
         "se utiliza para la toma de decisiones,"\
         "Papel,"\
         "Planillas de cálculo,"\
         "Software de gestión,"\
         "Sensorización,"\
         "En tiempo real,"\
         "Diariamente,"\
         "Semanalmente,"\
         "Mensualmente,"\
         "Herramientas integradas de gestion"\
         "Condiciones de orden y limpieza Nivel,"\
         "Registros e indicadores Nivel,"\
         "Estandarización de procesos Nivel,"\
         "campo1,"\
         "campo2,"\
         "campo3,"\
         "KAIZEN LEVEL"
    try:
        with open('csv_string.csv', 'w') as file:
            file.write(campos)
            file.write(csv_string)
        print("Archivo creado exitosamente.")
    except Exception as e:
        print(e)

CSV_Generate('ruta//absoluta//a//tu//directorio//principal//prediagnóstico', -1)

analisys.Read_CSV_PAC('ruta/a/tu/archivo/csv/generado/csv_string.csv')

