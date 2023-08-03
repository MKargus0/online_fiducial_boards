import cv2

class DictNotFoundException(Exception):
    pass

class DictSizeOverflow(Exception):
    def __init__(self, message, dict):
        super().__init__(message)
        self.dict = dict

class FiducialLibrary():
    
    @staticmethod
    def check_dictionary(marker_count: int, dict : str):
        if marker_count <= FiducialLibrary.ARUCO_DICT_SIZES[dict]:
            return True
        else:
            return False

    @staticmethod
    def get_dictionary(dict : str):
        try:
            dict_id = FiducialLibrary.ARUCO_DICT_IDS[dict]
        except KeyError:
            raise DictNotFoundException(f"Key '{dict}' does not exist in the fiducial dictionary.")
        
        return cv2.aruco.getPredefinedDictionary(dict_id)
    
    ARUCO_DICT_IDS = {
        "DICT_4X4_50": cv2.aruco.DICT_4X4_50,
        "DICT_4X4_100": cv2.aruco.DICT_4X4_100,
        "DICT_4X4_250": cv2.aruco.DICT_4X4_250,
        "DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
        "DICT_5X5_50": cv2.aruco.DICT_5X5_50,
        "DICT_5X5_100": cv2.aruco.DICT_5X5_100,
        "DICT_5X5_250": cv2.aruco.DICT_5X5_250,
        "DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
        "DICT_6X6_50": cv2.aruco.DICT_6X6_50,
        "DICT_6X6_100": cv2.aruco.DICT_6X6_100,
        "DICT_6X6_250": cv2.aruco.DICT_6X6_250,
        "DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
        "DICT_7X7_50": cv2.aruco.DICT_7X7_50,
        "DICT_7X7_100": cv2.aruco.DICT_7X7_100,
        "DICT_7X7_250": cv2.aruco.DICT_7X7_250,
        "DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
        "DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
        "DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
        "DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
        "DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
        "DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
    }

    ARUCO_DICT_SIZES = {
        "DICT_4X4_50": len(cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50).bytesList),
        "DICT_4X4_100": len(cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_100).bytesList),
        "DICT_4X4_250": len(cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250).bytesList),
        "DICT_4X4_1000": len(cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_1000).bytesList),
        "DICT_5X5_50": len(cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_50).bytesList),
        "DICT_5X5_100": len(cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_100).bytesList),
        "DICT_5X5_250": len(cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_250).bytesList),
        "DICT_5X5_1000": len(cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_1000).bytesList),
        "DICT_6X6_50": len(cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_50).bytesList),
        "DICT_6X6_100": len(cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_100).bytesList),
        "DICT_6X6_250": len(cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250).bytesList),
        "DICT_6X6_1000": len(cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_1000).bytesList),
        "DICT_7X7_50": len(cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_7X7_50).bytesList),
        "DICT_7X7_100": len(cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_7X7_100).bytesList),
        "DICT_7X7_250": len(cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_7X7_250).bytesList),
        "DICT_7X7_1000": len(cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_7X7_1000).bytesList),
        "DICT_ARUCO_ORIGINAL": len(cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL).bytesList),
        "DICT_APRILTAG_16h5": len(cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_APRILTAG_16h5).bytesList),
        "DICT_APRILTAG_25h9": len(cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_APRILTAG_25h9).bytesList),
        "DICT_APRILTAG_36h10": len(cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_APRILTAG_36h10).bytesList),
        "DICT_APRILTAG_36h11": len(cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_APRILTAG_36h11).bytesList)
    }
