# FahamuOSINT
![FahamuOSINT Logo](https://github.com/Ish3ng0m4/FahamuOSINT/blob/4e024ed8b477b9b60c4ddf2588049c1affecba55/FahamuOSINT%20Logo.png)
Is an Automated OSINT Reconnaissance Tool
FahamuOSINT is a Python-based OSINT tool that helps red teamers, pentesters and security researchers gather information about domains efficiently. It performs WHOIS lookups, IP & Shodan scans, subdomain enumeration and social media scraping. Results can be exported in CSV or JSON format.


## Features
<b>WHOIS Lookup:</b> Get domain registration informations.<br>
<b>IP and Shodan Scan:</b> Resolve domain to IP and check exposed services.<br>
<b>Subdomain Enumeration:</b> Using crt.sh, local/online wordlists or custom wordlists.<br>
<b>Social Media Scraper:</b> Checks top 50 social media platforms for usernames or default common ones.<br>
<b>Export Results:</b> CSV or JSON output for easy analysis.<br>
<b>Rich Console Output:</b> Colorful and readable results.


## Requirements
Python 3.10+ <br>
Pip packages: requests, python-whois, shodan, rich, pandas <br>
Shodan API Key (for Shodan scans)


## Installation
1. Clone the repository <br>
   `git clone https://github.com/Ish3ng0m4/FahamuOSINT.git` <br>
    `cd FahamuOSINT`

3. Set up Python virtual environment (optional but highly recommended) <br>
   `python3 -m venv Fahamuvenv` <br>
   `source Fahamuvenv/bin/activate`

3. Install dependencies <br>
   `pip install -r requirements.txt`


## Usage <br>
Command: `python3 -m scripts.fahamu -d example.com -o csv`

### Arguments
| Flag           | Description                     | Default  |
| -------------- | ------------------------------- | -------- |
| `-d, --domain` | Target domain                   | Required |
| `-o, --output` | Output format (`csv` or `json`) | `csv`    |



### Example Run
#### Command
`python3 -m scripts.fahamu -d example.com -o csv`

#### Output
`example.com_results_1.csv` → WHOIS <br>
`example.com_results_2.csv` → IP info <br>
`example.com_results_3.csv` → Shodan <br>
`example.com_results_4.csv` → Subdomains <br>
`example.com_results_5.csv` → Social Media Profiles


## Subdomain Wordlists
1. Uses local 1,613,291-entry wordlist: `common-crawl-subdomains-10000.txt`
2. Optionally, users can provide custom wordlists.
3. Online sources fallback: crt.sh


## Social Media Scraper
1. Checks top 50 platforms including Twitter (X), Facebook, LinkedIn, GitHub, Instagram, etc.
2. Users can provide a username, otherwise uses common usernames.


## License
under MIT & ICTC License free for personal and professional use.


# Contact
Gabriel D Ishengoma | <a href="https://github.com/Ish3ng0m4">GitHub</a>
