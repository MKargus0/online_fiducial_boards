# from pickletools import uint8
import cv2
import numpy as np
from .fiducial_data import ARUCO_DICT, FiducialMarkerData, FiducialBoard

class CustomFieldCreator:
    def __init__(self, size_x, size_y, pixel_density=1000) -> None:
        self.pixel_density = pixel_density
        self.image = np.full((int(size_x*pixel_density), int(size_y*pixel_density)), 255, dtype=np.uint8)
        self.fiducialBoard = FiducialBoard("board")


    def add_marker(self, pose_x, pose_y, size, id, dict_type ="DICT_4X4_100") -> None:
        arucoDict = cv2.aruco.getPredefinedDictionary(ARUCO_DICT[dict_type])

        pixel_size = int(self.pixel_density * size)
        marker_img = cv2.aruco.generateImageMarker(arucoDict, id, pixel_size)

        marker = self._create_fiducial(pose_x, pose_y, size, id, dict_type)
        self.fiducialBoard.add_fiducial(marker)

        pixel_x = int((self.pixel_density * pose_x) + int(self.image.shape[0]/2))
        pixel_y = -int((self.pixel_density * pose_y) + int(self.image.shape[1]/2))
        self.image = self._pasteImage(self.image, marker_img, pixel_x, pixel_y)
        # cv2.imshow("marker", marker_img)
        # cv2.waitKey(0)
        # FiducialMarkerData()

    def show_image(self) -> None:
        cv2.imshow("board", self.image)
        cv2.waitKey(0)

    def save_data(self) -> None:
        cv2.imwrite("board.png", self.image)
        self.fiducialBoard.write_data()

    def _create_fiducial(self, pose_x, pose_y, size, id, type):
        id = id
        type = type
        p1 = [-size/2, size/2, 0]
        p2 = [size/2, size/2, 0]
        p3 = [size/2, -size/2, 0]
        p4 = [-size/2, -size/2, 0]

        p1[0] += pose_x
        p2[0] += pose_x
        p3[0] += pose_x
        p4[0] += pose_x

        p1[1] += pose_y
        p2[1] += pose_y
        p3[1] += pose_y
        p4[1] += pose_y
        return FiducialMarkerData(id, type, p1, p2, p3, p4)


    def _pasteImage(self, img1, img2, px, py):
        pip_w = px-int(img2.shape[0]/2)
        pip_h = py-int(img2.shape[1]/2)
        img1[pip_h:pip_h+img2.shape[0],pip_w:pip_w+img2.shape[1]] = img2
        return img1


