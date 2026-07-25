"""
Configuration file for Eye4Eye - Attack Surface Mapper
"""

# Scanning Configuration
MAX_THREADS = 50
TIMEOUT = 5
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

# Port Scanning
COMMON_PORTS = [
    21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 
    3306, 3389, 5432, 5900, 8000, 8080, 8443, 8888, 9090
]

FULL_PORT_RANGE = range(1, 65536)

# Subdomain Enumeration
SUBDOMAIN_WORDLIST = [
    "www", "mail", "ftp", "localhost", "webmail", "smtp", "pop", "ns1", "webdisk",
    "ns2", "cpanel", "whm", "autodiscover", "autoconfig", "m", "imap", "test",
    "ns", "blog", "pop3", "dev", "www2", "admin", "forum", "news", "vpn",
    "ns3", "mail2", "new", "mysql", "old", "lists", "support", "mobile", "mx",
    "static", "docs", "beta", "shop", "sql", "secure", "demo", "cp", "calendar",
    "wiki", "web", "media", "email", "images", "img", "www1", "intranet",
    "portal", "video", "sip", "dns2", "api", "cdn", "stats", "dns1", "ns4",
    "www3", "dns", "search", "staging", "server", "mx1", "chat", "wap", "my",
    "svn", "mail1", "sites", "proxy", "ads", "host", "crm", "cms", "backup",
    "mx2", "lyncdiscover", "info", "apps", "download", "remote", "db", "forums",
    "store", "relay", "files", "newsletter", "app", "live", "owa", "en", "start",
    "sms", "office", "exchange", "ipv4", "git", "upload", "media1", "ssl"
]

# Vulnerability Patterns
VULNERABILITY_PATTERNS = {
    "Directory Listing": ["Index of /", "Parent Directory"],
    "Default Pages": ["Apache2 Ubuntu Default Page", "IIS Windows Server", "Welcome to nginx"],
    "Exposed Git": [".git/config", ".git/HEAD"],
    "Exposed Env": [".env", "config.php", "configuration.php"],
    "Admin Panels": ["/admin", "/administrator", "/wp-admin", "/phpmyadmin"],
    "Backup Files": [".bak", ".backup", ".old", ".sql", ".zip"],
    "Information Disclosure": ["phpinfo()", "Server: ", "X-Powered-By"],
}

# API Endpoint Patterns
API_PATTERNS = [
    "/api/v1/", "/api/v2/", "/api/", "/rest/", "/graphql",
    "/v1/", "/v2/", "/v3/", "/swagger", "/api-docs",
    "/openapi.json", "/api.json", "/endpoints"
]

# Output Configuration
OUTPUT_DIR = "output"
REPORT_FORMAT = "html"  # html, json, pdf

# Colors for terminal output
COLORS = {
    "HEADER": "\033[95m",
    "OKBLUE": "\033[94m",
    "OKCYAN": "\033[96m",
    "OKGREEN": "\033[92m",
    "WARNING": "\033[93m",
    "FAIL": "\033[91m",
    "ENDC": "\033[0m",
    "BOLD": "\033[1m",
    "UNDERLINE": "\033[4m",
}
