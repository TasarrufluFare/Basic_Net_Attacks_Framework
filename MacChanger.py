import re
import subprocess


def change_mac_adress(given_interface, given_macaddress):
    try:
        subprocess.call(["ifconfig", given_interface, "down"])
        subprocess.call(["ifconfig", given_interface, "hw", "ether", given_macaddress])
        subprocess.call(["ifconfig", given_interface, "up"])
    except ValueError:
        print("Value Error!")


def get_user_input(interface, newmac):
    request_dict = {"r_interface": interface, "r_newmac" : newmac}
    return request_dict


def control_new_mac(given_interface):
    ifconfig_output = subprocess.check_output(["ifconfig", given_interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_output))
    if new_mac:
        return new_mac.group(0)
    else:
        return None


def start_macchanger(interface, newmac):
    print("Mac Changer has started!")
    try:
        request_dict = get_user_input(interface, newmac)

        user_interface = request_dict["r_interface"]
        user_macaddress = request_dict["r_newmac"]
        print("Chosen Net Interface: "+user_interface)
        print("New Mac Address: "+user_macaddress)

        change_mac_adress(user_interface, user_macaddress)

        finalized_mac = control_new_mac(str(user_interface))

        if finalized_mac == user_macaddress:
            print("Mac Changer has done it's job...")
        else:
            print("Mac Changer couldn't done it's job...")
    except KeyboardInterrupt:
        print("Process canceled by user.")

