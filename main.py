import os
from tkinter.filedialog import askdirectory

pasta_origem = askdirectory(title="Pasta Origem")
pasta_destino = askdirectory(title="Pasta Destino")

regras_arquivos = {
    "jan": "Janeiro",
    "fev": "Fevereiro",
    "mar": "Março",
}

lista_arquivos = os.listdir(pasta_origem)

for nome_arquivo in lista_arquivos:
    for chave in regras_arquivos.keys():
        if chave in nome_arquivo:
            nova_pasta = regras_arquivos[chave]
            nome_completo_original = os.path.join(pasta_origem, nome_arquivo)
            nome_completo_final = os.path.join(pasta_destino, nova_pasta, nome_arquivo)
            caminho_nova_pasta = os.path.join(pasta_destino, nova_pasta)
            if not os.path.exists(caminho_nova_pasta):
                os.mkdir(caminho_nova_pasta)
            os.rename(nome_completo_original, nome_completo_final)