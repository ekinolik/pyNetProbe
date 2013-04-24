import socket

class Network:
   soc = None
   addr = None
   port = 0
   error = None

   def tcp_connect(self):

      getinfo = socket.getaddrinfo(self.addr, self.port, socket.AF_UNSPEC, socket.SOCK_STREAM)

      for info in getinfo:
	 family, socktype, proto, cannonname, sa = info
	 try:
	    self.soc = socket.socket(family, socktype)
	 except socket.error as msg:
	    self.error = "Could not create socket: %s\n" % ( msg )
	    continue
	 
	 try:
	    self.soc.connect(sa)
	 except socket.error as msg:
	    self.error = "Unable to connect: %s\n" % ( msg )
	    self.close()
	    self.soc = None
	    continue

	 break

      if self.soc is None:
	 return 0

      return 1

   def recv(self):
      return self.soc.recv(1024)

   def send(self, data):
      try:
	 self.soc.sendall(data)
      except socket.error as msg:
	 self.error = "Unable to send data: %s\n" % ( msg )
	 return 0

      return 1

   def close(self):
      try:
	 self.soc.close()
      except socket.error as msg:
	 self.error = "Unable to close socket %s\n" % ( msg )
	 return 0

      return 1

