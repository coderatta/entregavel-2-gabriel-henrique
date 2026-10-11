import csv
from modelos import Deteccao


def ler_arquivo(filepath: str) -> dict[str, list[Deteccao]]:
    boxes_per_img: dict[str, list[Deteccao]] = {}
    with open(filepath, "r") as file:
        reader = csv.reader(file)
        next(reader)  # pula a primera linha com os nomes das colunas
        for row in reader:
            img_name: str = row[0]
            img_box = Deteccao(
                int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5])
            )
            # verifica se o nome da imagem ja esta guardado,
            # se nao estiver cria uma lista para vazia para ele
            if img_name not in boxes_per_img:
                boxes_per_img[img_name] = []
            # adiciona a box na lista de boxes da imagem
            boxes_per_img[img_name].append(img_box)
    return boxes_per_img
