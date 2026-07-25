#  Eye4Eye - Attack Surface Mapper

A powerful Python tool that maps and visualizes the attack surface of any website. Combines reconnaissance, vulnerability scanning, and beautiful interactive visualizations.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

##  Features

Eye4Eye provides comprehensive attack surface analysis through:

###  Subdomain Discovery
- **DNS enumeration** with customizable wordlists
- **Certificate Transparency** log analysis
- **Interactive tree visualization** showing domain hierarchy
- IP resolution for all discovered subdomains

###  Port Scanning
- **Quick scan** of common ports (21, 22, 80, 443, etc.)
- **Full scan** option using nmap integration
- **Service detection** and banner grabbing
- **Heatmap visualization** of open ports across hosts

###  Technology Stack Detection
- **Web server** identification (Apache, Nginx, IIS)
- **Framework detection** (React, Vue, Angular, Django, etc.)
- **CMS identification** (WordPress, Joomla, Drupal, etc.)
- **HTTP header analysis** for security configurations
- **Visual tech stack graph**

###  Vulnerability Assessment
- Directory listing detection
- Exposed sensitive files (.git, .env, config files)
- Admin panel discovery
- Security header analysis
- SSL/TLS configuration check
- **Severity-based classification** (High, Medium, Low, Info)

###  API Endpoint Discovery
- Common API path enumeration
- Swagger/OpenAPI documentation parsing
- JavaScript file analysis for endpoints
- robots.txt and sitemap.xml parsing
- **Interactive sunburst visualization**

###  Visual Reports
- **Interactive HTML dashboard** with all findings
- **Network graphs** for subdomain relationships
- **Heatmaps** for port distribution
- **Charts** for vulnerability analysis
- **JSON export** for further processing

##  Installation

### Prerequisites
- Python 3.8 or higher
- nmap (optional, for advanced port scanning)

### Install nmap (optional but recommended)
```bash
# Ubuntu/Debian
sudo apt-get install nmap

# macOS
brew install nmap

# Fedora/RHEL
sudo dnf install nmap
```

### Install Python Dependencies
```bash
# Clone or navigate to the project directory
cd Eye4Eye

# Install required packages
pip install -r requirements.txt
```

##  Usage

### Basic Scan
```bash
python eye4eye.py example.com
```

### Advanced Options
```bash
# Full port scan with nmap (slower but more detailed)
python eye4eye.py example.com --full-scan

# Skip specific scan phases
python eye4eye.py example.com --skip-subdomains --skip-ports

# Scan only the main domain (skip subdomains)
python eye4eye.py example.com --main-only

# Skip vulnerability scanning
python eye4eye.py example.com --skip-vulns

# Skip API discovery
python eye4eye.py example.com --skip-api
```

### Command Line Options
```
positional arguments:
  domain              Target domain to scan

optional arguments:
  -h, --help          Show help message and exit
  --skip-subdomains   Skip subdomain enumeration
  --skip-ports        Skip port scanning
  --skip-tech         Skip technology detection
  --skip-vulns        Skip vulnerability scanning
  --skip-api          Skip API discovery
  --full-scan         Perform full port scan using nmap
  --main-only         Only scan main domain, skip subdomains
```

##  Project Structure

```
Eye4Eye/
├── eye4eye.py              # Main application
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
├── modules/                # Scanning modules
│   ├── __init__.py
│   ├── subdomain_scanner.py   # Subdomain enumeration
│   ├── port_scanner.py        # Port scanning
│   ├── tech_detector.py       # Technology detection
│   ├── vuln_scanner.py        # Vulnerability scanning
│   └── api_discovery.py       # API endpoint discovery
├── visualizations/         # Visualization components
│   ├── __init__.py
│   └── visualizer.py          # Chart and report generation
└── output/                 # Generated reports (created automatically)
    ├── domain_timestamp_report.html
    └── domain_timestamp_data.json
```

##  Output Examples

### HTML Dashboard
The tool generates a beautiful, interactive HTML dashboard featuring:
- **Real-time statistics** (subdomains, ports, vulnerabilities, endpoints)
- **Interactive visualizations** using Plotly.js
- **Dark theme** with gradient accents
- **Responsive design** for all screen sizes

### JSON Export
All data is also exported in JSON format for:
- Integration with other tools
- Custom analysis and reporting
- Automation workflows
- Long-term storage

##  Configuration

Edit `config.py` to customize:

```python
# Scanning parameters
MAX_THREADS = 50          # Concurrent threads
TIMEOUT = 5               # Request timeout in seconds

# Port scanning
COMMON_PORTS = [21, 22, 23, 25, 53, 80, ...]

# Subdomain wordlist
SUBDOMAIN_WORDLIST = ["www", "mail", "ftp", ...]

# Output settings
OUTPUT_DIR = "output"
REPORT_FORMAT = "html"
```

##  Technical Details

### Subdomain Enumeration
- Uses `dnspython` for DNS queries
- Queries Certificate Transparency logs via crt.sh
- Multi-threaded for performance
- Automatic IP resolution

### Port Scanning
- Socket-based scanning for speed
- Optional nmap integration for detailed service detection
- Banner grabbing for service identification
- Configurable port ranges

### Technology Detection
- `builtwith` library integration
- HTTP header fingerprinting
- HTML meta tag analysis
- JavaScript framework detection
- CMS pattern matching

### Vulnerability Scanning
- Path enumeration for sensitive files
- Security header validation
- SSL/TLS configuration check
- Admin panel discovery
- Directory listing detection

### API Discovery
- Common endpoint enumeration
- Swagger/OpenAPI parsing
- JavaScript source analysis
- robots.txt and sitemap parsing

##  Security & Legal

** IMPORTANT DISCLAIMER**

This tool is designed for **authorized security testing only**. You must have explicit permission to scan any target that you do not own.

- **Legal Use Only**: Unauthorized scanning is illegal in most jurisdictions
- **Responsible Disclosure**: Report vulnerabilities responsibly
- **Rate Limiting**: The tool includes delays to avoid overwhelming targets
- **No Exploitation**: This tool only discovers, it does not exploit

##  Contributing

Contributions are welcome! Areas for improvement:
- Additional vulnerability checks
- More visualization types
- Performance optimizations
- Additional data sources
- Export format options

##  License

This project is licensed under the MIT License - see the LICENSE file for details.

##  Acknowledgments

Built with:
- [dnspython](https://github.com/rthalley/dnspython) - DNS toolkit
- [python-nmap](https://github.com/nmmapper/python3-nmap) - Nmap integration
- [Plotly](https://plotly.com/python/) - Interactive visualizations
- [NetworkX](https://networkx.org/) - Graph analysis
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - HTML parsing
- [Requests](https://requests.readthedocs.io/) - HTTP library
- [Colorama](https://github.com/tartley/colorama) - Terminal colors

##  Contact

For questions, suggestions, or security concerns, please open an issue on GitHub.
