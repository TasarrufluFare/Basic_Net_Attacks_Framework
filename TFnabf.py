import subprocess
import MacChanger
from MITM import *
from PacketListener import *
from NetScanner import *
subprocess.call("clear")
print("𝓝𝓮𝓽 𝓐𝓽𝓽𝓪𝓬𝓴 𝓑𝓪𝓼𝓲𝓬𝓼 𝓕𝓻𝓪𝓶𝓮𝔀𝓸𝓻𝓴 𝓿1.0\n------------------------------------------------")
print("To Activate IP Forwarding - Type IFA\n------------------------------------------------")
print("Operations:\n1 - Mac Changer\n2 - Man In The Middle\n3 - Packet Listener\n4 - Net Scanner\n5 - Clear\n6 - Exit")
try:
    while True:
        user_request = input("\nSelect an operation: ")

        if not user_request == "IFA":
            user_request = user_request.lower()

        if user_request == "IFA": #Starts ip forwarding
            try:
                subprocess.call(["echo", "1 > /proc/sys/net/ipv4/ip_forward"])
                print("IP Forwarding activated.")
            except:
                print("Something went wrong! - IP Forwarding failed.")

        elif user_request == "1" or user_request == "mc" or user_request == "mac changer": #Starts Mac Changer
            try:
                print("You are using the Mac Changer.")
                user_r_interface = input("Type interface to change mac address: ")
                user_r_newmac = input("Type mac address that you desire: ")
                try:
                    MacChanger.start_macchanger(user_r_interface, user_r_newmac)
                except:
                    print("Something went wrong! - Mac changer process has failed.")
            except KeyboardInterrupt:
                print("\nProcess canceled by user.")

        elif user_request == "2" or user_request == "mitm" or user_request == "man in the middle":
            try:
                print("You are Man in the middle operation.")
                user_r_ip1 = input("Enter Target IP: ")
                user_r_ip2 = input("Enter Gateway IP: ")
                if not user_r_ip1:
                    print("Enter Target IP")
                    exit()
                if not user_r_ip2:
                    print("Enter Gateway IP")
                    exit()
                user_inputs = {"ip1": user_r_ip1, "ip2" : user_r_ip2}
                user_target_ip = user_inputs["ip1"]
                user_gateway_ip = user_inputs["ip2"]
                packet_number = 0
                try:
                    start_mitm(user_target_ip, user_gateway_ip)
                except KeyboardInterrupt:
                    print("\nProcess Ended by user. Mac address's reset.")
                    reverse_poisoning(user_target_ip, user_gateway_ip)
                    reverse_poisoning(user_gateway_ip, user_target_ip)
            except KeyboardInterrupt:
                print("\nProcess canceled by user.")

        elif user_request == "3" or user_request == "pl" or user_request == "listener" or user_request == "packet listener":
            try:
                listen_interface = input("Type the net interface which you desire to listen: ")
                try:
                    listen_packets(listen_interface)
                except:
                    print("Something went wrong! - Packet Listener process has failed.")
            except:
                print("\nProcess canceled by user.")

        elif user_request == "4" or user_request == "ns" or user_request == "scanner" or user_request == "net scanner":
            try:
                user_input_iprange = input("Type IP Range to scan: ")
                if not user_input_iprange:
                    print("Enter ip address range, Example: -i 10.0.2.1/24")
                    exit()
                start_netscan(str(user_input_iprange))
            except KeyboardInterrupt:
                print("\nProcess canceled by user.")

        elif user_request == "5" or user_request == "clc" or user_request == "clear":
            subprocess.call("clear")
            print("𝓝𝓮𝓽 𝓐𝓽𝓽𝓪𝓬𝓴 𝓑𝓪𝓼𝓲𝓬𝓼 𝓕𝓻𝓪𝓶𝓮𝔀𝓸𝓻𝓴 𝓿1.0\n------------------------------------------------")
            print("To Activate IP Forwarding - Type IFA\n------------------------------------------------")
            print("Operations:\n1 - Mac Changer\n2 - Man In The Middle\n3 - Packet Listener\n4 - Net Scanner\n5 - Clear\n6 - Exit")

        elif user_request == "6" or user_request == "esc" or user_request == "exit":
            print("\nExiting...")
            exit()
except KeyboardInterrupt:
    print(" ")
    print("\nExiting...")
