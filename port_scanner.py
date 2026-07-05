import socket

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
    for i in range(int(start_port), int(end_port)+1):
        if probe_single_port(ip,i,timeout):
            open_ports.append(i)
    
    return open_ports