# File de check cac vi tri thao man voi robot
# Tuong ung voi 64 vi tri tren ban co

from interbotix_xs_modules.arm import InterbotixManipulatorXS


def float_range(start, stop, step):
    if start < stop:
        while start <= stop:
            yield start
            start += step
    else:
        while start >= stop:
            yield start
            start -= step


def get_chess_square_info(move, number):
    characters = "FABCDEFGH"

    character = characters[move]

    return f'{character}{number}'


def check_board():

    m, n, out, move, number = 0, 0, 0, 1, 1
    size = 24
    space = 12
    step = size/8
    x_high = space + step * 7.5
    x_low = space + step * 0.5
    y_high = 3.5 * step
    y_low = -(y_high)
    z = 0.03

    for x in float_range(x_low, x_high, step):
        for y in float_range(y_high, y_low, step):
            angle = 3.14/2
            while True:
                result = bot.arm.set_ee_pose_components(
                    x=x*0.01, y=y*0.01, z=z, pitch=angle, execute=False)
                array, success = result

                if success == True:
                    break

                if angle <= 0:
                    break

                angle -= 0.01

            if success:
                pos = get_chess_square_info(move, number)
                print(f"Success -- > {pos} : ({x}, {y}, {z}, {angle})")
                file1.write(f'"{pos}" : ({x}, {y}, {z}, {angle}),' + "\n")
            else:
                pos = get_chess_square_info(move, number)
                file1.write(f'"{pos}" : ({x}, {y}, {z}, 0),' + "\n")
                print(f"{pos} : ({x}, {y})")

            move += 1

        number += 1
        move = 1


if __name__ == '__main__':
    bot = InterbotixManipulatorXS('rx150', 'arm', 'gripper')
    bot.arm.go_to_home_pose()
    file1 = open('/home/drx/Chess_robot/check_board_out.txt', "w")
    check_board()
    file1.close()
    bot.arm.go_to_sleep_pose()
