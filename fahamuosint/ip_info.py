import socket
from rich import print

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"[bold blue]IP INFO[/bold blue] {domain}: {ip}")
        return ip
    except Exception as e:
        print(f"[red]Error resolving IP: {e}[/red]")
        return None

