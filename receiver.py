import socket
import sys
import keyboard
import mouse
 
HOST = ''
PORT = 5789
   
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
try:
    soc.bind((HOST, PORT))
      
except socket.error as message:
    print('Bind failed. Error Code : '
          + str(message[0]) + ' Message '
          + message[1])
    sys.exit()
     
print('Socket binding operation completed')
  
soc.listen(9)
  
conn, address = soc.accept()
print('Connected with ' + address[0] + ':'
      + str(address[1]))
while True:
    data = conn.recv(1024)
    
    if data == b's':
        keyboard.press_and_release('space')
    elif data == b'f':
        keyboard.press_and_release('f')
    elif data == b'e':
        keyboard.press_and_release('esc')
    elif data == b'u':
        keyboard.press_and_release('up')
    elif data == b'd':
        keyboard.press_and_release('down')
    elif data == b'l':
        keyboard.press_and_release('left')
    elif data == b'r':
        keyboard.press_and_release('right')
    elif data == b'ml':
        x,y = mouse.get_position()
        mouse.move(x-15, y, absolute=True, duration=0)
    elif data == b'mr':
        x,y = mouse.get_position()
        mouse.move(x+15, y, absolute=True, duration=0)
    elif data == b'md':
        x,y = mouse.get_position()
        mouse.move(x, y+15, absolute=True, duration=0)
    elif data == b'mu':
        x,y = mouse.get_position()
        mouse.move(x, y-15, absolute=True, duration=0)
    elif data == b'mlc':
        mouse.click(button='left')
    elif data == b'mrc':
        mouse.right_click()
    elif data == b'':
        soc.listen(9)
  
        conn, address = soc.accept()
