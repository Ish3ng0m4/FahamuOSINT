from shodan import Shodan
from rich import print

SHODAN_API_KEY = "m0A4zmQRcWIkTTz2ub6pw9pY1taJXY0o"  # Replace with your key
api = Shodan(SHODAN_API_KEY)

def shodan_lookup(ip):
    try:
        result = api.host(ip)
        print(f"[bold yellow]SHODAN INFO[/bold yellow] for {ip}")
        shodan_data = []
        for item in result['data']:
            port = item.get('port')
            service = item.get('product', 'Unknown')
            print(f"Port: {port} | Service: {service}")
            shodan_data.append({"ip": ip, "port": port, "service": service})
        return shodan_data
    except Exception as e:
        print(f"[red]Error fetching Shodan data: {e}[/red]")
        return []
