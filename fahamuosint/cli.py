import argparse
import socket
import requests
import pandas as pd
from shodan import Shodan
from rich import print
from rich.console import Console
from rich.panel import Panel
from fahamuosint.whois_lookup import whois_lookup
from fahamuosint.ip_info import get_ip
from fahamuosint.shodan_lookup import shodan_lookup
from fahamuosint.export_results import export_results
from fahamuosint.subdomain_enum import subdomain_enum
from fahamuosint.social_scraper import social_scraper

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

console = Console()

banner_text = """
███████╗ █████╗ ██╗  ██╗ █████╗ ███╗   ███╗██╗   ██╗███████╗███████╗  ███████╗
██╔════╝██╔══██╗██║  ██║██╔══██╗████╗ ████║██║   ██║██╔════╝██╔════╝██╔══════╝
███████╗███████║███████║███████║██╔████╔██║██║   ██║███████╗███████╗██║
██╔════╝██╔══██║██╔══██║██╔══██║██║╚██╔╝██║██║   ██║╚════██║██╔════╝██║
██║     ██║  ██║██║  ██║██║  ██║██║ ╚═╝ ██║╚██████╔╝███████║███████╗ ╚███████╗
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚══════╝  ╚══════╝
"""

console.print(Panel(banner_text, style="bold green"))

console.print("[bold blue]GitHub:[/bold blue] https://github.com/Ish3ng0m4")
console.print("[bold magenta]Author:[/bold magenta] Ish3ng0m4 🎭")
# -------- CONFIG --------
SHODAN_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # Replace with your Shodan key
api = Shodan(SHODAN_API_KEY)
console = Console()

# -------- IP & Shodan Lookup --------
def ip_and_shodan(domain):
    ip_data = {}
    console.print(Panel(f"IP & Shodan for {domain}", style="cyan"))

    # Get IP
    try:
        ip = socket.gethostbyname(domain)
        console.print(f"[green]IP INFO[/green] {domain}: {ip}")
        ip_data['domain'] = domain
        ip_data['ip'] = ip
    except Exception as e:
        console.print(f"[red]Error resolving IP: {e}[/red]")
        ip = None

    # Shodan lookup
    shodan_results = []
    if ip:
        try:
            result = api.host(ip)
            for item in result['data']:
                shodan_results.append({
                    "ip": ip,
                    "port": item['port'],
                    "service": item.get('product', 'Unknown')
                })
        except Exception as e:
            console.print(f"[yellow]Error fetching Shodan data: {e}[/yellow]")

    return ip_data, shodan_results

# -------- Export Results --------
def export_results(results, filename="results", fmt="csv"):
    df_list = []
    for r in results:
        if isinstance(r['data'], list):
            if all(isinstance(i, dict) for i in r['data']):
                df_list.append(pd.DataFrame(r['data']))
            else:
                df_list.append(pd.DataFrame({r['type']: r['data']}))
        else:
            df_list.append(pd.DataFrame([{r['type']: r['data']}]))

    if fmt.lower() == "csv":
        for i, df in enumerate(df_list):
            df.to_csv(f"{filename}_{i+1}.csv", index=False)
        console.print(f"[green]Results exported to CSV files[/green]")
    elif fmt.lower() == "json":
        combined = [df.to_dict(orient="records") for df in df_list]
        with open(f"{filename}.json", "w") as f:
            import json
            json.dump(combined, f, indent=4)
        console.print(f"[green]Results exported to JSON[/green]")

# -------- Main Function --------
def main():
    parser = argparse.ArgumentParser(description="FahamuOSINT - Automated OSINT Tool")
    parser.add_argument("-d", "--domain", required=True, help="Target domain")
    parser.add_argument("-o", "--output", choices=["csv", "json"], default="csv", help="Output format")
    args = parser.parse_args()

    domain = args.domain
    output_format = args.output
    results = []

    # WHOIS
    console.print(Panel.fit(f"[bold cyan]WHOIS Lookup for {domain}[/bold cyan]"))
    whois_data = whois_lookup(domain)
    if whois_data:
        results.append({"type": "whois", "data": str(whois_data)})

    console.print("\n")

    # IP & Shodan
    ip_data, shodan_data = ip_and_shodan(domain)
    results.append({"type": "ip_info", "data": ip_data})
    results.append({"type": "shodan", "data": shodan_data})

    console.print("\n")

    # Subdomain Enumeration
    console.print(Panel.fit(f"[bold cyan]Subdomain Enumeration for {domain}[/bold cyan]"))
    subdomains = subdomain_enum(domain)
    for sub in subdomains:
        console.print(f"- {sub}")
    results.append({"type": "subdomains", "data": subdomains})

    console.print("\n")

    # Social Media Scraper
    username_input = input("Enter a username to check (or press Enter to use common usernames): ").strip()
    username_input = username_input if username_input else None
    social_profiles = social_scraper(username_input)
    console.print(Panel.fit(f"[bold cyan]Social Media Scraping for {domain}[/bold cyan]"))
    for profile in social_profiles:
        console.print(f"- {profile}")
    results.append({"type": "social_profiles", "data": social_profiles})

    # Export all results
    export_results(results, filename=domain.replace(".", "_"), fmt=output_format)
    console.print(Panel.fit(f"[green]Results saved to {domain.replace('.', '_')}.*{output_format}[/green]"))

if __name__ == "__main__":
    main()
