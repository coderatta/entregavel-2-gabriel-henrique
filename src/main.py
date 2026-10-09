import cv2
from arquivos import boxes_per_img
from modelos import ImagemAnotada

for img_name, boxes in boxes_per_img.items():
    img = ImagemAnotada(img_name, boxes)
    img.adicionar_deteccao()

cv2.destroyAllWindows()
