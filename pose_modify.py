from tkinter import *
from interbotix_xs_modules.arm import InterbotixManipulatorXS
from threading import Thread


def create_gui():
    # WAIST:
    waist_value = DoubleVar()

    def waist_thread(event):
        t1 = Thread(target=waist_working)
        t1.start()

    def waist_working():
        bot.arm.set_single_joint_position("waist", waist_value.get())

    waist_label = Label(root, text='Waist:')
    waist_label.grid(column=0, row=0, sticky='we')

    waist_slider = Scale(root, from_=-3.14, to=3.14, resolution=0.01, showvalue=False, orient='horizontal', command=waist_thread,
                         variable=waist_value)
    waist_slider.grid(row=0, column=1, sticky="we", padx=5, pady=5)

    waist_value_label = Label(root, textvariable=waist_value)
    waist_value_label.grid(row=0, column=2, sticky='we')

    # SHOULDER:
    shoulder_value = DoubleVar()

    def shoulder_thread(event):
        t2 = Thread(target=shoulder_working)
        t2.start()

    def shoulder_working():
        bot.arm.set_single_joint_position("shoulder", shoulder_value.get())

    shoulder_label = Label(root, text='Shoulder:')
    shoulder_label.grid(column=0, row=1, sticky='we')

    shoulder_slider = Scale(root, from_=-1.84, to=1.74, resolution=0.01, showvalue=False, orient='horizontal', command=shoulder_thread,
                            variable=shoulder_value)
    shoulder_slider.grid(row=1, column=1, sticky="we", padx=5, pady=5)

    shoulder_value_label = Label(root, textvariable=shoulder_value)
    shoulder_value_label.grid(row=1, column=2, sticky='we')

    # Elbow
    elbow_value = DoubleVar()

    def elbow_thread(event):
        t3 = Thread(target=elbow_working)
        t3.start()

    def elbow_working():
        bot.arm.set_single_joint_position("elbow", elbow_value.get())

    elbow_label = Label(root, text='elbow:')
    elbow_label.grid(row=2, column=0, sticky='we')

    elbow_slider = Scale(root, from_=-1.77, to=1.65, resolution=0.01, showvalue=False,
                         orient='horizontal', command=elbow_thread,                         variable=elbow_value)
    elbow_slider.grid(row=2, column=1, sticky="we", padx=5, pady=5)

    elbow_value_label = Label(root, textvariable=elbow_value)
    elbow_value_label.grid(row=2, column=2, sticky='we')

    # Wrist_angle
    wa_value = DoubleVar()

    def wa_thread(event):
        t4 = Thread(target=wa_working)
        t4.start()

    def wa_working():
        bot.arm.set_single_joint_position("wrist_angle", wa_value.get())

    wa_label = Label(root, text='wrist angle:')
    wa_label.grid(row=3, column=0, sticky='we')

    wa_slider = Scale(root, from_=-1.74, to=2.14, resolution=0.01, showvalue=False, orient='horizontal', command=wa_thread,
                      variable=wa_value)
    wa_slider.grid(row=3, column=1, sticky="we", padx=5, pady=5)

    wa_value_label = Label(root, textvariable=wa_value)
    wa_value_label.grid(row=3, column=2, sticky='we')

    # Wrist_rotate
    wr_value = DoubleVar()

    def wr_thread(event):
        t5 = Thread(target=wr_working)
        t5.start()

    def wr_working():
        bot.arm.set_single_joint_position("wrist_rotate", wr_value.get())

    wr_label = Label(root, text='wrist rotate:')
    wr_label.grid(row=4, column=0, sticky='we')

    wr_slider = Scale(root, from_=-3.14, to=3.14, resolution=0.01, showvalue=False, orient='horizontal', command=wr_thread,
                      variable=wr_value)
    wr_slider.grid(row=4, column=1, sticky="we", padx=5, pady=5)

    wr_value_label = Label(root, textvariable=wr_value)
    wr_value_label.grid(row=4, column=2, sticky='we')

    # BUTTON
    def check_limit():
        print(bot.arm.check_joint_limits(bot.arm.joint_commands))
    check_joint = Button(root, text='CHECK', command=check_limit)
    check_joint.grid(row=99, column=1)

    def show_value():
        print(bot.arm.joint_commands)
    show_joint = Button(root, text='Show', command=show_value)
    show_joint.grid(row=100, column=1)


if __name__ == "__main__":
    root = Tk()
    root.geometry('600x500')
    root.resizable(False, False)
    root.title('RX150 Controller')

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=3)
    root.columnconfigure(2, weight=1)

    bot = InterbotixManipulatorXS('rx150', 'arm', 'gripper')
    bot.arm.go_to_home_pose()

    create_gui()
    root.mainloop()

    bot.arm.go_to_sleep_pose()
