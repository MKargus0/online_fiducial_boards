
class CustomParamsContainer:
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
        

