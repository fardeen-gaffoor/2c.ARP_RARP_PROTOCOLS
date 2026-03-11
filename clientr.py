import socket

s = socket.socket()
s.connect(('localhost', 8000))

while True:
    mac = input("Enter MAC address to find IP (or type 'exit' to quit): ")
    
    if mac.lower() == 'exit':
        break
    
    s.send(mac.encode())  # Send MAC to server
    ip = s.recv(1024).decode()  # Receive IP from server
    print(f"IP address: {ip}")  # Display the IP

s.close()