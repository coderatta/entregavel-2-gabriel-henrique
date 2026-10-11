import os
from arquivos import ler_arquivo
from modelos import ImagemAnotada


def main():
    os.makedirs("resultados", exist_ok=True)
    boxes_per_img = ler_arquivo("dados/anotacoes.csv")
    for img_name, boxes in boxes_per_img.items():
        img = ImagemAnotada(img_name, boxes)
        if not img.adicionar_deteccao():
            break


if __name__ == "__main__":
    main()
