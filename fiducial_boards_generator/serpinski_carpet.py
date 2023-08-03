from .custom_field_gen import CustomFieldCreator
from .fiducial_data import FiducialBoard


class SerpinskiParamsContainer:
    def __init__(self) -> None:
        self.node_x = 1
        self.node_y = 1
        self.max_depth = 4
        self.node_size = 1
        # self.separation = 1

class SerpinskiCarpetBoard():
    def __init__(self) -> None:
        pass        

    def generate_board(self, params : SerpinskiParamsContainer):
        
        size_x = params.node_size * params.node_x 
        size_y = params.node_size * params.node_y
        board = CustomFieldCreator(size_x + params.node_size * 2,
                                   size_y + params.node_size * 2, 700)
        self.cur_id = 0
        self.max_depth = params.max_depth

        pose_x = 0 #-size_x / 2
        pose_y = 0 #-size_y / 2
        for i in range(params.node_x):
            for j in range(params.node_y):
                self.addNode(pose_x=pose_x + params.node_size * i,
                             pose_y=pose_y + params.node_size * j, id=self.cur_id,
                             cur_depth=0, size=params.node_size, board=board)
                self.cur_id += 1
                
        return board

    def addNode(self, pose_x: float, pose_y : float, id : int, cur_depth : int, size : float , board : FiducialBoard):
        board.add_marker(pose_x, pose_y, size, id, yaw = 0)
        if (cur_depth+1) >= self.max_depth:
            return
        cur_depth += 1
        
        self.cur_id +=1 
        # up
        self.addNode(pose_x=pose_x, pose_y=pose_y+size, id = self.cur_id,
                     cur_depth=cur_depth, size=size / 3.0, board=board)
        self.cur_id +=1
        # down
        self.addNode(pose_x=pose_x, pose_y=pose_y-size, id = self.cur_id,
                     cur_depth=cur_depth, size=size / 3, board=board)
        self.cur_id +=1
        # # right
        self.addNode(pose_x=pose_x+size, pose_y=pose_y, id = self.cur_id,
                     cur_depth=cur_depth, size=size / 3, board=board)
        self.cur_id +=1
        # left
        self.addNode(pose_x=pose_x-size, pose_y=pose_y, id = self.cur_id,
                     cur_depth=cur_depth, size=size / 3, board=board)

        self.cur_id +=1
        # up - right 
        self.addNode(pose_x=pose_x+size, pose_y=pose_y+size, id = self.cur_id,
                     cur_depth=cur_depth, size=size / 3, board=board)
        self.cur_id +=1
        # up - left
        self.addNode(pose_x=pose_x-size, pose_y=pose_y+size, id = self.cur_id,
                     cur_depth=cur_depth, size=size / 3, board=board)
        self.cur_id +=1
        # down - right 
        self.addNode(pose_x=pose_x+size, pose_y=pose_y-size, id = self.cur_id,
                     cur_depth=cur_depth, size=size / 3, board=board)
        self.cur_id +=1
        # down - left
        self.addNode(pose_x=pose_x-size, pose_y=pose_y-size, id = self.cur_id,
                     cur_depth=cur_depth, size=size / 3, board=board)
        
