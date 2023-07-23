
from .original_board import OriginalBoard

class BoardsGenerator:
    def __init__(self, static_folder) -> None:
        self.static_folder = static_folder
        
        self.original = OriginalBoard()

    def generate_original(self, library : str, N : int, M : int):
        print("try to generate")
        # self.original.generate_board()

    # def generate_serpinski(self, library : str, N : int, M : int):
    #     pass

    # def generate_original(self, library : str, N : int, M : int):
    #     pass