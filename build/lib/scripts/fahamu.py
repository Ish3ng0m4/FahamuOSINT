import argparse
from fahamu_osint.whois_lookup import whois_lookup
from fahamu_osint.ip_info import get_ip
from fahamu_osint.shodan_lookup import shodan_lookup
from fahamu_osint.export_results import export_results
from fahamu_osint.subdomain_enum import subdomain_enum
from fahamu_osint.social_scraper import social_scraper

def main():
    parser = argparse.ArgumentParser(description="FahamuOSINT - Automated OSINT Tool")
    parser.add_argument("-d", "--domain", help="Target domain", required=True)
    parser.add_argument("-o", "--output", choices=["csv", "json"], default="csv", help="Output format")
    args = parser.parse_args()

    domain = args.domain
    output_format = args.output

    results = []

    # WHOIS
    whois_data = whois_lookup(domain)
    if whois_data:
        results.append({"type": "whois", "data": str(whois_data)})

    # IP + Shodan
    ip = get_ip(domain)
    if ip:
        shodan_data = shodan_lookup(ip)
        results.extend(shodan_data)

    # Subdomain Enumeration
    subdomains = subdomain_enum(domain)
    if subdomains:
        results.append({"type": "subdomains", "data": subdomains})

    # Social Media Scraping
    social_profiles = social_scraper(domain)
    if social_profiles:
        results.append({"type": "social_profiles", "data": social_profiles})

    # Export
    export_results(results, filename=domain.replace(".", "_"), fmt=output_format)

if __name__ == "__main__":
    main()
