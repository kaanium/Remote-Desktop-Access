from tkinter import *

import socket

host = "192.168.1.22"
port = 5789
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


def port_data(data):
    s.sendall(data)


root = Tk()
root.geometry=("500x800")
frame = Frame(root, width=500, height=800)
frame.pack()

space_button = Button(frame, text="Space", command=lambda: port_data(b's'))
space_button.place(x=170, y=300, width=90, height=65)
f_button = Button(frame, text="F", command=lambda: port_data(b'f'))
f_button.place(x=170, y=230, width=90, height=65)
esc_button = Button(frame, text="Esc", command=lambda: port_data(b'e'))
esc_button.place(x=70, y=230, width=90, height=65)
up_arrow = Button(frame, text="↑", command=lambda: port_data(b'u'), repeatinterval=50, repeatdelay=50)
up_arrow.place(x=170, y=390, width=90, height=65)
down_arrow = Button(frame, text="↓", command=lambda: port_data(b'd'), repeatinterval=50, repeatdelay=50)
down_arrow.place(x=170, y=460, width=90, height=65)
left_arrow = Button(frame, text="←", command=lambda: port_data(b'l'), repeatinterval=50, repeatdelay=50)
left_arrow.place(x=70, y=460, width=90, height=65)
right_arrow = Button(frame, text="→", command=lambda: port_data(b'r'), repeatinterval=50, repeatdelay=50)
right_arrow.place(x=270, y=460, width=90, height=65)
mouse_right = Button(frame, text="→", command=lambda: port_data(b'mr'), repeatinterval=50, repeatdelay=50)
mouse_right.place(x=320, y=620, width=90, height=65)
mouse_left = Button(frame, text="←", command=lambda: port_data(b'ml'), repeatinterval=50, repeatdelay=50)
mouse_left.place(x=20, y=620, width=90, height=65)
mouse_up = Button(frame, text="↑", command=lambda: port_data(b'mu'), repeatinterval=50, repeatdelay=50)
mouse_up.place(x=170, y=550, width=90, height=65)
mouse_down = Button(frame, text="↓", command=lambda: port_data(b'md'), repeatinterval=50, repeatdelay=50)
mouse_down.place(x=170, y=690, width=90, height=65)
mouse_left_click = Button(frame, text="LC", command=lambda: port_data(b'mlc'))
mouse_left_click.place(x=120, y=620, width=90, height=65)
mouse_right_click = Button(frame, text="RC", command=lambda: port_data(b'mrc'))
mouse_right_click.place(x=220, y=620, width=90, height=65)

root.mainloop()