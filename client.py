import socket
import sys

BUFFER_SIZE = 1024


def get_socket():
    while True:
        ip_port = input(
            "Digite o IP do servidor e a porta no formato HOST:PORT (ex.: 127.0.0.1:443): "
        )
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip_port.split(":")[0], int(ip_port.split(":")[1])))
            break
        except:
            print("IP invalido ou conexao recusada, tente novamente", file=sys.stderr)

    return s


def evenOrOdd(s):
    data = s.recv(BUFFER_SIZE)
    if data == b"y":
        while True:
            print("Voce foi a primeira conexao!")
            choice = input("Digite p para escolher par e i para impar: ")
            if choice in ["p", "i"]:
                break
            else:
                print("Invalido", file=sys.stderr)

        s.send(str.encode(choice))
    else:
        choice = data.decode("utf-8")
        if choice == "p":
            print("Voce foi a segunda conexao, voce sera o par")
        else:
            print("Voce foi a segunda conexao, voce sera o impar")
    return choice


def chooseNum():
    while True:
        num = input("Digite o numero que voce quer jogar: ")

        try:
            num = int(num)
            break
        except:
            print("Numero invalido", file=sys.stderr)

    return num


print("Bem vindo ao jogo de par ou impar!")
s = get_socket()

print("Conexao bem sucedida!")
evenOrOdd(s)

num = chooseNum()
s.send(str.encode(str(num)))
print("Esperando o outro jogador...")
data = s.recv(BUFFER_SIZE)
print(data.decode())
s.close()
