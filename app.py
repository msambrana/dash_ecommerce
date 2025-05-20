import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Leitura do arquivo CSV
df = pd.read_csv("ecommerce_estatistica (1).csv")

# Criação dos gráficos
fig1 = px.histogram(df, x="Quantidade", title="Distribuição de Quantidade de Produtos")
fig2 = px.box(df, y="ValorVenda", title="Boxplot do Valor de Venda")
fig3 = px.scatter(df, x="Quantidade", y="ValorVenda", color="Categoria", 
                  title="Quantidade vs Valor de Venda por Categoria")

# Criação da aplicação Dash
app = Dash(__name__)
app.title = "Dashboard E-commerce"

app.layout = html.Div(children=[
    html.H1("Dashboard de Estatísticas do E-commerce", style={'textAlign': 'center'}),

    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2),
    dcc.Graph(figure=fig3)
])

# Executar o servidor localmente
if __name__ == '__main__':
    app.run_server(debug=True)
