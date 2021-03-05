#Leitura basica de dataframe usando Pandas

from IPython.display import display
import pandas as pd

df = pd.read_excel(r'Vendas.xlsx')

fatura_qtd = df[['ID Loja', 'Valor Final', 'Quantidade']].groupby('ID Loja').sum().sort_values(by = 'Valor Final', ascending = False)

ticket_medio = (fatura_qtd['Valor Final'] / fatura_qtd['Quantidade']).to_frame().sort_values(by = 0, ascending = False).rename(columns = {0:'Ticket Medio'})

ticket_medio.to_excel('Vendas Ticket_medios.xlsx', encoding = 'utf-8', index = True)
