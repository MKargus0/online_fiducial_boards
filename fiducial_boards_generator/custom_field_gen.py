# from pickletools import uint8
import cv2
import numpy as np

from .fiducial_data import FiducialData, FiducialBoard, Point3D 
from .fiducial_library import FiducialLibrary

class CustomFieldCreator:
    def __init__(self, size_x : float, size_y : float,
                 pixel_density : int = 1000) -> None:
        self.pixel_density = pixel_density
        self.image = np.full((int(size_x * pixel_density),
                              int(size_y * pixel_density)),
                              255, dtype=np.uint8)
        self.fiducialBoard = FiducialBoard()


    def add_marker(self, pose_x : float, pose_y : float, size : float, id : int,
                   yaw : float = 0, dict_type : str = "DICT_4X4_1000") -> None:
        
        arucoDict = FiducialLibrary.get_dictionary(dict_type)

        pixel_size = int(self.pixel_density * size)
        marker_img = cv2.aruco.generateImageMarker(arucoDict, id, pixel_size)

        marker = self._create_fiducial(pose_x, pose_y, size, id, dict_type)
        self.fiducialBoard.add_fiducial(marker)

        pixel_x = int((self.pixel_density * pose_x) + int(self.image.shape[0] / 2))
        pixel_y = -int((self.pixel_density * pose_y) + int(self.image.shape[1] / 2))
        yaw = np.deg2rad(yaw)
        self.image = self._pasteImage(self.image, marker_img, pixel_x, pixel_y, yaw)
        # cv2.imshow("marker", marker_img)
        # cv2.waitKey(0)
        # FiducialMarkerData()

    def show_image(self) -> None:
        cv2.imshow("board", self.image)
        cv2.waitKey(0)

    def save_data(self, filename : str = "") -> None:
        cv2.imwrite("board.png", self.image)
        self.fiducialBoard.write_to_file()

    def _create_fiducial(self, pose_x : float, pose_y : float, size : float, id : int, type : str):
        id = id
        type = type
        p1 = Point3D(-size / 2, size / 2, 0)
        p2 = Point3D(size / 2, size / 2, 0)
        p3 = Point3D(size / 2, -size / 2, 0)
        p4 = Point3D(-size / 2, -size / 2, 0)

        p1.x += pose_x
        p2.x += pose_x
        p3.x += pose_x
        p4.x += pose_x

        p1.y += pose_y
        p2.y += pose_y
        p3.y += pose_y
        p4.y += pose_y
        
        return FiducialData(id, type, (p1, p2, p3, p4))


    def _pasteImage(self, board_image, marker_image, px : int, py : int, angle : float, scale : float = 1):
        (h, w) = marker_image.shape[:2]
        center = (w / 2, h / 2)
        M = cv2.getRotationMatrix2D(center, np.rad2deg(angle), scale)
        cos = np.abs(M[0, 0])
        sin = np.abs(M[0, 1])
        new_w = int(np.ceil((h * sin) + (w * cos)))
        new_h = int(np.ceil((h * cos) + (w * sin)))
        # calculate new translation
        M[0, 2] += (new_w / 2) - center[0]
        M[1, 2] += (new_h / 2) - center[1]
        
        # get pixel pose for marker in board
        pip_w = px - int(new_w / 2)
        pip_h = py - int(new_h / 2)
        
        # rotate image
        # TODO: MKargus0 - add transparent borders
        rotated_marker = cv2.warpAffine(src=marker_image,
                                         M=M, dsize=(new_w, new_h), borderValue=(255,255,255),
                                         flags=cv2.WARP_FILL_OUTLIERS)

        # insert rotated image to board
        board_image[pip_h:pip_h+rotated_marker.shape[0],pip_w:pip_w+rotated_marker.shape[1]] = rotated_marker
        

        return board_image


