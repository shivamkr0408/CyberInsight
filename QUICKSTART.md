#  Quick Start Guide - Eye4Eye

## Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **(Optional) Install nmap for advanced scanning:**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install nmap
   
   # macOS
   brew install nmap
   ```

## Basic Usage

### Simple Scan
Scan a domain with all default options:
```bash
python eye4eye.py example.com
```

### Quick Scan (Skip Subdomains)
If you only want to scan the main domain:
```bash
python eye4eye.py example.com --skip-subdomains --main-only
```

### Fast Scan (Essential Checks Only)
Skip time-consuming scans:
```bash
python eye4eye.py example.com --skip-ports --skip-api
```

### Comprehensive Scan
Full detailed scan with nmap:
```bash
python eye4eye.py example.com --full-scan
```

## What Happens During a Scan?

### Phase 1: Subdomain Enumeration
- DNS queries using wordlist
- Certificate Transparency log lookup
- IP resolution

### Phase 2: Port Scanning
- Scans common ports (or all ports with --full-scan)
- Service detection
- Banner grabbing

### Phase 3: Technology Detection
- Web server identification
- Framework detection
- CMS identification
- Security header analysis

### Phase 4: Vulnerability Scanning
- Directory listing checks
- Exposed file detection
- Admin panel discovery
- Security configuration review

### Phase 5: API Discovery
- Common endpoint enumeration
- Documentation parsing
- JavaScript analysis

### Phase 6: Report Generation
- Interactive HTML dashboard
- JSON data export
- Visual charts and graphs

## Viewing Results

After the scan completes, you'll find two files in the `output/` directory:

1. **HTML Report**: Open in your browser for interactive visualizations
   ```bash
   # The tool will print the full path, something like:
   # file:///home/user/Eye4Eye/output/example.com_20241124_153045_report.html
   ```

2. **JSON Data**: Raw data for further analysis
   ```bash
   cat output/example.com_*_data.json | jq .
   ```

## Example Workflow

### Scenario: Quick Security Assessment
```bash
# 1. Basic scan
python eye4eye.py target.com

# 2. Open the HTML report in browser
# 3. Review findings
# 4. Export JSON for reporting
```

### Scenario: Deep Dive Analysis
```bash
# 1. Comprehensive scan
python eye4eye.py target.com --full-scan

# 2. Review all discovered subdomains
# 3. Check vulnerability findings
# 4. Investigate API endpoints
```

## Tips

- **Start Small**: Use `--main-only` for initial reconnaissance
- **Be Patient**: Full scans can take several minutes
- **Check Permissions**: Always ensure you have authorization
- **Review Output**: The HTML report is interactive - click around!
- **Save Results**: JSON files are great for tracking changes over time

## Troubleshooting

### "Connection timeout" errors
- Target may be blocking automated requests
- Try with `--skip-subdomains` or `--main-only`
- Check your internet connection

### "Nmap not found"
- Install nmap or use basic scanning (don't use `--full-scan`)

### No subdomains found
- Domain may not have many subdomains
- Certificate Transparency logs may be incomplete
- Try adding custom wordlist in `config.py`

### Permission denied
- Make sure script is executable: `chmod +x eye4eye.py`
- Run with `python eye4eye.py` instead of `./eye4eye.py`

## Next Steps

1.  Run your first scan
2.  Explore the HTML dashboard
3. 🔍 Review vulnerability findings
4.  Export and share results
5.  Customize `config.py` for your needs

## Need Help?

- Check the main README.md for detailed documentation
- Review the code in `modules/` to understand each scan type
- Open an issue on GitHub for bugs or feature requests

---

**Happy Hunting! **

Remember: Only scan systems you have permission to test!
