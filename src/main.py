from arquivos import boxes_per_img
from modelos import ImagemAnotada


def main():
    for img_name, boxes in boxes_per_img.items():
        img = ImagemAnotada(img_name, boxes)
        if not img.adicionar_deteccao():
            break
