import socket

def scan_port(host, port): 

    # Create a TCP socket that communicates over IPv4. 
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    tcp_socket.settimeout(1)

    result = tcp_socket.connect_ex((host, port))

    tcp_socket.close()

    if result == 0: 
        return True 
    else:
        return False
    
def scan_ports(host, ports):
    print(f"Scanning {host}...\n")
    for port in ports: 
        if (scan_port(host, port)):
            print(f"{port}: Open")
        else: 
            print(f"{port}: Closed")

ports = [22, 80, 443, 8000, 9999]

scan_ports("127.0.0.1", ports)