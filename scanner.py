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

target_host = input("Enter target host: ")
start_port = input("Enter the starting port: ")
end_port = input("Enter the ending port: ")


try: 
    start_port = int(start_port)
    end_port = int(end_port)
    if (start_port >= 1 and end_port >= start_port and end_port <= 65535):
        ports = range(start_port, end_port + 1)
        scan_ports(target_host, ports)
    else: 
        print("Error: please enter a valid port range")

except ValueError: 
    print("Error: ports must be integers.")
