import requests
from rich import print

def subdomain_enum(domain):
    print(f"[bold magenta]Subdomain Enumeration[/bold magenta] for {domain}")
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        subdomains = set()
        for entry in data:
            name = entry.get("name_value")
            if name:
                for sub in name.split("\n"):
                    subdomains.add(sub.strip())
        subdomains = list(subdomains)
        print(f"[green]Found {len(subdomains)} subdomains[/green]")
        for sub in subdomains:
            print(sub)
        return subdomains
    except Exception as e:
        print(f"[red]Error enumerating subdomains: {e}[/red]")
        return []
