# Eye4Eye - Complete Project Summary

## Project Created Successfully!

Eye4Eye is now ready to use. This is a comprehensive Python-based attack surface mapping tool with visual reporting capabilities.

## What Was Built

### Core Application
- **eye4eye.py** - Main CLI application with 6 scanning phases
- **config.py** - Centralized configuration
- **requirements.txt** - All Python dependencies
- **setup.sh** - Automated installation script with ASCII art

### Scanning Modules (modules/)
1. **subdomain_scanner.py** - DNS enumeration + Certificate Transparency
2. **port_scanner.py** - Socket scanning + nmap integration
3. **tech_detector.py** - Technology stack fingerprinting
4. **vuln_scanner.py** - Vulnerability assessment
5. **api_discovery.py** - API endpoint discovery

### Visualization Engine (visualizations/)
- **visualizer.py** - Interactive charts and HTML dashboard generation

### Documentation
- **README.md** - Complete project documentation
- **QUICKSTART.md** - 5-minute getting started guide
- **FEATURES.md** - Detailed feature showcase
- **PROJECT_SUMMARY.md** - Technical overview
- **INSTALLATION.md** - Installation troubleshooting
- **LICENSE** - MIT License
- **examples.py** - Programmatic usage examples

## Key Features

### 1. Subdomain Discovery
- DNS wordlist enumeration
- Certificate Transparency log queries
- IP resolution
- Interactive tree visualization

### 2. Port Scanning
- Quick scan (common ports)
- Full scan (nmap integration)
- Service detection
- Banner grabbing
- Heatmap visualization

### 3. Technology Detection
- Web server identification
- Framework detection
- CMS fingerprinting
- Security header analysis
- Bar chart visualization

### 4. Vulnerability Assessment
- Directory listing detection
- Exposed file discovery
- Admin panel enumeration
- Security header validation
- SSL/TLS configuration check
- Severity-based classification

### 5. API Discovery
- Common endpoint enumeration
- Swagger/OpenAPI parsing
- JavaScript analysis
- robots.txt/sitemap parsing
- Sunburst chart visualization

### 6. Visual Reporting
- Interactive HTML dashboard
- Real-time statistics
- Multiple chart types
- Dark theme with neon accents
- JSON data export

## File Structure

```
Eye4Eye/
├── eye4eye.py                    # Main application
├── config.py                     # Configuration
├── requirements.txt              # Dependencies
├── setup.sh                      # Setup script (with ASCII eye)
├── examples.py                   # Usage examples
│
├── modules/                      # Scanning modules
│   ├── __init__.py
│   ├── subdomain_scanner.py
│   ├── port_scanner.py
│   ├── tech_detector.py
│   ├── vuln_scanner.py
│   └── api_discovery.py
│
├── visualizations/               # Visualization engine
│   ├── __init__.py
│   └── visualizer.py
│
├── output/                       # Generated reports
│   └── README.md
│
└── docs/                         # Documentation
    ├── README.md
    ├── QUICKSTART.md
    ├── FEATURES.md
    ├── PROJECT_SUMMARY.md
    ├── INSTALLATION.md
    ├── LICENSE
    └── .gitignore
```

## How to Use

### Quick Start
```bash
# 1. Install dependencies
./setup.sh

# 2. Run a scan
python3 eye4eye.py example.com

# 3. View the report
# Open output/example.com_TIMESTAMP_report.html in browser
```

### Command Line Options
```bash
python3 eye4eye.py example.com                    # Full scan
python3 eye4eye.py example.com --skip-subdomains  # Skip subdomain phase
python3 eye4eye.py example.com --full-scan        # Use nmap
python3 eye4eye.py example.com --main-only        # Only main domain
python3 eye4eye.py example.com --help             # Show all options
```

### Programmatic Usage
```python
from modules.subdomain_scanner import SubdomainScanner

scanner = SubdomainScanner("example.com")
results = scanner.get_all_subdomains()
print(f"Found {len(results)} subdomains")
```

## Technical Stack

### Core Technologies
- Python 3.8+
- dnspython (DNS queries)
- python-nmap (port scanning)
- requests (HTTP operations)
- BeautifulSoup4 (HTML parsing)

### Visualization
- Plotly (interactive charts)
- NetworkX (graph analysis)
- HTML5/CSS3 (dashboard)

### Performance
- Multi-threading (concurrent scanning)
- Async I/O (non-blocking operations)
- Connection pooling (efficient networking)

## Output Examples

### Console Output
```
Eye4Eye - Attack Surface Mapper v1.0.0
Target: example.com
================================================

[*] Phase 1: Subdomain Enumeration
[+] Found: www.example.com -> 93.184.216.34
[+] Found: mail.example.com -> 93.184.216.35

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

Scan Complete!
Summary:
  • Subdomains: 15
  • Open Ports: 8
  • Vulnerabilities: 12
  • API Endpoints: 7
```

### HTML Dashboard Features
- Statistics cards (subdomains, ports, vulns, APIs)
- Subdomain tree graph (interactive network)
- Port heatmap (visual distribution)
- Technology stack chart (bar chart)
- Vulnerability analysis (pie + bar charts)
- API endpoint map (sunburst chart)
- Dark theme with gradients
- Responsive design
- Export options (PNG, SVG)

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

## Configuration

Edit `config.py` to customize:

```python
# Performance
MAX_THREADS = 50
TIMEOUT = 5

# Ports to scan
COMMON_PORTS = [21, 22, 80, 443, ...]

# Subdomain wordlist
SUBDOMAIN_WORDLIST = ["www", "mail", "ftp", ...]

# Output directory
OUTPUT_DIR = "output"
```

## Security & Legal

**IMPORTANT**: This tool is for authorized security testing ONLY.

- Get explicit permission before scanning
- Unauthorized access is illegal
- Respect rate limits
- Report vulnerabilities responsibly
- Document all authorization

## Performance

### Typical Scan Times
- Quick scan: 2-5 minutes
- Full scan: 10-30 minutes
- Subdomain only: 1-3 minutes
- Port scan only: 1-5 minutes

### Resource Usage
- CPU: Scales with cores
- Memory: 100-500 MB
- Network: Respectful rate limiting
- Disk: Minimal (reports only)

## Customization

### Custom Wordlist
```python
from modules.subdomain_scanner import SubdomainScanner

scanner = SubdomainScanner("example.com")
custom_list = ["www", "api", "dev", "staging"]
results = scanner.enumerate_subdomains(wordlist=custom_list)
```

### Custom Ports
```python
from modules.port_scanner import PortScanner

scanner = PortScanner("example.com")
custom_ports = [80, 443, 8080, 8443]
results = scanner.quick_scan(ports=custom_ports)
```

### Custom Visualization
```python
from visualizations.visualizer import AttackSurfaceVisualizer

viz = AttackSurfaceVisualizer("example.com")
fig = viz.create_subdomain_tree(subdomain_data)
fig.write_html("custom_report.html")
```

## Troubleshooting

### Installation Issues
- Run `./setup.sh` for automated setup
- Check Python version: `python3 --version`
- Install dependencies: `pip3 install -r requirements.txt`
- See INSTALLATION.md for details

### Runtime Issues
- Connection timeout: Check internet connection
- Permission denied: `chmod +x eye4eye.py`
- Module not found: `pip3 install <module>`
- nmap not found: Install nmap or skip --full-scan

## Next Steps

1. Run the setup script: `./setup.sh`
2. Read QUICKSTART.md
3. Try examples: `python3 examples.py`
4. Run your first scan: `python3 eye4eye.py example.com`
5. Explore the HTML dashboard
6. Review the documentation

## Documentation Files

- **README.md** - Main documentation with features and usage
- **QUICKSTART.md** - Get started in 5 minutes
- **FEATURES.md** - Detailed feature showcase with examples
- **PROJECT_SUMMARY.md** - Technical architecture overview
- **INSTALLATION.md** - Installation and troubleshooting
- **examples.py** - Code examples for programmatic use

## Special Features

### ASCII Eye Art
The setup script displays a custom ASCII eye art banner

### No Emojis
All documentation is emoji-free for better compatibility

### Modular Design
Each component can be used independently

### Professional Output
Client-ready HTML reports with interactive visualizations

### JSON Export
Complete data export for automation and integration

## License

MIT License - Free and open source

## Credits

Built with:
- dnspython, python-nmap, requests, BeautifulSoup4
- Plotly, NetworkX, colorama, pyfiglet
- builtwith, aiohttp, pandas

## Support

For help:
1. Check documentation files
2. Review examples.py
3. Read module source code
4. Open GitHub issue

---

## Quick Command Reference

```bash
# Setup
./setup.sh

# Basic scan
python3 eye4eye.py example.com

# Advanced options
python3 eye4eye.py example.com --full-scan
python3 eye4eye.py example.com --skip-subdomains
python3 eye4eye.py example.com --main-only

# Help
python3 eye4eye.py --help

# Examples
python3 examples.py

# View report
# Open output/*.html in browser
```

---

**Eye4Eye - See the attack surface before attackers do!**

*For authorized security testing only. Use responsibly and ethically.*
