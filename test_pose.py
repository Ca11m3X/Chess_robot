from interbotix_xs_modules.arm import InterbotixManipulatorXS
import time


def get_chess_square_info(move, number):
    characters = "ABCDEFGH"

    character = characters[move]

    return f'{character}{number}'


chess_info = {
    "A5": (25.5, 10.5, 0.03, 1.56),
    "B5": (25.5, 7.5, 0.03, 1.56),
    "C5": (25.5, 4.5, 0.03, 1.56),
    "D5": (25.5, 1.5, 0.03, 1.56),
    "E5": (25.5, -1.5, 0.03, 1.56),
    "F5": (25.5, -4.5, 0.03, 1.56),
    "G5": (25.5, -7.5, 0.03, 1.56),
    "H5": (25.5, -10.5, 0.03, 1.56),
    "A6": (28.5, 10.5, 0.03, 1.52),
    "B6": (28.5, 7.5, 0.03, 1.56),
    "C6": (28.5, 4.5, 0.03, 1.56),
    "D6": (28.5, 1.5, 0.03, 1.52),
    "E6": (28.5, -1.5, 0.03, 1.52),
    "F6": (28.5, -4.5, 0.03, 1.56),
    "G6": (28.5, -7.5, 0.03, 1.56),
    "H6": (28.5, -10.5, 0.03, 1.52),
    "A7": (31.5, 10.5, 0.03, 1.34),
    "B7": (31.5, 7.5, 0.03, 1.39),
    "C7": (31.5, 4.5, 0.03, 1.43),
    "D7": (31.5, 1.5, 0.03, 1.44),
    "E7": (31.5, -1.5, 0.03, 1.44),
    "F7": (31.5, -4.5, 0.03, 1.43),
    "G7": (31.5, -7.5, 0.03, 1.39),
    "H7": (31.5, -10.5, 0.03, 1.34),
    "A8": (34.5, 10.5, 0.03, 1.17),
    "B8": (34.5, 7.5, 0.03, 1.21),
    "C8": (34.5, 4.5, 0.03, 1.25),
    "D8": (34.5, 1.5, 0.03, 1.26),
    "E8": (34.5, -1.5, 0.03, 1.26),
    "F8": (34.5, -4.5, 0.03, 1.25),
    "G8": (34.5, -7.5, 0.03, 1.21),
    "H8": (34.5, -10.5, 0.03, 1.17),
}

bot = InterbotixManipulatorXS('rx150', 'arm', 'gripper')

chess_height = 3*0.01

for number in range(5, 9, 1):
    for move in range(8):
        name = get_chess_square_info(move, number)
        x, y, z, pitch = chess_info[name]
        print(name)
        bot.arm.set_ee_pose_components(x=x*0.01, y=y*0.01, z=z, pitch=pitch)
        time.sleep(3)
        print(f"End__{name}")
