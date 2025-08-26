import whois
from rich import print

def whois_lookup(domain):
    try:
        info = whois.whois(domain)
        print(f"[bold green]WHOIS INFO[/bold green] for {domain}:\n{info}")
        return info
    except Exception as e:
        print(f"[red]Error fetching WHOIS: {e}[/red]")
        return None

