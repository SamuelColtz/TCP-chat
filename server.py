# Python3 TCP chat

import socket
from colorama import Fore, Back, Style
from threading import Thread 

TCP_IP = '127.0.0.1'
TCP_PORT = 6060 
BUFFER_SIZE = 1024 #1kb
clients = list()

server = socket.socket()
server.bind((TCP_IP, TCP_PORT))
server.listen(10)
print(Fore.GREEN + 'server was listting...')

class Client():
	def __init__(self, conn, addr):
		self.__conn = conn
		self.__addr = addr
		Thread(target=self.received, args=()).start()

	@property
	def conn(self):
		return self.__conn

	@property
	def addr(self):
		return self.__addr
	
	def received(self):
		self.name = self.conn.recv(BUFFER_SIZE).decode()

		while 1:
			data = self.conn.recv(BUFFER_SIZE).decode()
			if not data:
				self.exit()
				return 0
			self.send(data)

	def exit(self):
		print(Fore.RED + 'been close')
		print(Style.RESET_ALL)
		self.conn.close()
		for i in clients:
			if i.addr == self.addr:
				clients.remove(i)

	def send(self, data):
		msg = self.name + ': ' + data
		for i in clients:
			if i.addr != self.addr:
				i.conn.send(msg.encode())

while 1:
	conn, addr = server.accept()
	clients.append(Client(conn, addr))
	print(Fore.GREEN +'client: ', addr, 'connected!' )

server.close()
	