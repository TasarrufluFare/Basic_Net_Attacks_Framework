import scapy.all as scapy


def create_broadcast_arp_request(given_iprange, given_bcmac="ff:ff:ff:ff:ff:ff"):
    if str(given_bcmac) != "ff:ff:ff:ff:ff:ff":
        given_bcmac = "ff:ff:ff:ff:ff:ff"
        print("Edited Broadcast Mac Address:", given_bcmac)

    arp_request_packet = scapy.ARP(pdst=str(given_iprange))

    broadcast_packet = scapy.Ether(dst=str(given_bcmac))

    combined_packet = broadcast_packet / arp_request_packet

    return scapy.srp(combined_packet, timeout=1)


def start_netscan(user_input_iprange):
    try:
        (answered_list, unanswered_list) = create_broadcast_arp_request(str(user_input_iprange))
        answered_list.summary()
    except KeyboardInterrupt:
        print("\nProcess canceled by user.")
