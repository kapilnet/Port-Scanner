import socket

# Step 1: Starting message
print("Port Scanner Started")

# Step 2: Ask for target IP
target = input("Enter target IP address: ")
print("Scanning target:", target)

# Step 3: Scan ports from 20 to 1024
for port in range(20, 1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # wait 1 second per port
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port}: OPEN")
    sock.close()

print("Scan Completed!")
