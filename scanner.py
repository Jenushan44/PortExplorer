import socket
import time

def scan_port(host, port): 

    start_scan_time = time.time()
    # Create a TCP socket that communicates over IPv4. 
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.settimeout(1)
    result = tcp_socket.connect_ex((host, port))
    tcp_socket.close()

    end_scan_time = time.time()
    scan_time_length = end_scan_time - start_scan_time
    
    if result == 0: 
        return True, scan_time_length
    else:
        return False, scan_time_length
    
def scan_ports(host, ports):
    total_scan_time = 0
    open_ports = 0
    closed_ports = 0
    print(f"Scanning {host}...\n")
    for port in ports: 
        current_port, scan_time_length = scan_port(host, port)
        if (current_port):
            print(f"{port}: Open")
            total_scan_time += scan_time_length
            open_ports += 1
        else: 
            print(f"{port}: Closed")
            total_scan_time += scan_time_length
            closed_ports += 1
    print(f"Scan completed in {round(total_scan_time, 2)} seconds")
    print(f"\nPorts scanned: {open_ports+closed_ports}")
    print(f"Open Ports: {open_ports}")
    print(f"Closed Ports: {closed_ports}")


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
