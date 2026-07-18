import socket

def scan_port(host, port): 

    # Create a TCP socket that communicates over IPv4. 
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    tcp_socket.settimeout(1)

    result = tcp_socket.connect_ex((host, port))