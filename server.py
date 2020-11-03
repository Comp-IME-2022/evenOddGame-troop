import socket

TCP_PORT = 4242
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", TCP_PORT))
s.listen(1)

while True:
    i = 0
    firstIsEven = True
    connections = {}
    ans = 0
    while i < 2:
        conn, addr = s.accept()
        if i == 0:
            conn.send(b"y")
            data = conn.recv(BUFFER_SIZE)
            firstIsEven = data == b"p"

        else:
            if firstIsEven:
                conn.send(b"i")
            else:
                conn.send(b"p")

        ans += int(conn.recv(BUFFER_SIZE))

        if i == 0 and firstIsEven:
            connections["p"] = conn
        elif i == 1 and not firstIsEven:
            connections["p"] = conn
        else:
            connections["i"] = conn

        i += 1

    if ans % 2 == 0:
        connections["p"].send(b"VOCE GANHOU!")
        connections["i"].send(b"VOCE PERDEU!")
    else:
        connections["i"].send(b"VOCE GANHOU!")
        connections["p"].send(b"VOCE PERDEU!")
