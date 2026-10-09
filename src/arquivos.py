import csv
from modelos import Deteccao

# dicio pra guardar as deteccoes de cada imagem,
# a chave eh o nome da imagem
# e o valor eh uma lista de objetos Deteccao
# guardadas em memoria
boxes_per_img = {}

with open("dados/anotacoes.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        img_name: str = row[0]
        img_box = Deteccao(
            int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5])
        )
        # verifica se a imagem ja esta guardada, se nao estiver cria uma lista para vazia para ela
        if img_name not in boxes_per_img:
            boxes_per_img[img_name] = []
        # adiciona a caixa na lista de caixas da imagem
        boxes_per_img[img_name].append(img_box)
