# FahamuOSINT

Is an Automated OSINT Reconnaissance Tool
FahamuOSINT is a Python-based OSINT tool that helps red teamers, pentesters and security researchers gather information about domains efficiently. It performs WHOIS lookups, IP & Shodan scans, subdomain enumeration and social media scraping. Results can be exported in CSV or JSON format.


## Features
<b>WHOIS Lookup:</b> Get domain registration info.<br>
<b>IP and Shodan Scan:</b> Resolve domain to IP, check exposed services.<br>
<b>Subdomain Enumeration:</b> Using crt.sh, local/online wordlists, or custom wordlists.<br>
<b>Social Media Scraper:</b> Checks top 50 social media platforms for usernames or default common ones.<br>
<b>Export Results:</b> CSV or JSON output for easy analysis.<br>
<b>Rich Console Output:</b> Colorful, readable results.


## Requirements
Python 3.10+ <br>
Pip packages: requests, python-whois, shodan, rich, pandas <br>
Shodan API Key (for Shodan scans)


## Installation
1. Clone the repository <br>
   `git clone https://github.com/Ish3ng0m4/FahamuOSINT.git` <br>
    `cd FahamuOSINT`

3. Set up Python virtual environment (optional but highly recommended) <br>
   `python3 -m venv venv` <br>
   `source venv/bin/activate`

3. Install dependencies <br>
   `pip install -r requirements.txt`


## Usage <br>
Command: `python3 -m scripts.fahamu -d example.com -o csv`

### Arguments
| Flag           | Description                     | Default  |
| -------------- | ------------------------------- | -------- |
| `-d, --domain` | Target domain                   | Required |
| `-o, --output` | Output format (`csv` or `json`) | `csv`    |
