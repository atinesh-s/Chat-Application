import socket, threading

def send(uname):
    while True:
        msg = raw_input('\nMe > \n')
        data = '\n\n' + uname + ' > ' + msg + '\n\nMe > '
        cli_sock.send(data)

def receive():
    while True:
        data = cli_sock.recv(1024)
        print('\t'+ str(data))

if __name__ == "__main__":   
    # socket
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect
    HOST = 'localhost'
    PORT = 5020
    
    uname = raw_input('Enter your name to enter the chat > ')

    cli_sock.connect((HOST, PORT))     
    print('Connected to remote host...')
    cli_sock.send(uname)

    thread_send = threading.Thread(target = send,args=[uname])
    thread_send.start()

    thread_receive = threading.Thread(target = receive)
    thread_receive.start()
