import sys
import Network

def print_usage():
   sys.exit('Usage: %s <address> <port>' % ( sys.argv[0] ))

if len(sys.argv) < 3:
   print_usage()

# The following is simply to test the Network object

soc = Network.Network()
soc.addr = sys.argv[1]
soc.port = sys.argv[2]

if not soc.tcp_connect():
   print "%s" % ( soc.error )
   sys.exit(1)

buf = soc.recv()
print "%s" % ( buf )
if buf[:3] != "220":
   print "No SMTP Greeting\n"
   soc.close()
   sys.exit(1)

if not soc.send("HELO test.com\r\n"):
   print "%s" % ( soc.error )
   sys.exit(1)

buf = soc.recv()
print "%s" % ( buf )
soc.close()
