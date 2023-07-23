from fiducial_boards_generator.custom_field_gen import CustomFieldCreator

board = CustomFieldCreator(0.8, 0.8, 700)

size = 0.25
board.add_marker(0.21, 0.21, size, 0)
board.add_marker(-0.21, 0.21, size, 1)
board.add_marker(0.21, -0.21, size, 2)
board.add_marker(-0.21, -0.21, size, 3)

size = 0.12
board.add_marker(0, 0, size, 4)

size = 0.09
board.add_marker(0.22, 0, size, 5)
board.add_marker(-0.22, 0, size, 6)
board.add_marker(0, 0.22, size, 7)
board.add_marker(0, -0.22, size, 8)

size = 0.05
board.add_marker(0.35, 0, size, 9)
board.add_marker(-0.35, 0, size, 10)
board.add_marker(0, 0.35, size, 11)
board.add_marker(0, -0.35, size, 12)

board.add_marker(0.12, 0, size, 13)
board.add_marker(-0.12, 0, size, 14)
board.add_marker(0, 0.12, size, 15)
board.add_marker(0, -0.12, size, 16)


board.show_image()
board.save_data()