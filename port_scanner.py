import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

def probe_single_port(target , port , timeout = 0.5):
    try:
        sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target,port))
        sock.close()
        return result == 0
    except socket.error:
        return False
    
    

def scan_ports(ip,start_port = 1,end_port = 1024,timeout = 0.5):
    open_ports = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = {}
        for port in range(int(start_port), int(end_port)+1):
            future = executor.submit(probe_single_port,ip,port, timeout)
            futures[future] = port
        for future in as_completed(futures):
            if future.result():
                if future.result():
                    open_ports.append(futures[future])     
                  

    return sorted(open_ports)