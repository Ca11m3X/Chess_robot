# Lấy data trong all24_H2.txt
# "Name_square": (x,y,z,pitch)

# Bị Ngược
# chess_board_to_robot_pose_H = {
#     "A1": (13.5, 10.5, 0.15, 1.56),
#     "B1": (13.5, 7.5, 0.15, 1.56),
#     "C1": (13.5, 4.5, 0.15, 1.56),
#     "D1": (13.5, 1.5, 0.15, 1.56),
#     "E1": (13.5, -1.5, 0.15, 1.56),
#     "F1": (13.5, -4.5, 0.15, 1.56),
#     "G1": (13.5, -7.5, 0.15, 1.56),
#     "H1": (13.5, -10.5, 0.15, 1.56),
#     "A2": (16.5, 10.5, 0.15, 1.56),
#     "B2": (16.5, 7.5, 0.15, 1.56),
#     "C2": (16.5, 4.5, 0.15, 1.56),
#     "D2": (16.5, 1.5, 0.15, 1.56),
#     "E2": (16.5, -1.5, 0.15, 1.56),
#     "F2": (16.5, -4.5, 0.15, 1.56),
#     "G2": (16.5, -7.5, 0.15, 1.56),
#     "H2": (16.5, -10.5, 0.15, 1.56),
#     "A3": (19.5, 10.5, 0.15, 1.56),
#     "B3": (19.5, 7.5, 0.15, 1.56),
#     "C3": (19.5, 4.5, 0.15, 1.56),
#     "D3": (19.5, 1.5, 0.15, 1.56),
#     "E3": (19.5, -1.5, 0.15, 1.56),
#     "F3": (19.5, -4.5, 0.15, 1.56),
#     "G3": (19.5, -7.5, 0.15, 1.56),
#     "H3": (19.5, -10.5, 0.15, 1.56),
#     "A4": (22.5, 10.5, 0.15, 1.46),
#     "B4": (22.5, 7.5, 0.15, 1.51),
#     "C4": (22.5, 4.5, 0.15, 1.54),
#     "D4": (22.5, 1.5, 0.15, 1.56),
#     "E4": (22.5, -1.5, 0.15, 1.56),
#     "F4": (22.5, -4.5, 0.15, 1.54),
#     "G4": (22.5, -7.5, 0.15, 1.51),
#     "H4": (22.5, -10.5, 0.15, 1.46),
#     "A5": (25.5, 10.5, 0.12, 1.43),
#     "B5": (25.5, 7.5, 0.12, 1.49),
#     "C5": (25.5, 4.5, 0.12, 1.53),
#     "D5": (25.5, 1.5, 0.12, 1.55),
#     "E5": (25.5, -1.5, 0.12, 1.55),
#     "F5": (25.5, -4.5, 0.12, 1.53),
#     "G5": (25.5, -7.5, 0.12, 1.49),
#     "H5": (25.5, -10.5, 0.12, 1.43),
#     "A6": (28.5, 10.5, 0.12, 1.27),
#     "B6": (28.5, 7.5, 0.12, 1.32),
#     "C6": (28.5, 4.5, 0.12, 1.36),
#     "D6": (28.5, 1.5, 0.12, 1.38),
#     "E6": (28.5, -1.5, 0.12, 1.38),
#     "F6": (28.5, -4.5, 0.12, 1.36),
#     "G6": (28.5, -7.5, 0.12, 1.32),
#     "H6": (28.5, -10.5, 0.12, 1.27),
#     "A7": (31.5, 10.5, 0.1, 1.18),
#     "B7": (31.5, 7.5, 0.1, 1.23),
#     "C7": (31.5, 4.5, 0.1, 1.26),
#     "D7": (31.5, 1.5, 0.1, 1.28),
#     "E7": (31.5, -1.5, 0.1, 1.28),
#     "F7": (31.5, -4.5, 0.1, 1.26),
#     "G7": (31.5, -7.5, 0.1, 1.23),
#     "H7": (31.5, -10.5, 0.1, 1.18),
#     "A8": (34.5, 10.5, 0.1, 1.02),
#     "B8": (34.5, 7.5, 0.1, 1.06),
#     "C8": (34.5, 4.5, 0.1, 1.09),
#     "D8": (34.5, 1.5, 0.1, 1.11),
#     "E8": (34.5, -1.5, 0.1, 1.11),
#     "F8": (34.5, -4.5, 0.1, 1.09),
#     "G8": (34.5, -7.5, 0.1, 1.06),
#     "H8": (34.5, -10.5, 0.1, 1.02),

# }

chess_board_to_robot_pose_H = {
    "H8": (13.5, 10.5, 0.15, 1.56),
    "G8": (13.5, 7.5, 0.15, 1.56),
    "F8": (13.5, 4.5, 0.15, 1.56),
    "E8": (13.5, 1.5, 0.15, 1.56),
    "D8": (13.5, -1.5, 0.15, 1.56),
    "C8": (13.5, -4.5, 0.15, 1.56),
    "B8": (13.5, -7.5, 0.15, 1.56),
    "A8": (13.5, -10.5, 0.15, 1.56),
    "H7": (16.5, 10.5, 0.15, 1.56),
    "G7": (16.5, 7.5, 0.15, 1.56),
    "F7": (16.5, 4.5, 0.15, 1.56),
    "E7": (16.5, 1.5, 0.15, 1.56),
    "D7": (16.5, -1.5, 0.15, 1.56),
    "C7": (16.5, -4.5, 0.15, 1.56),
    "B7": (16.5, -7.5, 0.15, 1.56),
    "A7": (16.5, -10.5, 0.15, 1.56),
    "H6": (19.5, 10.5, 0.15, 1.56),
    "G6": (19.5, 7.5, 0.15, 1.56),
    "F6": (19.5, 4.5, 0.15, 1.56),
    "E6": (19.5, 1.5, 0.15, 1.56),
    "D6": (19.5, -1.5, 0.15, 1.56),
    "C6": (19.5, -4.5, 0.15, 1.56),
    "B6": (19.5, -7.5, 0.15, 1.56),
    "A6": (19.5, -10.5, 0.15, 1.56),
    "H5": (22.5, 10.5, 0.15, 1.46),
    "G5": (22.5, 7.5, 0.15, 1.51),
    "F5": (22.5, 4.5, 0.15, 1.54),
    "E5": (22.5, 1.5, 0.15, 1.56),
    "D5": (22.5, -1.5, 0.15, 1.56),
    "C5": (22.5, -4.5, 0.15, 1.54),
    "B5": (22.5, -7.5, 0.15, 1.51),
    "A5": (22.5, -10.5, 0.15, 1.46),
    "H4": (25.5, 10.5, 0.12, 1.43),
    "G4": (25.5, 7.5, 0.12, 1.49),
    "F4": (25.5, 4.5, 0.5, -7.5, 0.15, 1.51),
    "A5": (22.5, -10.5, 0.15, 1.46),
    "H4": (25.5, 10.5, 0.12, 1.43),
    "G4": (25.5, 7.5, 0.12, 1.49),
    "F4": (25.5, 4.5, .12, 1.53),
    "E4": (25.5, 1.5, 0.12, 1.55),
    "D4": (25.5, -1.5, 0.12, 1.55),
    "C4": (25.5, -4.5, 0.12, 1.53),
    "B4": (25.5, -7.5, 0.12, 1.49),
    "A4": (25.5, -10.5, 0.12, 1.43),
    "H3": (28.5, 10.5, 0.12, 1.27),
    "G3": (28.5, 7.5, 0.12, 1.32),
    "F3": (28.5, 4.5, 0.12, 1.36),
    "E3": (28.5, 1.5, 0.12, 1.38),
    "D3": (28.5, -1.5, 0.12, 1.38),
    "C3": (28.5, -4.5, 0.12, 1.36),
    "B3": (28.5, -7.5, 0.12, 1.32),
    "A3": (28.5, -10.5, 0.12, 1.27),
    "H2": (31.5, 10.5, 0.1, 1.18),
    "G2": (31.5, 7.5, 0.1, 1.23),
    "F2": (31.5, 4.5, 0.1, 1.26),
    "E2": (31.5, 1.5, 0.1, 1.28),
    "D2": (31.5, -1.5, 0.1, 1.28),
    "C2": (31.5, -4.5, 0.1, 1.26),
    "B2": (31.5, -7.5, 0.1, 1.23),
    "A2": (31.5, -10.5, 0.1, 1.18),
    "H1": (34.5, 10.5, 0.1, 1.02),
    "G1": (34.5, 7.5, 0.1, 1.06),
    "F1": (34.5, 4.5, 0.1, 1.09),
    "E1": (34.5, 1.5, 0.1, 1.11),
    "D1": (34.5, -1.5, 0.1, 1.11),
    "C1": (34.5, -4.5, 0.1, 1.09),
    "B1": (34.5, -7.5, 0.1, 1.06),
    "A1": (34.5, -10.5, 0.1, 1.02),

}


def get(name_square):
    return chess_board_to_robot_pose_H[name_square]


# file = open('/home/drx/Chess_robot/board_2_pose/poseH_out', 'w')

# for a in range(1, 9, 1):
#     for b in list('ABCDEFGH'):
#         x, y, z, pitch = get(b+str(a))
#         pitch = round(pitch, 2) - 0.01
#         file.write(f'"{b}{str(a)}": ({x},{y},{z},{pitch}),' + "\n")
# file.close()
