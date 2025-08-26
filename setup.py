from setuptools import setup, find_packages

setup(
    name="fahamu_osint",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "whois",
        "shodan",
        "dnspython",
        "pandas",
        "rich",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "fahamu=fahamu_osint.cli:main",
        ],
    },
    author="Gabriel D Ishengoma (Ish3ng0m4)",
    description="Automated OSINT reconnaissance tool",
    url="https://github.com/Ish3ng0m4/FahamuOSINT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Security",
    ],
)
