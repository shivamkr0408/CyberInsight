#  Eye4Eye - Feature Showcase

## Overview
Eye4Eye is a comprehensive attack surface mapping tool that combines multiple reconnaissance techniques with beautiful visualizations. This document showcases all major features.

---

##  Feature 1: Subdomain Discovery

### What It Does
Discovers all subdomains associated with a target domain using multiple techniques.

### Techniques Used
1. **DNS Enumeration**: Queries DNS servers with a comprehensive wordlist
2. **Certificate Transparency**: Queries crt.sh for SSL certificate records
3. **IP Resolution**: Resolves all discovered subdomains to IP addresses

### Output
- **Console**: Real-time discovery with color-coded output
- **Visualization**: Interactive tree graph showing domain hierarchy
- **Data**: JSON export with all subdomains and IPs

### Example Output
```
[+] Found: www.example.com -> 93.184.216.34
[+] Found: mail.example.com -> 93.184.216.35
[+] CT Log: api.example.com
```

### Visualization Features
- **Network Graph**: Shows relationships between domain, subdomains, and IPs
- **Interactive**: Hover for details, zoom and pan
- **Color Coded**: Root (red), Subdomains (blue), IPs (green)

---

##  Feature 2: Port Scanning

### What It Does
Identifies open ports and running services on discovered hosts.

### Scan Modes
1. **Quick Scan**: Common ports (21, 22, 80, 443, etc.)
2. **Full Scan**: All 65,535 ports using nmap integration

### Capabilities
- **Service Detection**: Identifies running services
- **Banner Grabbing**: Captures service banners
- **Version Detection**: Detects software versions (with nmap)
- **Multi-Host**: Scans main domain and subdomains

### Output
- **Console**: Port-by-port results with service info
- **Visualization**: Heatmap showing open ports across hosts
- **Data**: Detailed port and service information

### Example Output
```
[+] Port 22/tcp open - SSH-2.0-OpenSSH_7.4
[+] Port 80/tcp open - HTTP/1.1
[+] Port 443/tcp open - HTTPS
```

### Visualization Features
- **Heatmap**: Visual representation of port distribution
- **Color Intensity**: Shows port density
- **Interactive**: Hover for service details

---

##  Feature 3: Technology Stack Detection

### What It Does
Identifies web technologies, frameworks, and software running on the target.

### Detection Methods
1. **HTTP Headers**: Analyzes Server, X-Powered-By, etc.
2. **HTML Analysis**: Parses meta tags and page structure
3. **JavaScript Detection**: Identifies frontend frameworks
4. **CMS Fingerprinting**: Detects WordPress, Joomla, Drupal, etc.
5. **Library Detection**: Uses builtwith for comprehensive analysis

### Detected Technologies
- **Web Servers**: Apache, Nginx, IIS, etc.
- **Languages**: PHP, Python, Ruby, Node.js, etc.
- **Frameworks**: Django, Rails, Express, Laravel, etc.
- **Frontend**: React, Vue, Angular, jQuery, etc.
- **CMS**: WordPress, Joomla, Drupal, Magento, etc.
- **Analytics**: Google Analytics, Mixpanel, etc.
- **CDN**: Cloudflare, Akamai, etc.

### Output
- **Console**: Categorized technology list
- **Visualization**: Bar chart of detected technologies
- **Data**: Complete technology stack in JSON

### Example Output
```
[+] web-servers: nginx
[+] programming-languages: PHP
[+] javascript-frameworks: React
[+] cms: WordPress
```

### Visualization Features
- **Bar Chart**: Technologies grouped by category
- **Color Coded**: Different colors for different categories
- **Sortable**: Easy to identify technology stack

---

##  Feature 4: Vulnerability Assessment

### What It Does
Identifies potential security issues and misconfigurations.

### Vulnerability Checks

#### 1. Directory Listing
- Checks for exposed directory indexes
- Tests common paths (/images/, /uploads/, etc.)

#### 2. Exposed Files
- `.git/` directory exposure
- `.env` files
- Configuration files (wp-config.php, config.php)
- Backup files (.bak, .sql, .zip)
- Info pages (phpinfo.php)

#### 3. Admin Panels
- Common admin paths
- Login pages
- Management interfaces

#### 4. Security Headers
- X-Frame-Options (Clickjacking protection)
- X-Content-Type-Options (MIME-sniffing)
- X-XSS-Protection
- Strict-Transport-Security (HSTS)
- Content-Security-Policy (CSP)

#### 5. SSL/TLS
- HTTPS availability
- Certificate validation
- Configuration issues

### Severity Levels
-  **High**: Critical issues (exposed .git, .env files)
-  **Medium**: Significant issues (directory listings)
-  **Low**: Minor issues (missing headers)
-  **Info**: Informational findings (admin panels)

### Output
- **Console**: Real-time findings with severity
- **Visualization**: Pie chart (severity) + Bar chart (types)
- **Data**: Detailed vulnerability information

### Example Output
```
[!] Exposed File (High): /.git/config
[!] Directory Listing: /uploads/
[!] Missing Header: X-Frame-Options
[i] Admin Panel: /admin (Status: 403)
```

### Visualization Features
- **Dual Charts**: Severity distribution + Type breakdown
- **Color Coded**: Red (High), Yellow (Medium), Blue (Low)
- **Summary Stats**: Total count per severity

---

##  Feature 5: API Endpoint Discovery

### What It Does
Discovers and maps API endpoints and documentation.

### Discovery Methods

#### 1. Common Paths
- `/api/`, `/api/v1/`, `/api/v2/`
- `/rest/`, `/graphql/`
- `/swagger/`, `/api-docs/`
- `/openapi.json`, `/openapi.yaml`

#### 2. Documentation Parsing
- Swagger/OpenAPI specifications
- API documentation pages
- Endpoint listings

#### 3. JavaScript Analysis
- Scans JS files for API calls
- Extracts endpoint patterns
- Identifies API versions

#### 4. Auxiliary Files
- robots.txt analysis
- sitemap.xml parsing
- Well-known URIs

### Output
- **Console**: Discovered endpoints in real-time
- **Visualization**: Sunburst chart showing API structure
- **Data**: Complete endpoint list with metadata

### Example Output
```
[+] API Endpoint: /api/v1
  └─ /api/v1/users
  └─ /api/v1/posts
  └─ /api/v1/comments
[+] JS API Endpoint: /api/v2/auth
```

### Visualization Features
- **Sunburst Chart**: Hierarchical view of endpoints
- **Interactive**: Click to zoom into sections
- **Grouped**: Endpoints organized by base path

---

##  Feature 6: Interactive Dashboard

### What It Includes

#### 1. Header Section
- Eye4Eye branding with gradient
- Target domain display
- Scan timestamp
- Professional styling

#### 2. Statistics Cards
- Total subdomains found
- Total open ports
- Total vulnerabilities
- Total API endpoints
- Hover effects and animations

#### 3. Visualizations
All charts are interactive with:
- Zoom and pan
- Hover tooltips
- Click interactions
- Export options (PNG, SVG)

#### 4. Dark Theme
- Professional dark background
- Neon accent colors (cyan, magenta, green)
- High contrast for readability
- Glassmorphism effects

#### 5. Responsive Design
- Works on desktop and mobile
- Adaptive layouts
- Touch-friendly interactions

### Technologies Used
- **Plotly.js**: Interactive charts
- **HTML5/CSS3**: Modern web standards
- **Responsive Grid**: Flexible layouts

---

##  Feature 7: Data Export

### JSON Export
Complete scan data in structured JSON format:

```json
{
  "domain": "example.com",
  "timestamp": "2024-11-24T15:30:45",
  "subdomains": {
    "www.example.com": ["93.184.216.34"]
  },
  "ports": {
    "example.com": {
      "80": "HTTP",
      "443": "HTTPS"
    }
  },
  "technologies": {...},
  "vulnerabilities": [...],
  "api_endpoints": [...]
}
```

### Use Cases
- **Integration**: Feed data to other tools
- **Automation**: Part of CI/CD pipelines
- **Reporting**: Generate custom reports
- **Tracking**: Monitor changes over time
- **Analysis**: Deep dive with custom scripts

---

##  Design Philosophy

### Visual Excellence
- **Modern UI**: Contemporary design patterns
- **Color Psychology**: Meaningful color usage
- **Information Hierarchy**: Clear data organization
- **Accessibility**: Readable and usable

### User Experience
- **Real-time Feedback**: See results as they happen
- **Progress Indicators**: Know what's happening
- **Error Handling**: Graceful failure messages
- **Help Text**: Inline guidance

### Performance
- **Multi-threading**: Parallel execution
- **Async Operations**: Non-blocking I/O
- **Optimized Queries**: Efficient network usage
- **Caching**: Avoid redundant operations

---

##  Customization Options

### Configuration File (config.py)
```python
# Adjust scanning parameters
MAX_THREADS = 50
TIMEOUT = 5

# Customize port list
COMMON_PORTS = [21, 22, 80, 443, ...]

# Extend subdomain wordlist
SUBDOMAIN_WORDLIST = ["www", "mail", ...]

# Add vulnerability patterns
VULNERABILITY_PATTERNS = {...}
```

### Command Line Options
```bash
--skip-subdomains   # Skip subdomain enumeration
--skip-ports        # Skip port scanning
--skip-tech         # Skip technology detection
--skip-vulns        # Skip vulnerability scanning
--skip-api          # Skip API discovery
--full-scan         # Use nmap for detailed scanning
--main-only         # Only scan main domain
```

### Programmatic Usage
Import and use individual modules:
```python
from modules.subdomain_scanner import SubdomainScanner
scanner = SubdomainScanner("example.com")
results = scanner.get_all_subdomains()
```

---

##  Performance Metrics

### Typical Scan Times
- **Quick Scan**: 2-5 minutes
- **Full Scan**: 10-30 minutes
- **Subdomain Only**: 1-3 minutes
- **Port Scan Only**: 1-5 minutes

### Resource Usage
- **CPU**: Multi-threaded, scales with cores
- **Memory**: ~100-500 MB depending on results
- **Network**: Respectful rate limiting
- **Disk**: Minimal (only for reports)

---

##  Security & Ethics

### Built-in Safeguards
- **Rate Limiting**: Prevents overwhelming targets
- **Timeout Controls**: Avoids hanging connections
- **Error Handling**: Graceful failure modes
- **Legal Warnings**: Clear usage guidelines

### Best Practices
1. **Get Permission**: Always authorize before scanning
2. **Respect robots.txt**: Honor website policies
3. **Limit Scope**: Don't scan entire internet
4. **Report Responsibly**: Disclose vulnerabilities properly
5. **Document Everything**: Keep records of authorization

---

##  Future Enhancements

### Planned Features
- [ ] WHOIS information integration
- [ ] DNS zone transfer attempts
- [ ] Screenshot capture of web pages
- [ ] Automated vulnerability exploitation (ethical)
- [ ] Integration with Shodan API
- [ ] Historical tracking and diff reports
- [ ] Custom plugin system
- [ ] REST API for remote scanning
- [ ] Docker containerization
- [ ] Cloud deployment options

### Community Contributions
We welcome contributions for:
- Additional vulnerability checks
- New visualization types
- Performance improvements
- Documentation enhancements
- Bug fixes and testing

---

##  Learning Resources

### Understanding Attack Surfaces
- What is an attack surface?
- Why map attack surfaces?
- Common attack vectors
- Defense strategies

### Tool Comparisons
- **vs Shodan**: Eye4Eye is active scanning, Shodan is passive
- **vs Burp Suite**: Eye4Eye is reconnaissance, Burp is exploitation
- **vs Nmap**: Eye4Eye includes nmap plus much more
- **vs Recon-ng**: Eye4Eye has better visualizations

### Related Tools
- **Amass**: Advanced subdomain enumeration
- **Masscan**: Ultra-fast port scanner
- **Nuclei**: Vulnerability scanner
- **OWASP ZAP**: Web application scanner

---

**Eye4Eye - See the attack surface before attackers do! **
