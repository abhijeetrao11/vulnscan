import sys
import socket
import json
import time
import argparse

from port_scanner import scan_ports
from service_detector import find_service
from version_detector import detect_version
from banner_graber import grab_banner
from cve_lookup import lookup_cve
from report_generator import generate_html_report
from pdf_generator import generate_pdf

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <target> [start_port end_port]")
        sys.exit(1)
    
    parser = argparse.ArgumentParser(description="Python Vulnerability Scanner")
    parser.add_argument("target",help="Target IP address")
    parser.add_argument("--start-port",type=int,default=1,help="Starting Port")
    parser.add_argument("--end-port",type=int,default=1024,help="Ending port")
    parser.add_argument("--threads",type=int,default=50,help="number of worker threads")
    parser.add_argument("--pdf",action="store_true",help="generate pdf report ")
    parser.add_argument("--html",action="store_true",help="generate html report ")
    args = parser.parse_args()


    target = args.target

    final_report = {}
    final_report["target"] = target
    final_report["results"] = []

    start = time.time()

    sport = args.start_port
    eport = args.end_port
    thread = args.threads
    generate_pdf_flag = args.pdf
    generate_html_flag = args.html

    if sport<1 or sport>65535:
        print(f"[-] invalid start Port.")
        sys.exit(1)

    if eport<1 or eport>65535:
        print(f"[-] Invalid start Port.")
        sys.exit(1)
    
    if sport > eport:
        print(f"[-] start port cannot be greater than end port")
        sys.exit(1)
    
    if thread < 1:
        print(f"[-] thread count must be greater than 0.")
        sys.exit(1)

   
    ports = scan_ports(target, sport, eport,threads=thread)
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

        # if service[i] == "http":
        #     banner = grab_http_banner(target , ports[i])

        supported_services = [
            "http",
            "https",
            "ssh",
            "ftp",
            "smtp",
            "pop3",
            "imap",
            "mysql",
            "redis"
        ]

        if service[i] in supported_services:
            banner = grab_banner(
                target,
                ports[i],
                service[i]
            )


        

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
    if generate_html_flag:
        generate_html_report(final_report)
    if generate_pdf_flag:
        generate_pdf()




main()


