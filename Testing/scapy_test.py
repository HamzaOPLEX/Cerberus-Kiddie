from sys import flags
from scapy.all import IP,sr,TCP,sr1


# Global Variables
ports = [80,40,443,21]




for port in ports : 
    res = sr1(IP(dst='192.168.1.1')/TCP(dport=port,flags='S'),timeout=5,verbose=False)
    if res


# res,nres = sr1(IP(dst='192.168.1.1')/TCP(dport=ports),verbose=False,timeout=5)

# print('unresponded :')
# nres.summary()

# print('responded :')
# res.summary()
# # res.summary( lambda s,r: r.sprintf("Port %TCP.sport% is open in %IP.src%") )
# # nres.summary( lambda r: r.sprintf("Port %TCP.sport% is closed in %IP.src%") 