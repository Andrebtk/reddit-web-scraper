import socket
import tqdm
import os


SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096
host = "192.168.1.42"
port = 5001
filename = "struc.csv"

filesize = os.path.getsize(filename)

s = socket.socket()

print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")