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
        cor = blue if self.classe_id == 0 else green
        cv2.rectangle(img, (self.x_min, self.y_min), (self.x_max, self.y_max), cor, 1)


class ImagemAnotada:
    def __init__(self, img_name: str, boxes: list[Deteccao]):
        self.img_name = img_name
        self.boxes = boxes

    def adicionar_deteccao(self):
        img = cv2.imread(f"imagens/{self.img_name}")

        if img is None:
            print("Erro ao carregar imagem")
            return
        else:
            for box in self.boxes:
                box.desenhar(img)

            cv2.imshow("Imagem Anotada", img)
            cv2.imwrite(f"resultados/{self.img_name}", img)

            if cv2.waitKey(0) & 0xFF == ord("q"):
                return False
        return True
