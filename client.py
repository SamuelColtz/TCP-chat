import socket 
from colorama import Fore, Style, Back
from threading import Thread


TCP_IP = '127.0.0.1'
TCP_PORT = 6060
BUFFER_SIZE = 1024


client = socket.socket()
client.connect((TCP_IP, TCP_PORT))

def inp():
	print('Welcome to the chat room')
	name = input('plase type your name: ')
	print(Fore.GREEN  + 'Welcome to the chat ', Fore.MAGENTA + name)
	print(Style.RESET_ALL)
	client.send(name.encode())
	while 1:
		data = input(Fore.BLUE + 'you: ' + Style.RESET_ALL)
		if data == '-close':
			client.close()
			return 0
		client.send(data.encode())

def recevied():
	while 1:
		data = client.recv(BUFFER_SIZE).decode()
		print(Fore.RED + data)
		print(Style.RESET_ALL)


Thread(target=inp, args=()).start()	
Thread(target=recevied, args=()).start()
