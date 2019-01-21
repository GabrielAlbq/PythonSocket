import socket
def Main():
    host = '127.0.0.1'
    port = 5000

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    message = input("-> ")
    while message != 'q':
        #s.send(message.encode('utf-8'))
        codf = message.encode('utf-8')
        getrequest = 'GET /'+message+' HTTP/1.1\r\n\r\n'
        client.send(getrequest.encode('utf-8'))
        data = client.recv(1024).decode('utf-8')
        lista = data.split(' ')
        method = lista[0]  # First string is a method
        requesting_file = lista[1]
        if(lista[1] == '200'):
            print('ok')
        elif(lista[1] == '404'):
            print('Desculpe, mas não conseguimos encontrar a página solicitada')
        for a in range(lista):
            if(a!=0 | a!=1| a!=2):
                recebido += lista[a]

        print (lista[1])
        print ('Received from server: ' + str(recebido))
        message = input("-> ")
    s.close()

if __name__ == '__main__':
    Main()