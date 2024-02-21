"""
This Python program verifies whether the operating system is Linux or Windows.
Author: Amanda Andreis
Date: 21/02/2024
"""
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import sr1, IP, ICMP

def check_os(ip):
    """
    This function sends an ICMP echo request packet to the specified IP address
    and determines the operating system based on the response TTL value
    and TCP flags in the response packet, the script categorizes the system as Linux, Windows, or Unknown. 

    It prompts the user for an IP address, sends an ICMP packet, and displays the detected operating system.
    """
    packet = IP(dst=ip)/ICMP()
    response = sr1(packet, timeout=2, verbose=0)

    if response is None:
        return "Unknown: No response received"

    # Analyze the response (TTL and tcp flags)
    ttl = response.ttl
    tcp_flags = response.getlayer(IP).flags

    # Check TTL range
    if 64 <= ttl <= 128:
        # Check TCP flags for Windows-specific characteristics
        if tcp_flags == 0x12:  # SYN-ACK 
            return "Windows"
        elif tcp_flags == 0x14:  # RST-ACK 
            return "Windows"
        else:
            return "Linux or other"

    elif 128 < ttl <= 255:
        # Check TCP flags for Linux-specific characteristics
        if tcp_flags == 0x12:  # SYN-ACK flags
            return "Linux"
        elif tcp_flags == 0x14:  # RST-ACK flags
            return "Linux"
        else:
            return "Windows or other"

    else:
        return "Unknown: TTL value out of expected range"

if __name__ == "__main__":
    ip_address = input("Enter the IP address to be checked: ")
    result = check_os(ip_address)
    
    print(f"The operating system at IP address {ip_address} is: {result}")