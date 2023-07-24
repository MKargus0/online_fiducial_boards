import cv2
import os

from .original_board import OriginalBoard, OriginalParamsContainer

class BoardsGenerator:
    def __init__(self, static_folder_abs, static_folder_rel) -> None:
        self.static_folder_abs = static_folder_abs
        self.static_folder_rel = static_folder_rel
        
        self.original = OriginalBoard()

    def save_image(self, img):
        img_name = "original_image.jpeg"
        image_path = os.path.join(self.static_folder_abs, img_name)
        cv2.imwrite(image_path, img)

        return os.path.join(self.static_folder_rel, img_name)

    def generate_original(self, data):
        params = OriginalParamsContainer(data)
        img = self.original.generate_board(params)

        return self.save_image(img)

    # def generate_serpinski(self, library : str, N : int, M : int):
    #     pass

    # def generate_original(self, library : str, N : int, M : int):
    #     pass