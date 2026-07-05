import sys
import socket
import json

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


def find_service(ports):
    service = []
    for i in ports:
        try:
            x = socket.getservbyport(i)
            service.append(x)
        except OSError:
            print("[-] getting error")
            service.append("UNKNOWN")
            continue
    return service

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <target> [start_port end_port]")
        sys.exit(1)

    target = sys.argv[1]

    final_report = {}
    final_report["target"] = target
    final_report["results"] = []

    if len(sys.argv) >= 4:
        sport = int(sys.argv[2])
        eport = int(sys.argv[3])
        if eport > 65535:
            print("your port number should be in range of 0-65535")
            sys.exit(1)
        ports = scan_ports(target, sport, eport)
    else:
        ports = scan_ports(target)

    
    if not ports:
        print("No open ports found.")

    # now service will star 

    service = []
    service = find_service(ports)
    for i in range(len(ports)):
        #print(f"[+] On port {ports[i]} {service[i]} service is running")
        entry = {"port":ports[i] , "service":service[i]}
        final_report["results"].append(entry)
    
    print(json.dumps(final_report,indent=4))
main()


