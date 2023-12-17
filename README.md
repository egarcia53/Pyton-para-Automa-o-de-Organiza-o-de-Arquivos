# Script de Organização de Arquivos

## Descrição:
**Este script em Python foi desenvolvido para automatizar a organização de arquivos em uma pasta de origem, categorizando-os com base em regras pré-definidas e movendo-os para uma pasta de destino correspondente. No exemplo fornecido, os arquivos são organizados de acordo com o mês em que contêm uma determinada substring no nome.** 



## Requisitos:

- Python 3.x instalado
- Módulo Tkinter (normalmente incluído na instalação padrão do Python)
  

## Instruções de Uso:

-  Execute o script.
-  Uma janela será aberta para selecionar a "Pasta Origem". Selecione a pasta que contém os arquivos a serem organizados.
-  Uma segunda janela será aberta para selecionar a "Pasta Destino". Escolha ou crie a pasta onde os arquivos organizados serão movidos.
-  O script aplicará as regras definidas e moverá os arquivos para pastas correspondentes na "Pasta Destino".


## Regras de Organização (Exemplo):

-  Arquivos contendo "jan" no nome serão movidos para a pasta "Janeiro".
-  Arquivos contendo "fev" no nome serão movidos para a pasta "Fevereiro".
-  Arquivos contendo "mar" no nome serão movidos para a pasta "Março".
      

## Notas Adicionais:

-  Certifique-se de ter permissões adequadas para acessar, modificar e criar pastas no sistema de arquivos.
-  O script cria automaticamente as pastas de destino, se necessário.
-  As regras de organização podem ser personalizadas editando o dicionário regras_arquivos no script.
-  Foi adicionado ao repositório uma pasta com arquivos de teste.


## Exemplo de Uso:

-  Suponha que você tenha os arquivos "relatorio_jan.txt", "planilha_fev.xlsx" e "notas_mar.docx" na "Pasta Origem". Após a execução do script, esses arquivos serão movidos para as pastas "Janeiro", "Fevereiro" e "Março" na "Pasta Destino", respectivamente.


## Observações:

-  Este é um exemplo simples e pode ser personalizado conforme necessário. Certifique-se de entender o funcionamento do script antes de aplicá-lo a dados importantes.


