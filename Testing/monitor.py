# use arp poisning :)
from scapy.all import Ether, ARP, srp, send



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


# iproute_windows()
get_mac('192.168.1.1')

