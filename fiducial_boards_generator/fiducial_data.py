import sys
import cv2
import yaml
import numpy as np

# ARUCO_DICT = {
#     "DICT_4X4_50": cv2.aruco.DICT_4X4_50,
#     "DICT_4X4_100": cv2.aruco.DICT_4X4_100,
#     "DICT_4X4_250": cv2.aruco.DICT_4X4_250,
#     "DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
#     "DICT_5X5_50": cv2.aruco.DICT_5X5_50,
#     "DICT_5X5_100": cv2.aruco.DICT_5X5_100,
#     "DICT_5X5_250": cv2.aruco.DICT_5X5_250,
#     "DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
#     "DICT_6X6_50": cv2.aruco.DICT_6X6_50,
#     "DICT_6X6_100": cv2.aruco.DICT_6X6_100,
#     "DICT_6X6_250": cv2.aruco.DICT_6X6_250,
#     "DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
#     "DICT_7X7_50": cv2.aruco.DICT_7X7_50,
#     "DICT_7X7_100": cv2.aruco.DICT_7X7_100,
#     "DICT_7X7_250": cv2.aruco.DICT_7X7_250,
#     "DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
#     "DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
#     "DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
#     "DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
#     "DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
#     "DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
# }

def get_value(node, name):
    assert isinstance(node, yaml.MappingNode)
    for key, value in node.value:
        assert isinstance(key, yaml.ScalarNode)
        if key.value == name:
            return value

class FiducialMarkerData(yaml.YAMLObject):
    yaml_tag = u'!ENV'
    
    def __init__(self, id, type, p1, p2, p3, p4) -> None:
        self.id = id 
        self.type = type 
        self.p1 = p1 #np.array(p1, dtype=np.float32) 
        self.p2 = p2 #np.array(p1, dtype=np.float32)
        self.p3 = p3 #np.array(p2, dtype=np.float32)
        self.p4 = p4 #np.array(p3, dtype=np.float32)
   
        
    @classmethod
    def from_yaml(cls, loader, node):
        id = int(get_value(node, "id").value)
        type = get_value(node, "type").value
        p1 = [float(get_value(node, "p1").value[0].value), float(get_value(node, "p1").value[1].value), float(get_value(node, "p1").value[2].value)]
        p2 = [float(get_value(node, "p2").value[0].value), float(get_value(node, "p2").value[1].value), float(get_value(node, "p2").value[2].value)]
        p3 = [float(get_value(node, "p3").value[0].value), float(get_value(node, "p3").value[1].value), float(get_value(node, "p3").value[2].value)]
        p4 = [float(get_value(node, "p4").value[0].value), float(get_value(node, "p4").value[1].value), float(get_value(node, "p4").value[2].value)]
        return FiducialMarkerData(id, type, p1, p2, p3, p4)

class CustomGridBoard:
    def __init__(self, ids, objPoints) -> None:
        # self.dictionary = dictionary
        # self.objPoints = objPoints
        # self.ids = ids
        self.corners = {ids[i]: objPoints[i] for i in range(len(ids))}
        
    def get_objPoints(self, ids, img_points):
        corners_list = []
        img_points_detected =[]
        for i in range (len(ids)):
            corners = self.corners.get(ids[i][0])
            if corners is not None:
                for j in range(4):
                    corners_list.append(corners[j])
                    img_points_detected.append(img_points[i][0][j])
        return corners_list, img_points_detected
        

class FiducialBoard:
    def __init__(self, filename="board") -> None:
        self._fiducial_list = []
        self._filename = filename
        # yaml.add_constructor("!!python/object:fiducial_data.FiducialMarkerData", FiducialMarkerData.from_yaml)
        yaml.SafeLoader.add_constructor('!ENV', FiducialMarkerData.from_yaml)
        # Required for safe_dump
        # yaml.SafeDumper.add_multi_representer(FiducialMarkerData, FiducialMarkerData.to_yaml)
        
    def add_fiducial(self, fiducial) -> None:
        self._fiducial_list.append(fiducial)
    
    def write_data(self):
        with open(self._filename+".yaml", "w") as f:
            for fiducial in self._fiducial_list:
                yaml.dump([fiducial], f)
                
    def show_marker_data(self):
        for fiducial in self.fiducial_list:
            yaml.dump([fiducial], sys.stdout)
            
    def read_data(self, filename="board.yaml"):
        with open(filename, "r") as f:
            self._fiducial_list = yaml.safe_load(f)
            
    def get_board(self):
        ids = []
        objPoints = []
        for fiducial in self._fiducial_list:
            corners = np.array([fiducial.p1, fiducial.p2,
                                fiducial.p3, fiducial.p4], dtype=np.float32)
            objPoints.append(corners)
            ids.append(fiducial.id)
        
        return CustomGridBoard(ids, objPoints)