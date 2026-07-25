# Eye4Eye - Installation Guide

## Quick Installation

### Step 1: Run Setup Script
```bash
cd Eye4Eye
./setup.sh
```

The setup script will:
- Check Python version (requires 3.8+)
- Install all Python dependencies
- Check for nmap (optional)
- Make scripts executable
- Test the installation

### Step 2: Verify Installation
```bash
python3 eye4eye.py --help
```

You should see the help menu with all available options.

## Manual Installation

If the automated setup fails, follow these manual steps:

### 1. Check Python Version
```bash
python3 --version
```
Ensure you have Python 3.8 or higher.

### 2. Install Dependencies
```bash
pip3 install -r requirements.txt
```

### 3. Install nmap (Optional but Recommended)
```bash
# Ubuntu/Debian
sudo apt-get install nmap

# macOS
brew install nmap

# Fedora/RHEL
sudo dnf install nmap
```

### 4. Make Scripts Executable
```bash
chmod +x eye4eye.py
chmod +x examples.py
chmod +x setup.sh
```

### 5. Test Installation
```bash
python3 -c "import dns.resolver, requests, plotly, networkx, colorama, pyfiglet; print('All modules imported successfully!')"
```

## Troubleshooting

### Issue: ModuleNotFoundError
**Solution**: Install the missing module
```bash
pip3 install <module-name>
```

### Issue: Permission Denied
**Solution**: Make the script executable
```bash
chmod +x eye4eye.py
```

### Issue: nmap not found
**Solution**: Either install nmap or use basic scanning (don't use --full-scan flag)

### Issue: DNS Resolution Fails
**Solution**: Check your internet connection and DNS settings

## System Requirements

### Minimum Requirements
- Python 3.8 or higher
- 512 MB RAM
- 100 MB disk space
- Internet connection

### Recommended Requirements
- Python 3.9 or higher
- 2 GB RAM
- 500 MB disk space
- Stable internet connection
- nmap installed

## Dependencies

All dependencies are listed in `requirements.txt`:

- dnspython - DNS queries
- requests - HTTP operations
- beautifulsoup4 - HTML parsing
- python-nmap - Port scanning
- plotly - Visualizations
- networkx - Graph analysis
- colorama - Terminal colors
- tqdm - Progress bars
- pyfiglet - ASCII art
- builtwith - Tech detection
- aiohttp - Async HTTP
- pandas - Data processing
- kaleido - Image export

## Next Steps

After installation:

1. Read the QUICKSTART.md guide
2. Try the examples: `python3 examples.py`
3. Run your first scan: `python3 eye4eye.py example.com`
4. Review the generated HTML report

## Getting Help

If you encounter issues:
1. Check this installation guide
2. Review the README.md
3. Check the examples.py file
4. Open an issue on GitHub

---

For more information, see README.md and QUICKSTART.md
