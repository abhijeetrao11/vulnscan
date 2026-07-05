import socket

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