import sys
import socket
import json

from port_scanner import scan_ports
from service_detector import find_service

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
        #print(ports)

    
    if not ports:
        print("No open ports found.")

    # now service will star 

    service = []
    service = find_service(ports)
    #print(service)
    for i in range(len(ports)):
        #print(f"[+] On port {ports[i]} {service[i]} service is running")
        entry = {"port":ports[i] , "service":service[i]}
        final_report["results"].append(entry)
    
    #print(final_report)
    print(json.dumps(final_report,indent=4))
main()


