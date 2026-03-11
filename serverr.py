import socket

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 8000))
s.listen(5)
print("Server is listening for RARP requests...")

c, addr = s.accept()
print(f"Connection established with {addr}")

rarp_table = {
    "6A:08:AA:C2": "165.165.80.80",
    "8A:BC:E3:FA": "165.165.79.1"
}

while True:
    mac = c.recv(1024).decode()
    
    if not mac:
        break
    
    try:
        # Look up MAC address in RARP table
        if mac in rarp_table:
            ip = rarp_table[mac]
            c.send(ip.encode())  # Send IP back to client
            print(f"MAC {mac} -> IP {ip}")
        else:
            msg = "MAC address not found"
            c.send(msg.encode())  # Send error message
            print(f"MAC {mac} not found in table")
    
    except Exception as e:
        print(f"Error: {e}")
        break

c.close()
s.close()