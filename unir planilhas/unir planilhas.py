import io
import os
from pathlib import Path
import pandas as pd
from Tools.scripts.dutree import display

vendas = pd.DataFrame(columns=['Loja', 'Vendedor','Valor da Venda'])

caminho = Path.cwd()
print(caminho)
for pasta in caminho.iterdir():
    if pasta.is_dir():
        os.chdir(pasta)
        caminho = Path.cwd()
        for pasta in caminho.iterdir():
            if pasta.is_dir():
                os.chdir(pasta)
                caminho = Path.cwd()
                for pasta in caminho.iterdir():
                    if pasta.is_dir():
                        os.chdir(pasta)
                        caminho = Path.cwd()
                        for pasta in caminho.iterdir():
                            if pasta.is_dir():
                                os.chdir(pasta)
                                caminho = Path.cwd()
                                for arquivo in caminho.iterdir():
                                    venda = pd.read_excel(arquivo)
                                    vendas = pd.concat([vendas, venda], axis=0, ignore_index=True)
vendas_agregado = vendas.groupby(by='Loja').sum()
del vendas_agregado['Vendedor']
os.chdir(r'C:\Users\SAMAE\Documents\CURSOS\Python-Hashtag\comandos-uteis\unir planilhas\Vendas')
vendas_agregado.to_excel('vendas por Loja.xlsx')







# entender quais são as tarefas a serem feitas
# onde estão os arquivos
# Entrar nas pastas
# coletar a informacao da pasta
# juntar toda a informacao