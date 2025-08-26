import requests
import socket
from rich import print

# Default local wordlist file (should contain ~10,000 subdomains, one per line)
DEFAULT_WORDLIST_FILE = "common-crawl-subdomains-10000.txt"

def load_wordlist(file_path=None):
    try:
        path = file_path or DEFAULT_WORDLIST_FILE
        with open(path, "r") as f:
            subdomains = [line.strip() for line in f if line.strip()]
        print(f"[green]Loaded {len(subdomains)} subdomains from {path}[/green]")
        return subdomains
    except Exception as e:
        print(f"[yellow]Failed to load wordlist: {e}. Using small fallback list[/yellow]")
        # Fallback small list
        return ["www", "mail", "admin", "portal", "blog", "test", "dev", "intranet"]

def subdomain_enum(domain, wordlist_file=None):
    subdomains_found = set()

    # Try crt.sh first
    try:
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        response = requests.get(url, timeout=20)
        data = response.json()
        for entry in data:
            name_value = entry.get("name_value")
            if name_value:
                for n in name_value.split("\n"):
                    subdomains_found.add(n.strip())
        if subdomains_found:
            print(f"[green]Found {len(subdomains_found)} subdomains via crt.sh[/green]")
    except Exception as e:
        print(f"[yellow]crt.sh lookup failed: {e}[/yellow]")

    # Ask user for custom wordlist
    if wordlist_file is None:
        user_input = input("Enter path to your subdomain wordlist file (or press Enter to use default): ").strip()
        wordlist_file = user_input if user_input else None

    # Load wordlist
    wordlist = load_wordlist(wordlist_file)

    # Check each subdomain in the wordlist
    print(f"[cyan]Checking {len(wordlist)} subdomains from wordlist...[/cyan]")
    for sub in wordlist:
        full = f"{sub}.{domain}"
        try:
            socket.gethostbyname(full)
            subdomains_found.add(full)
        except:
            continue

    if not subdomains_found:
        print("[red]No subdomains found[/red]")
    else:
        print(f"[green]Total unique subdomains found: {len(subdomains_found)}[/green]")

    # Return as sorted list
    return sorted(subdomains_found)
