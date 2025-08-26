# FahamuOSINT

Is an Automated OSINT Reconnaissance Tool
FahamuOSINT is a Python-based OSINT tool that helps red teamers, pentesters and security researchers gather information about domains efficiently. It performs WHOIS lookups, IP & Shodan scans, subdomain enumeration and social media scraping. Results can be exported in CSV or JSON format.

## Features
<b>WHOIS Lookup:</b> Get domain registration info.

<b>IP and Shodan Scan:</b> Resolve domain to IP, check exposed services.

<b>Subdomain Enumeration:</b> Using crt.sh, local/online wordlists, or custom wordlists.

<b>Social Media Scraper:</b> Checks top 50 social media platforms for usernames or default common ones.

<b>Export Results:</b> CSV or JSON output for easy analysis.

<b>Rich Console Output:</b> Colorful, readable results.


## Requirements
Python 3.10+
Pip packages: requests, python-whois, shodan, rich, pandas
Shodan API Key (for Shodan scans)
