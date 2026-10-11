import cv2

# cores das boxes
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
            img = cv2.putText(
                img, "Classe 0", (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, blue, 2
            )
            img = cv2.putText(
                img, "Classe 1", (40, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, green, 2
            )
            cv2.imshow(self.img_name, img)
            cv2.imwrite(f"resultados/{self.img_name}", img)

            # Verifica a tecla pressionada pelo usuario
            while True:
                pressed_key = cv2.waitKey(0) & 0xFF
                if pressed_key == ord("q"):  # tecla q
                    cv2.destroyAllWindows()
                    return False
                if pressed_key == 32:  # tecla espaco
                    break

            cv2.destroyAllWindows()
        return True
