import cv2
from .fiducial_library import ARUCO_DICT, DictNotFoundException

class OriginalBoard:
    def __init__(self) -> None:
        pass

    def generate_board(self, n : int, m : int, border_bits : int,
                       marker_length : float, marker_separation : float,
                       marker_resolution : int, margin_size : int,
                       marker_library : str):

        try:
            dict = ARUCO_DICT[marker_library]
        except KeyError:
            raise DictNotFoundException(f"Key '{marker_library}' does not exist in the fiducial dictionary.")

        board = cv2.aruco.GridBoard([n, m], marker_length, marker_separation, dict)
        pixel_per_metr = marker_resolution * marker_length
        board_width = (n * marker_resolution + (n - 1) * marker_separation) * pixel_per_metr
        board_height = (m * marker_resolution + (m - 1) * marker_separation) * pixel_per_metr
        # img = board.generateImage([board_width, board_height], None

        img = cv2.aruco.drawPlanarBoard(board, [board_width, board_height], margin_size, border_bits)
        cv2.imshow(img)
        cv2.waitKey(0)
