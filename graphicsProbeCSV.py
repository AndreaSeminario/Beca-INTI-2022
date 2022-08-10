import plotly.graph_objects as go

import pandas as pd

df1 = pd.read_csv('F:\FilesProyectVSC\ProyectoINTIAndrea\CSV\plotly version semifinal-prueba copy 6.csv')
fig = go.Figure()

fig.add_trace(go.Sunburst(
    ids=df1.ids,
    labels=df1.labels,
    parents=df1.parents,
    domain=dict(column=0)
))


fig.update_layout(
    grid= dict(columns=1, rows=1),
    margin = dict(t=0, l=0, r=0, b=0)
)

fig.show()