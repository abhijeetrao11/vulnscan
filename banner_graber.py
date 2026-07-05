import socket

def grab_http_banner(ip , port):
    try:
        sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((ip,port))
        request = f"HEAD / HTTP/1.1\r\nHost: {ip}\r\n\r\n"
        sock.send(request.encode())

        response = sock.recv(4096)
        response = response.decode()
        for line in response.splitlines():
            if line.startswith("Server:"):
                banner = line.split(":",1)[1].strip()
                break;
        return banner;
    except TimeoutError as e:
        print(e)
    finally:
        sock.close()
    

