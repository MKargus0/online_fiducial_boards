from fiducial_boards_generator.serpinski_carpet import SerpinskiCarpetBoard, SerpinskiParamsContainer


params = SerpinskiParamsContainer()

generator = SerpinskiCarpetBoard()

board = generator.generate_board(params)

# board.show_image()
board.save_data()