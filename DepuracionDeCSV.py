import pandas
### NO DESCOMENTAR NI EJECUTAR ###
"""
tabla = pandas.read_csv('plotly version semifinal-prueba copy 5.csv')
tabla_sin_duplicados=tabla.drop_duplicates(subset=None, 
                          keep='first', 
                          inplace=False, 
                          ignore_index=False)


tabla_sin_duplicados.to_csv('plotly version semifinal-prueba copy 6.csv', index=False)
"""

### NO DESCOMENTAR NI EJECUTAR ###
"""
tablon = pandas.read_csv('plotly version semifinal-prueba.csv')
tablon2 = pandas.read_csv('plotly version semifinal-prueba copy.csv')
tablon3 = pandas.read_csv('plotly version semifinal-prueba copy 2.csv')

print(tablon)


print(tablon2['ids'].value_counts())

tablon = tablon[['parents','labels','ids']]

print(tablon)

tablon.to_csv('plotly version semifinal-prueba.csv', index=False)



for i in tablon2.index:
    tablon2['ids'][i] = tablon2['parents'][i] +'-'+ tablon2['labels'][i]
    tablon2['parents'][i] = tablon3['ids'][i] +'-'+ tablon2['parents'][i]

#print(tablon['ids'][0])
 

#tablon2.to_csv('plotly version semifinal-prueba copy.csv', index=False)

"""