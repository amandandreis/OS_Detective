# OS_Detective
OSDetective is a Python script that detects the operating system of a target machine based on its response to an ICMP echo request. It utilizes the Scapy library for packet manipulation and analysis.

## How it Works

When run, OSDetective prompts the user to input the IP address of the target machine. It then sends an ICMP echo request packet to the specified IP address using Scapy and waits for the response.

Upon receiving the response, OS Detective analyzes the Time to Live (TTL) value and TCP flags in the response packet. Based on these characteristics, it categorizes the operating system of the target machine as Linux, Windows, or Unknown.

The detected operating system is then displayed to the user.

## Prerequisites

- Python 3.x
- Scapy library (`pip install scapy`)

## Usage

1. Clone this repository to your local machine.
2. Navigate to the directory containing OSDetective.py.
3. Run the script by executing the command `python OSDetective.py`.
4. Follow the on-screen prompts to input the IP address of the target machine.
5. View the detected operating system.

## Example
$ python OSDetective.py
Enter the IP address to be checked: 192.168.1.100
The operating system at IP address 192.168.1.100 is: Windows

## Credits

- **Author:** Amanda Andreis
- **Email:** amandaandreis04@gmail.com
