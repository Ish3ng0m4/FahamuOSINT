from shodan import Shodan
from rich import print

# Set your Shodan API key here
SHODAN_API_KEY = "m0A4zmQRcWIkTTz2ub6pw9pY1taJXY0o"  # Leave empty to skip Shodan
api = Shodan(SHODAN_API_KEY) if SHODAN_API_KEY else None

def shodan_lookup(ip):
    if not api:
        print("[yellow]Shodan API key missing, skipping Shodan lookup[/yellow]")
        return []

    try:
        result = api.host(ip)
        print(f"[bold yellow]SHODAN INFO[/bold yellow] for {ip}")
        shodan_data = []
        for item in result['data']:
            port = item.get('port')
            service = item.get('product', 'Unknown')
            print(f"- Port: {port} | Service: {service}")
            shodan_data.append({"ip": ip, "port": port, "service": service})
        return shodan_data
    except Exception as e:
        print(f"[red]Error fetching Shodan data: {e}[/red]")
        return []

