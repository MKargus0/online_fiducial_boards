import sys
import cv2
import yaml
import numpy as np


# def get_value(node, name):
#     assert isinstance(node, yaml.MappingNode)
#     for key, value in node.value:
#         assert isinstance(key, yaml.ScalarNode)
#         if key.value == name:
#             return value

class Point3D:
    def __init__(self, x : float = 0, y : float = 0, z : float = 0):
        self.x = x
        self.y = y
        self.z = z

class FiducialData:
    def __init__(self, id : int, type : str, corners : tuple[Point3D]) -> None:
        self.id = id
        self.type = type
        self.corners = corners #np.array(p1, dtype=np.float32) 


def point3d_representer(dumper, data):
    return dumper.represent_dict({'x': data.x, 'y': data.y, 'z': data.z})


def fiducial_data_representer(dumper, data):
    return dumper.represent_dict({'corners': data.corners, 'id': data.id, 'type': data.type})


def point3d_constructor(loader, node):
    values = loader.construct_mapping(node)
    return Point3D(**values)


def fiducial_data_constructor(loader, node):
    values = loader.construct_mapping(node)
    return FiducialData(**values)


yaml.add_representer(Point3D, point3d_representer)
yaml.add_representer(FiducialData, fiducial_data_representer)
yaml.add_constructor('!Point3D', point3d_constructor)
yaml.add_constructor('!FiducialData', fiducial_data_constructor)



    # @classmethod
    # def from_yaml(cls, loader, node):
    #     id = int(get_value(node, "id").value)
    #     type = get_value(node, "type").value
    #     p1 = [float(get_value(node, "p1").value[0].value), float(get_value(node, "p1").value[1].value), float(get_value(node, "p1").value[2].value)]
    #     p2 = [float(get_value(node, "p2").value[0].value), float(get_value(node, "p2").value[1].value), float(get_value(node, "p2").value[2].value)]
    #     p3 = [float(get_value(node, "p3").value[0].value), float(get_value(node, "p3").value[1].value), float(get_value(node, "p3").value[2].value)]
    #     p4 = [float(get_value(node, "p4").value[0].value), float(get_value(node, "p4").value[1].value), float(get_value(node, "p4").value[2].value)]
    #     return FiducialMarkerData(id, type, p1, p2, p3, p4)

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
    def __init__(self) -> None:
        self._fiducial_list = []
        
    def add_fiducial(self, fiducial) -> None:
        self._fiducial_list.append(fiducial)
    
    # Serialization
    def write_to_file(self, filename="board.yaml"):
        with open(filename, "w") as f:
            # for fiducial in self._fiducial_list:
            yaml.dump(self._fiducial_list, f)
                
    # Deserialization        
    def read_data(self, filename="board.yaml"):
        with open(filename, "r") as f:
            self._fiducial_list = yaml.safe_load(f)
            
    def show_marker_data(self):
        yaml.dump(self._fiducial_list, sys.stdout)
    
    
    def get_board(self):
        ids = []
        objPoints = []
        for fiducial in self._fiducial_list:
            corners = np.array([fiducial.p1, fiducial.p2,
                                fiducial.p3, fiducial.p4], dtype=np.float32)
            objPoints.append(corners)
            ids.append(fiducial.id)
        
        return CustomGridBoard(ids, objPoints)