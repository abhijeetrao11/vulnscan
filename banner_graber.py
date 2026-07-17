import socket
import ssl

def grab_banner(ip , port, service):
    try:
        sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((ip,port))
        if service == "https":
            context = ssl.create_default_context()
            sock = context.wrap_socket(
                sock,
                server_hostname=ip
            )
        if service in ["http","https"]:
            request = f"HEAD / HTTP/1.1\r\nHost: {ip}\r\n\r\n"
            sock.send(request.encode())

            response = sock.recv(4096)
            response = response.decode(errors="ignore")
            banner = None
            for line in response.splitlines():
                if line.startswith("Server:"):
                    banner = line.split(":",1)[1].strip()
                    break;
            return banner;

        elif service in ["ssh","ftp","smtp","pop3","imap","mysql","postgresql"]:
            banner = sock.recv(4096).decode(errors="ignore")
            return banner.strip()
        
        elif service == "redis":
            sock.send(b"PING\r\n")
            banner = sock.recv(4096).decode(errors="ignore")
            return banner.strip()



    except socket.timeout:
        return None
    except ConnectionRefusedError:
        return None
    except ssl.SSLError:
        return None
    except Exception:
        return None
    finally:
        sock.close()

    

