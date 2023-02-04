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


bot = InterbotixManipulatorXS('rx150', 'arm', 'gripper')

size = 24
space = 12
step = size/8
x_low = space + step * 0.5
x_high = space + step * 3.5
y_low = step * 4.5
y_high = step * 7.5
z = 0.13
file = open('/home/drx/Chess_robot/chess_board_out.txt', 'w')

number = 1

for y in float_range(-y_low, -y_high, step):
    for x in float_range(x_low, x_high, step):
        angle = 3.14/2
        while True:
            angle = round(angle, 2)-0.01
            arr, success = bot.arm.set_ee_pose_components(
                x=x*0.01, y=y*0.01, z=z, pitch=angle, execute=False)
            if success:
                file.write(
                    f'"{number}" : ({x},{y},{z},{angle}),' + '\n')
                break
            elif angle <= 0:
                file.write(f'"{number}" : ({x},{y},{z},0),' + '\n')
                break
            angle -= 0.01
        number += 1

file.close()
