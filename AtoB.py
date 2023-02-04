from arm_modules_modifi.arm import InterbotixManipulatorXS
from board_2_pose import pose_H, pose_L, out_H, out_L

bot = InterbotixManipulatorXS('rx150', 'arm', 'gripper')

# Capture: False


def AtoB(squ_A, squ_B):
    squ_A = squ_A.upper()
    squ_B = squ_B.upper()

    x1_H, y1_H, z1_H, pitch1_H = pose_H.get(squ_A)
    *xy, z1_L,  pitch1_L = pose_L.get(squ_A)

    x2_H, y2_H, z2_H, pitch2_H = pose_H.get(squ_B)
    *xy, z2_L,  pitch2_L = pose_L.get(squ_B)

    # Square 1
    bot.arm.set_ee_pose_components(
        x=x1_H*0.01, y=y1_H*0.01, z=z1_H, pitch=pitch1_H)
    bot.arm.set_ee_cartesian_trajectory(
        z=-(z1_H-z1_L), pitch=+ (pitch1_L - pitch1_H))
    bot.gripper.close()
    bot.arm.set_ee_cartesian_trajectory(
        z=z1_H-z1_L, pitch=- (pitch1_L - pitch1_H))
    # End Square 1

    # Square 2
    bot.arm.set_ee_pose_components(
        x=x2_H*0.01, y=y2_H*0.01, z=z2_H, pitch=pitch2_H)
    bot.arm.set_ee_cartesian_trajectory(
        z=-(z2_H-z2_L), pitch=+ (pitch2_L - pitch2_H))
    bot.gripper.open()
    bot.arm.set_ee_cartesian_trajectory(
        z=z2_H-z2_L, pitch=- (pitch2_L - pitch2_H))
    # End Square 2

    bot.arm.go_to_home_pose()
    # bot.arm.got_to_rest_pose() (thay the home pose)


# Captrue: True
def AtoB_capture(squ_A, squ_B, grave):
    squ_B = squ_B.upper()

    x1_H, y1_H, z1_H, pitch1_H = pose_H.get(squ_B)
    *xy, z1_L,  pitch1_L = pose_L.get(squ_B)

    x2_H, y2_H, z2_H, pitch2_H = out_H.get(grave)
    *xy, z2_L,  pitch2_L = out_L.get(grave)

    # Square 1
    bot.arm.set_ee_pose_components(
        x=x1_H*0.01, y=y1_H*0.01, z=z1_H, pitch=pitch1_H)
    bot.arm.set_ee_cartesian_trajectory(
        z=-(z1_H-z1_L), pitch=+ (pitch1_L - pitch1_H))
    bot.gripper.close()
    bot.arm.set_ee_cartesian_trajectory(
        z=z1_H-z1_L, pitch=- (pitch1_L - pitch1_H))
    # End Square 1

    # Square 2
    bot.arm.set_ee_pose_components(
        x=x2_H*0.01, y=y2_H*0.01, z=z2_H, pitch=pitch2_H)
    bot.arm.set_ee_cartesian_trajectory(
        z=-(z2_H-z2_L), pitch=+ (pitch2_L - pitch2_H))
    bot.gripper.open()
    bot.arm.set_ee_cartesian_trajectory(
        z=z2_H-z2_L, pitch=- (pitch2_L - pitch2_H))
    # End Square 2

    AtoB(squ_A, squ_B)
