# Beca INTI/UNLZ 2022
# Andrea Seminario

import pandas
import matplotlib.pyplot as plt

def Read_CSV_MiPyMES(dir):
    try:
        tabla = pandas.read_csv(dir)

        # Conteo por sector
        print(tabla['Sector'].value_counts())
        print(tabla['Sector'].value_counts(normalize=True))  # %
        # Grafico sector
        tabla['Sector'].value_counts().plot(kind="bar")
        plt.show()

        # Conteo por Provincia
        print(tabla['Provincia'].value_counts())
        print(tabla['Provincia'].value_counts(normalize=True))  # %
        # Grafico Provincia
        tabla['Provincia'].value_counts().plot(kind="bar")
        plt.show()
    except Exception as e:
        print(f'Error al procesar el archivo CSV: {str(e)}')

def Read_CSV_PAC(dir):
    try:
        tabla = pandas.read_csv(dir)

        # Conteo por sector
        print(tabla['Sector industrial'].value_counts())
        print(tabla['Sector industrial'].value_counts(normalize=True))  # %
        # Grafico sector
        tabla['Sector industrial'].value_counts().plot(kind="bar")
        plt.show()

        # Conteo por Nivel de Kaizen
        print(tabla['KAIZEN LEVEL'].value_counts())
        print(tabla['KAIZEN LEVEL'].value_counts(normalize=True))  # %
        # Grafico Nivel de Kaizen
        tabla['KAIZEN LEVEL'].value_counts().plot(kind="bar")
        plt.show()

        # Conteo por Provincia
        print(tabla['Provincia'].value_counts())
        print(tabla['Provincia'].value_counts(normalize=True))  # %
        # Grafico Provincia
        tabla['Provincia'].value_counts().plot(kind="bar")
        plt.show()
    except Exception as e:
        print(f'Error al procesar el archivo CSV: {str(e)}')
