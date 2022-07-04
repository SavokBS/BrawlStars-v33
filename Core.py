import logging
import socket
import time
import os
from threading import *
from tkinter import Pack

from Logic.Player import Player
from Logic.PacketsHelper import PacketsHelper
from Factory import packets

logging.basicConfig(filename="errors.log", level=logging.INFO, filemode="w")


def _(*args):
	print('[CORE]', end=' ')
	for arg in args:
		print(arg, end=' ')
	print()


class Server:
	def __init__(self, ip: str, port: int):
		self.server = socket.socket()
		self.port = port
		self.ip = ip

	def start(self):
		_('Preparing landing area...')

		self.server.bind((self.ip, self.port))
		_(f'VokesBrawl-v33 launched!')
		while True:
			self.server.listen()
			client, address = self.server.accept()
			_(f'New connection!')
			ClientThread(client, address).start()


class ClientThread(Thread):
	def __init__(self, client, address):
		super().__init__()
		self.client = client
		self.address = address
		self.player = Player()

	def recvall(self, length: int):
		data = b''
		while len(data) < length:
			s = self.client.recv(length)
			if not s:
				print("Receive Error!")
				break
			data += s
		return data

	def run(self):
		last_packet = time.time()
		try:
			while True:
				header = self.client.recv(7)
				if len(header) > 0:
					last_packet = time.time()
					packet_id = int.from_bytes(header[:2], 'big')
					packet_name = PacketsHelper.getMessageName(packet_id)
					length = int.from_bytes(header[2:5], 'big')
					data = self.recvall(length)
					if packet_id in packets:
						_(f'Packet land! ID: {packet_id}, Name: {packet_name}, Length: {length}')
						message = packets[packet_id](self.client, self.player, data)
						message.decode()
						message.process()
					else:
						blockList = [10108, 10110]
						if packet_id not in blockList:
							_(f'Unhandled packet land! ID: {packet_id}, Name: {packet_name}, Length: {length}')
				if time.time() - last_packet > 5:
					_(f"Client disconnected!")
					self.client.close()
					break
		except ConnectionAbortedError:
			_(f"Client disconnected!")
			self.client.close()
		except ConnectionResetError:
			_(f"Client disconnected!")
			self.client.close()
		except TimeoutError:
			_(f"Client disconnected!")
			self.client.close()


if __name__ == '__main__':
	server = Server('0.0.0.0', 9339)
	server.start()