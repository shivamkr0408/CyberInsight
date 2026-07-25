#  Eye4Eye - Project Summary

## Project Overview

**Eye4Eye** is a comprehensive Python-based attack surface mapping tool that combines multiple reconnaissance techniques with beautiful interactive visualizations. It's designed for security professionals, penetration testers, and bug bounty hunters who need to understand the complete attack surface of a target domain.

## What Makes Eye4Eye Unique?

### 1. **All-in-One Solution**
Instead of using 5-10 different tools, Eye4Eye combines:
- Subdomain enumeration (like Amass)
- Port scanning (like Nmap)
- Technology detection (like Wappalyzer)
- Vulnerability scanning (like Nikto)
- API discovery (like Burp Suite)
- Beautiful visualizations (unique to Eye4Eye)

### 2. **Visual Intelligence**
Unlike traditional CLI tools, Eye4Eye generates:
- **Interactive HTML dashboards** with Plotly.js charts
- **Network graphs** showing domain relationships
- **Heatmaps** for port distribution
- **Sunburst charts** for API structure
- **Professional reports** ready to share with clients

### 3. **Modular Architecture**
Each component can be used independently:
```python
from modules.subdomain_scanner import SubdomainScanner
scanner = SubdomainScanner("example.com")
results = scanner.get_all_subdomains()
```

### 4. **Production Ready**
- Multi-threaded for performance
- Async operations where appropriate
- Error handling and graceful failures
- Configurable timeouts and rate limiting
- JSON export for automation

## Core Components

###  Project Structure
```
Eye4Eye/
├── eye4eye.py                 # Main application (CLI)
├── config.py                  # Configuration settings
├── requirements.txt           # Python dependencies
├── setup.sh                   # Automated setup script
├── examples.py                # Usage examples
│
├── modules/                   # Scanning modules
│   ├── subdomain_scanner.py   # DNS enumeration + CT logs
│   ├── port_scanner.py        # Socket + nmap scanning
│   ├── tech_detector.py       # Technology fingerprinting
│   ├── vuln_scanner.py        # Vulnerability assessment
│   └── api_discovery.py       # API endpoint discovery
│
├── visualizations/            # Visualization engine
│   └── visualizer.py          # Plotly-based charts + HTML dashboard
│
├── output/                    # Generated reports
│   ├── *.html                 # Interactive dashboards
│   └── *.json                 # Raw data exports
│
└── docs/                      # Documentation
    ├── README.md              # Main documentation
    ├── QUICKSTART.md          # Quick start guide
    └── FEATURES.md            # Feature showcase
```

## Technical Stack

### Core Technologies
- **Python 3.8+**: Main language
- **dnspython**: DNS queries and resolution
- **python-nmap**: Advanced port scanning
- **requests**: HTTP operations
- **BeautifulSoup4**: HTML parsing
- **Plotly**: Interactive visualizations
- **NetworkX**: Graph analysis
- **aiohttp**: Async HTTP requests

### Visualization
- **Plotly.js**: Interactive charts
- **HTML5/CSS3**: Dashboard UI
- **Responsive design**: Works on all devices

### Performance
- **Multi-threading**: Concurrent scanning
- **Async I/O**: Non-blocking operations
- **Connection pooling**: Efficient network usage
- **Smart caching**: Avoid redundant queries

## Key Features Breakdown

###  Subdomain Discovery
**Methods:**
- DNS wordlist enumeration (customizable)
- Certificate Transparency logs (crt.sh)
- Automatic IP resolution

**Output:**
- Real-time console updates
- Interactive tree visualization
- Complete subdomain-to-IP mapping

###  Port Scanning
**Modes:**
- Quick scan (common ports)
- Full scan (all 65,535 ports with nmap)

**Features:**
- Service detection
- Banner grabbing
- Version identification
- Multi-host support

###  Technology Detection
**Identifies:**
- Web servers (Apache, Nginx, IIS)
- Programming languages (PHP, Python, Ruby, Node.js)
- Frameworks (Django, Rails, Laravel, Express)
- Frontend (React, Vue, Angular, jQuery)
- CMS (WordPress, Joomla, Drupal)
- CDN, Analytics, and more

###  Vulnerability Assessment
**Checks:**
- Directory listings
- Exposed files (.git, .env, configs)
- Admin panels
- Security headers
- SSL/TLS configuration

**Severity Levels:**
- High (critical issues)
- Medium (significant issues)
- Low (minor issues)
- Info (informational)

###  API Discovery
**Discovers:**
- Common API paths
- Swagger/OpenAPI docs
- JavaScript API calls
- robots.txt references
- Sitemap entries

###  Visualizations
**Dashboard Includes:**
- Statistics cards (subdomains, ports, vulns, APIs)
- Subdomain tree graph
- Port heatmap
- Technology stack chart
- Vulnerability analysis charts
- API endpoint sunburst

## Usage Scenarios

### Scenario 1: Bug Bounty Reconnaissance
```bash
# Quick initial scan
python3 eye4eye.py target.com --main-only

# Deep dive after finding interesting subdomains
python3 eye4eye.py target.com --full-scan
```

### Scenario 2: Penetration Testing
```bash
# Comprehensive scan for pentest report
python3 eye4eye.py client.com

# Generate professional HTML report
# Share output/client.com_*_report.html with client
```

### Scenario 3: Security Monitoring
```bash
# Regular scans to track changes
python3 eye4eye.py company.com

# Compare JSON outputs over time
diff output/company.com_old.json output/company.com_new.json
```

### Scenario 4: Custom Integration
```python
# Use as a library in your own tools
from modules.subdomain_scanner import SubdomainScanner
from modules.vuln_scanner import VulnerabilityScanner

scanner = SubdomainScanner("example.com")
subdomains = scanner.get_all_subdomains()

for subdomain in subdomains:
    vuln_scanner = VulnerabilityScanner(f"https://{subdomain}")
    vulns = vuln_scanner.scan_all()
    # Process vulnerabilities...
```

## Installation & Setup

### Quick Start
```bash
# 1. Navigate to project directory
cd Eye4Eye

# 2. Run automated setup
./setup.sh

# 3. Start scanning
python3 eye4eye.py example.com
```

### Manual Installation
```bash
# Install dependencies
pip3 install -r requirements.txt

# Install nmap (optional)
sudo apt-get install nmap  # Ubuntu/Debian

# Make scripts executable
chmod +x eye4eye.py examples.py

# Run
python3 eye4eye.py --help
```

## Configuration

### Customize Scanning (config.py)
```python
# Performance
MAX_THREADS = 50        # Concurrent threads
TIMEOUT = 5             # Request timeout

# Ports
COMMON_PORTS = [21, 22, 80, 443, ...]

# Subdomains
SUBDOMAIN_WORDLIST = ["www", "mail", ...]

# Output
OUTPUT_DIR = "output"
```

### Command Line Options
```bash
--skip-subdomains   # Skip subdomain phase
--skip-ports        # Skip port scanning
--skip-tech         # Skip tech detection
--skip-vulns        # Skip vulnerability scan
--skip-api          # Skip API discovery
--full-scan         # Use nmap (slower, detailed)
--main-only         # Only scan main domain
```

## Output Examples

### Console Output
```
 Eye4Eye - Attack Surface Mapper v1.0.0
Target: example.com
================================================

[*] Phase 1: Subdomain Enumeration
[+] Found: www.example.com -> 93.184.216.34
[+] Found: mail.example.com -> 93.184.216.35
[+] CT Log: api.example.com

[*] Phase 2: Port Scanning
[+] Port 80/tcp open - HTTP
[+] Port 443/tcp open - HTTPS

[*] Phase 3: Technology Detection
[+] web-servers: nginx
[+] cms: WordPress

[*] Phase 4: Vulnerability Scanning
[!] Exposed File (High): /.git/config
[!] Missing Header: X-Frame-Options

[*] Phase 5: API Discovery
[+] API Endpoint: /api/v1

[*] Phase 6: Generating Visualizations
[+] HTML report saved: output/example.com_20241124_153045_report.html
[+] JSON data saved: output/example.com_20241124_153045_data.json

 Scan Complete!
Summary:
  • Subdomains: 15
  • Open Ports: 8
  • Vulnerabilities: 12
  • API Endpoints: 7
```

### HTML Dashboard
- **Modern dark theme** with neon accents
- **Interactive charts** (zoom, pan, hover)
- **Responsive design** (mobile-friendly)
- **Professional layout** (client-ready)
- **Export options** (PNG, SVG)

### JSON Export
```json
{
  "domain": "example.com",
  "timestamp": "2024-11-24T15:30:45",
  "subdomains": {...},
  "ports": {...},
  "technologies": {...},
  "vulnerabilities": [...],
  "api_endpoints": [...]
}
```

## Performance Metrics

### Typical Scan Times
- **Quick scan**: 2-5 minutes
- **Full scan**: 10-30 minutes
- **Subdomain only**: 1-3 minutes
- **Port scan only**: 1-5 minutes

### Resource Usage
- **CPU**: Scales with available cores
- **Memory**: 100-500 MB
- **Network**: Respectful rate limiting
- **Disk**: Minimal (reports only)

## Security & Ethics

###  Legal Disclaimer
**This tool is for authorized security testing ONLY.**

- Get explicit permission before scanning
- Unauthorized access is illegal
- Respect rate limits and robots.txt
- Report vulnerabilities responsibly
- Document all authorization

### Built-in Safeguards
- Configurable timeouts
- Rate limiting
- Error handling
- Legal warnings
- Respectful scanning

## Future Roadmap

### Planned Features
- [ ] WHOIS integration
- [ ] Screenshot capture
- [ ] Shodan API integration
- [ ] Historical tracking
- [ ] Custom plugins
- [ ] REST API
- [ ] Docker support
- [ ] Cloud deployment

### Community
- Contributions welcome
- Bug reports appreciated
- Feature requests considered
- Documentation improvements needed

## Comparison with Other Tools

| Feature | Eye4Eye | Shodan | Burp Suite | Nmap | Amass |
|---------|---------|--------|------------|------|-------|
| Subdomain Discovery |  |  |  |  |  |
| Port Scanning |  |  |  |  |  |
| Tech Detection |  |  |  |  |  |
| Vuln Scanning |  |  |  |  |  |
| API Discovery |  |  |  |  |  |
| Visualizations |  |  |  |  |  |
| Free & Open Source |  |  |  |  |  |
| Easy to Use |  |  |  |  |  |

## Documentation

### Available Guides
- **README.md**: Complete documentation
- **QUICKSTART.md**: Get started in 5 minutes
- **FEATURES.md**: Detailed feature showcase
- **examples.py**: Programmatic usage examples

### Learning Resources
- Code comments throughout
- Modular design for easy understanding
- Example scripts included
- Configuration well-documented

## Credits & Acknowledgments

### Built With
- dnspython, python-nmap, requests, BeautifulSoup4
- Plotly, NetworkX, colorama, pyfiglet
- builtwith, aiohttp, pandas

### Inspired By
- Shodan (passive reconnaissance)
- Burp Suite (web app testing)
- Amass (subdomain enumeration)
- Nmap (port scanning)

### License
MIT License - See LICENSE file

## Contact & Support

### Getting Help
- Read the documentation
- Check examples.py
- Review module source code
- Open GitHub issue

### Contributing
- Fork the repository
- Create feature branch
- Submit pull request
- Follow code style

---

## Quick Reference

### Installation
```bash
./setup.sh
```

### Basic Usage
```bash
python3 eye4eye.py example.com
```

### Advanced Usage
```bash
python3 eye4eye.py example.com --full-scan --main-only
```

### Programmatic
```python
from modules.subdomain_scanner import SubdomainScanner
scanner = SubdomainScanner("example.com")
results = scanner.get_all_subdomains()
```

### Output
```
output/example.com_TIMESTAMP_report.html  # Interactive dashboard
output/example.com_TIMESTAMP_data.json    # Raw data
```

---

**Eye4Eye - See the attack surface before attackers do! **

*For authorized security testing only. Use responsibly and ethically.*
