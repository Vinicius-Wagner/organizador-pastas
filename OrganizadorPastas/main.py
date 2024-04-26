import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)

locais = {
    "imagens": [".png", ".jpg"],
    "planilhas": [".xlsx"],
    "pdfs": [".pdf"],
    "words": [".docx"],
    "csv": [".csv"],
    "mp3s": [".mp3"],
}

for arquivo in lista_arquivos:
    
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    #Verificando se a extensão esta dentro da lista para cada pasta
    for pasta in locais:
        if extensao in locais[pasta]:
            #Verificando se a pasta existe:
            if not os.path.exists(f"{caminho}/{pasta}"):
                #Se não existe, então cria a pasta:
                os.makedirs(f"{caminho}/{pasta}")
            #Movimentando o arquivo para a nova pasta:
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
            