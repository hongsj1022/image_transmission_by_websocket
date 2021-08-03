from scp import SCPClient, SCPException
import paramiko
import os
import time
from zipfile import *

class SSHManager:
	
	def __init__(self):
		self.ssh_client = None

	def create_ssh_client(self, hostname, username, password):
		"""Create SSH client session to remote server"""
		if self.ssh_client is None:
			self.ssh_client = paramiko.SSHClient()
			self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			self.ssh_client.connect(hostname, username=username, password=password)
		else:
			print("SSH client session exist.")

	def close_ssh_client(self):
		"""Close SSH client session"""
		self.ssh_client.close()

	def send_file(self, local_path, remote_path):
		"""Send a single file to remote path"""
		try: 
			with SCPClient(self.ssh_client.get_transport()) as scp:
				scp.put(local_path, remote_path, preserve_times=True)
		except SCPException:
			raise SCPException.message

	def get_file(self, remote_path, local_path):
		"""Get a single file from remote path"""
		try:
			with SCPClient(self.ssh_client.get_transport()) as scp:
				scp.get(remote_path, local_path)
		except SCPException:
			raise SCPException.message

	def send_command(self, command):
		"""Send a single command"""
		stdin, stdout, stderr = self.ssh_client.exec_command(command)
		return stdout.readlines()

if __name__ == '__main__':
	
	start_time = time.time() 
	ssh_manager = SSHManager()
	local_path = "/home/pi/image/images.zip"
	remote_path = "/home/super/images.zip"
	ssh_manager.create_ssh_client("163.180.117.43", "super", "super123!@#")

	#if len(os.listdir("./images")) == 10:
	file = "./images"
	with ZipFile(file + '.zip', 'w') as compzip:
		compzip.write(file)
	ssh_manager.send_file(local_path,remote_path)
	ssh_manager.get_file(remote_path,local_path)
	ssh_manager.close_ssh_client()
	end_time = time.time()
	print(end_time - start_time)

