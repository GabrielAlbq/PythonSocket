import socket

def Main():
    host = '0.0.0.0'
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(2)
    #c, addr = s.accept()
    #print ("Connection from: " + str(addr))
    while True:
        connection, addr = s.accept()
        print("Connection from: " + str(addr))
        data = connection.recv(1024).decode('utf-8')
        print (data)
        lista = data.split(' ')
        for a in lista:
            if a in "first_button=Portugues":
                print('o botao esta presente')
        if len(lista)<2:
            print('nao pega')
            continue
        method = lista[0]# First string is a method
        requesting_file = lista[1]# Second string is request file
        ultimo = len(lista)-1
        dalista = lista[ultimo]
        separando = dalista.split('&')
        again = separando[len(separando)-1]
        isso = again.split('=')
        textomudado = isso[len(isso)-1]
        print(textomudado)
        #print(dalista)
        print('Client request', method + requesting_file)

        if requesting_file == '/':
            requesting_file = 'index.html'
            response = open(requesting_file).read()
            print(requesting_file)
        elif requesting_file == '/teste.html':
            requesting_file = 'teste.html'
            file = open(requesting_file, 'rb')
            response = file.read().decode('utf-8').format(traduz=textomudado)
            #response = open(requesting_file).read().format(traduz='adeus')
            #print(resposta)

        try:
            #file = open(requesting_file, 'rb')  # open file , r => read , b => byte format
            #response = file.read()
            #file.close()

            header = 'HTTP/1.1 200 OK\n'

            if (requesting_file.endswith(".jpg")):
                mimetype = 'image/jpg'
            elif (requesting_file.endswith(".css")):
                mimetype = 'text/css'
            else:
                mimetype = 'text/html'

            header += 'Content-Type: ' + str(mimetype) + '\n\n'

        except Exception as e:
            header = 'HTTP/1.1 404 Not Found\n\n'
            response = '<html>' \
                        '<head>' \
                       '    <meta charset="UTF-8">' \
                       '    <title>TESTANDO</title>' \
                       '</head>'\
                       '    <body>' \
                       '        <center>' \
                       '            <h3>Error 404: File not found </h3>' \
                       '                <p>Desculpe, mas não conseguimos encontrar a página solicitada</p>' \
                       '        </center>' \
                       '    </body>' \
                       '</html>'.encode('utf-8')
        final_response = header.encode('utf-8')
        final_response += response.encode('utf-8')
        connection.send(final_response)
        connection.close()





       # print ("from connected user: " + str(data))
       # data = str(data).upper()
       # print ("sending: " + str(data))
        #c.send(data.encode('utf-8'))
        '''
        c.send(b'HTTP/1.0 200 OK\n')
        c.send(b'Content-Type: text/html\n')
        c.send(b'\n')  # header and body should be separated by additional newline
        c.send(b"""
                <html>
                <head>
                    <meta charset="UTF-8">
                    <title>TESTANDO</title>
                </head>
                <body>
                <h1>Hello World</h1> this is my server!
                </body>
                </html>
               """)
        c.close()
        '''

if __name__ == '__main__':
    Main()
