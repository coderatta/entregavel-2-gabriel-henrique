import csv
import cv2

green = (0, 255, 0)
blue = (255, 0, 0)


class Deteccao:
    def __init__(self, classe_id: int, x_min: int, y_min: int, x_max: int, y_max: int):
        self.classe_id = classe_id
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

    def desenhar(self, img):
        if self.classe_id == 0:
            cv2.rectangle(
                img, (self.x_min, self.y_min), (self.x_max, self.y_max), blue, 2
            )
        else:
            cv2.rectangle(
                img, (self.x_min, self.y_min), (self.x_max, self.y_max), green, 2
            )


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
        if img_name not in boxes_per_img:
            boxes_per_img[img_name] = []
        boxes_per_img[img_name].append(img_box)

for img_name, boxes in boxes_per_img.items():
    img = cv2.imread(f"imagens/{img_name}")

    if img is None:
        print("Erro ao carregar imagem")
    else:
        for box in boxes:
            box.desenhar(img)

        cv2.imshow("Imagem Anotada", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# class ImagemAnotada:
#     def __init__(self, caminho_imagem, lista_deteccoes):
#         self.caminho_imagem = caminho_imagem
#         self.lista_deteccoes = lista_deteccoes

#     def AdicionarDeteccao(self, deteccao):
#         return
