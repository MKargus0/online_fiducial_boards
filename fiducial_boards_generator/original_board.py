import cv2
from .fiducial_library import FiducialLibrary, DictSizeOverflow


class OriginalParamsContainer:
    def __init__(self, data):
        # Process the data and store it in instance variables
        self.marker_library = data.get('select_dict')
        self.n = int(data.get('n_input'))
        self.m = int(data.get('m_input'))
        self.length = float(data.get('length'))
        self.separation = float(data.get('separation'))
        self.pixel_per_meter = float(data.get('board_resolution'))
        self.margin_size = int(data.get('board_margin_size'))
        self.border_bit = int(data.get('border_bit'))
       

class OriginalBoard:
    def __init__(self) -> None:
        pass

    def check_input(self, params : OriginalParamsContainer):
        fiducial_count = params.n * params.m
        if not FiducialLibrary.check_dictionary(fiducial_count, params.marker_library):
            raise DictSizeOverflow("Dictionary size too big, choose another one:", params.marker_library)


    def generate_board(self, params : OriginalParamsContainer):

        self.check_input(params)
    
        dict = FiducialLibrary.get_dictionary(params.marker_library)

        board = cv2.aruco.GridBoard([params.n, params.m], params.length, params.separation, dict)
        
        board_width = (params.n * params.length + (params.n - 1) * params.separation) * params.pixel_per_meter
        board_height = (params.m * params.length + (params.m - 1) * params.separation) * params.pixel_per_meter
        # img = board.generateImage([board_width, board_height], None
        size = (int(board_width), int(board_height))

        img = cv2.aruco.drawPlanarBoard(board, size, params.margin_size, params.border_bit)
        return img
