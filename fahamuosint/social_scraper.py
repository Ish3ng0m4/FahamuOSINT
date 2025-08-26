import requests
from rich import print

# Top 50 social media platforms
SOCIAL_PLATFORMS = {
    "X": "https://x.com/{username}",
    "GitHub": "https://github.com/{username}",
    "LinkedIn": "https://www.linkedin.com/in/{username}",
    "Instagram": "https://www.instagram.com/{username}",
    "Facebook": "https://www.facebook.com/{username}",
    "TikTok": "https://www.tiktok.com/@{username}",
    "YouTube": "https://www.youtube.com/{username}",
    "Pinterest": "https://www.pinterest.com/{username}",
    "Reddit": "https://www.reddit.com/user/{username}",
    "Medium": "https://medium.com/@{username}",
    "Snapchat": "https://www.snapchat.com/add/{username}",
    "Twitch": "https://www.twitch.tv/{username}",
    "StackOverflow": "https://stackoverflow.com/users/{username}",
    "Dribbble": "https://dribbble.com/{username}",
    "Behance": "https://www.behance.net/{username}",
    "SoundCloud": "https://soundcloud.com/{username}",
    "Vimeo": "https://vimeo.com/{username}",
    "DeviantArt": "https://www.deviantart.com/{username}",
    "Flickr": "https://www.flickr.com/people/{username}",
    "Telegram": "https://t.me/{username}",
    "WhatsApp": "https://wa.me/{username}",
    "Discord": "https://discord.com/users/{username}",
    "Quora": "https://www.quora.com/profile/{username}",
    "Goodreads": "https://www.goodreads.com/{username}",
    "Tumblr": "https://{username}.tumblr.com",
    "VK": "https://vk.com/{username}",
    "Spotify": "https://open.spotify.com/user/{username}",
    "Patreon": "https://www.patreon.com/{username}",
    "Letterboxd": "https://letterboxd.com/{username}",
    "Ravelry": "https://www.ravelry.com/people/{username}",
    "Ello": "https://ello.co/{username}",
    "Mixcloud": "https://www.mixcloud.com/{username}",
    "Triller": "https://triller.co/@{username}",
    "Caffeine": "https://www.caffeine.tv/{username}",
    "WeHeartIt": "https://weheartit.com/{username}",
    "Periscope": "https://www.pscp.tv/{username}",    
    
}

# Common usernames if user does not provide any
COMMON_USERNAMES = ["admin", "info", "contact", "support", "webmaster", "help", "office", "team", "service", "enquiries"]

def social_scraper(username=None):
    results = []

    # If username is provided, use it; otherwise iterate common usernames
    usernames_to_check = [username] if username else COMMON_USERNAMES

    for user in usernames_to_check:
        print(f"\n[cyan]Checking social profiles for username: {user}[/cyan]")
        for platform, url_template in SOCIAL_PLATFORMS.items():
            url = url_template.format(username=user)
            try:
                resp = requests.head(url, timeout=5, allow_redirects=True)
                if resp.status_code == 200:
                    print(f"[green]Found {platform} profile: {url}[/green]")
                    results.append({"platform": platform, "username": user, "url": url})
            except Exception as e:
                print(f"[yellow]Error checking {platform}: {e}[/yellow]")

    return results
