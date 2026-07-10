import sys
import socket
import json
import time

from port_scanner import scan_ports
from service_detector import find_service
from version_detector import detect_version
from banner_graber import grab_http_banner
from cve_lookup import lookup_cve
from report_generator import generate_html_report
from pdf_generator import generate_pdf

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <target> [start_port end_port]")
        sys.exit(1)

    target = sys.argv[1]

    final_report = {}
    final_report["target"] = target
    final_report["results"] = []

    start = time.time()

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
    end = time.time()
    scan_time = end - start
    print(f"\n[+] Port scan completed in {scan_time:.2f} seconds")
    

    
    if not ports:
        print("No open ports found.")

    service = find_service(ports)

    for i in range(len(ports)):
        banner = None
        software = None
        version = None

        #grab banner only for http service

        if service[i] == "http":
            banner = grab_http_banner(target , ports[i])

            if banner:
                version_info = detect_version(banner)
                software = version_info["software"]
                version = version_info["version"]

        vulnerabilities = []
        if software and version:
            vulnerabilities = lookup_cve(software,version)
            
        entry = {
            "port": ports[i],
            "service": service[i],
            "banner": banner,
            "software": software,
            "version": version,
            "vulnerabilities" : vulnerabilities
        }

        final_report["results"].append(entry)

    print(json.dumps(final_report,indent=4))
    generate_html_report(final_report)
    generate_pdf()




main()


