import requests
from rich import print

SOCIAL_PLATFORMS = {
    "Twitter": "https://twitter.com/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "GitHub": "https://github.com/{}",
}

def social_scraper(domain):
    print(f"[bold cyan]Social Media Scraping[/bold cyan] for {domain}")
    possible_usernames = [domain.split('.')[0], "admin", "info", "contact"]
    found_profiles = []

    for platform, url_template in SOCIAL_PLATFORMS.items():
        for username in possible_usernames:
            url = url_template.format(username)
            try:
                resp = requests.get(url, timeout=5)
                if resp.status_code == 200:
                    print(f"[green]Found {platform} profile: {url}[/green]")
                    found_profiles.append({"platform": platform, "username": username, "url": url})
            except Exception as e:
                print(f"[red]Error checking {url}: {e}[/red]")

    if not found_profiles:
        print("[yellow]No public profiles found[/yellow]")
    return found_profiles
