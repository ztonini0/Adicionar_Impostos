import pandas as pd

def adicionar_imposto(preco):
    return preco * 1.1


tabela = pd.read_excel("Base Vendas.xlsx")
tabela["Preco Imposto"] = list(map(adicionar_imposto, tabela['Preco Unitario']))
print(tabela)
