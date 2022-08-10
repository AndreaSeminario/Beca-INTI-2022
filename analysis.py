import pandas
import matplotlib.pyplot as plt


#df = pd.read_excel('F:\FilesProyectVSC\ProyectoINTI\Libro5.xlsx')
#print(df)

tabla = pandas.read_csv('registro_mipyme_09-05-2022.csv')

#print(pd.options.display.max_rows) 
print(tabla)


"""
print(tabla['Sector'].value_counts())
print(tabla['Provincia'].value_counts())
print(tabla['Sector'].value_counts(normalize=True))
print(tabla['Provincia'].value_counts(normalize=True))
"""
#tabla['Sector'].value_counts().to_frame()
"""
tabla['Sector'].value_counts().plot(kind="bar")
plt.show()


tabla['Provincia'].value_counts().plot(kind="bar")
plt.show()
""" 

"""
print(tabla['Regimen_Tributario'].value_counts())
print(tabla['Categoria'].value_counts())
print(tabla['Regimen_Tributario'].value_counts(normalize=True))
print(tabla['Categoria'].value_counts(normalize=True))
"""
