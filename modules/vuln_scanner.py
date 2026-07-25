"""
Vulnerability Scanner Module
Checks for common vulnerabilities and misconfigurations
"""

import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from config import VULNERABILITY_PATTERNS, USER_AGENT, TIMEOUT
from colorama import Fore, Style
from concurrent.futures import ThreadPoolExecutor
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VulnerabilityScanner:
    def __init__(self, url: str):
        self.url = url if url.startswith('http') else f'http://{url}'
        self.vulnerabilities: List[Dict] = []
        self.headers = {'User-Agent': USER_AGENT}
        
    def check_path(self, path: str) -> tuple:
        """Check if a path exists and is accessible"""
        try:
            full_url = f"{self.url}{path}"
            response = requests.get(full_url, headers=self.headers, 
                                  timeout=TIMEOUT, verify=False, allow_redirects=False)
            return (path, response.status_code, response.text[:500])
        except:
            return None
    
    def check_directory_listing(self) -> List[Dict]:
        """Check for directory listing vulnerabilities"""
        print(f"\n{Fore.CYAN}[*] Checking for directory listings...{Style.RESET_ALL}")
        
        findings = []
        test_paths = ['/', '/images/', '/assets/', '/uploads/', '/files/', '/backup/', '/admin/']
        
        for path in test_paths:
            result = self.check_path(path)
            if result:
                _, status, content = result
                if status == 200:
                    for pattern in VULNERABILITY_PATTERNS['Directory Listing']:
                        if pattern in content:
                            vuln = {
                                'type': 'Directory Listing',
                                'severity': 'Medium',
                                'path': path,
                                'description': f'Directory listing enabled at {path}'
                            }
                            findings.append(vuln)
                            self.vulnerabilities.append(vuln)
                            print(f"{Fore.YELLOW}[!] Directory Listing: {path}{Style.RESET_ALL}")
                            break
        
        return findings
    
    def check_exposed_files(self) -> List[Dict]:
        """Check for exposed sensitive files"""
        print(f"\n{Fore.CYAN}[*] Checking for exposed sensitive files...{Style.RESET_ALL}")
        
        findings = []
        sensitive_files = [
            '/.git/config', '/.git/HEAD', '/.env', '/.env.local', '/.env.production',
            '/config.php', '/configuration.php', '/wp-config.php', '/web.config',
            '/.htaccess', '/phpinfo.php', '/info.php', '/test.php',
            '/backup.sql', '/backup.zip', '/database.sql', '/db.sql',
            '/.DS_Store', '/composer.json', '/package.json', '/.gitignore',
            '/robots.txt', '/sitemap.xml', '/.well-known/security.txt'
        ]
        
        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = [executor.submit(self.check_path, path) for path in sensitive_files]
            
            for future in futures:
                result = future.result()
                if result:
                    path, status, content = result
                    if status == 200:
                        severity = 'High' if any(x in path for x in ['.git', '.env', 'config', 'backup', '.sql']) else 'Low'
                        vuln = {
                            'type': 'Exposed File',
                            'severity': severity,
                            'path': path,
                            'description': f'Sensitive file accessible: {path}'
                        }
                        findings.append(vuln)
                        self.vulnerabilities.append(vuln)
                        print(f"{Fore.RED if severity == 'High' else Fore.YELLOW}[!] Exposed File ({severity}): {path}{Style.RESET_ALL}")
        
        return findings
    
    def check_admin_panels(self) -> List[Dict]:
        """Check for accessible admin panels"""
        print(f"\n{Fore.CYAN}[*] Checking for admin panels...{Style.RESET_ALL}")
        
        findings = []
        admin_paths = [
            '/admin', '/admin/', '/administrator', '/administrator/',
            '/wp-admin', '/wp-admin/', '/phpmyadmin', '/phpmyadmin/',
            '/cpanel', '/webmail', '/admin/login', '/admin/dashboard',
            '/login', '/signin', '/user/login', '/auth/login',
            '/manager', '/management', '/control', '/panel'
        ]
        
        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = [executor.submit(self.check_path, path) for path in admin_paths]
            
            for future in futures:
                result = future.result()
                if result:
                    path, status, _ = result
                    if status in [200, 401, 403]:
                        vuln = {
                            'type': 'Admin Panel',
                            'severity': 'Info',
                            'path': path,
                            'status': status,
                            'description': f'Admin panel found at {path} (Status: {status})'
                        }
                        findings.append(vuln)
                        self.vulnerabilities.append(vuln)
                        print(f"{Fore.CYAN}[i] Admin Panel: {path} (Status: {status}){Style.RESET_ALL}")
        
        return findings
    
    def check_security_headers(self) -> List[Dict]:
        """Check for missing security headers"""
        print(f"\n{Fore.CYAN}[*] Checking security headers...{Style.RESET_ALL}")
        
        findings = []
        try:
            response = requests.get(self.url, headers=self.headers, timeout=TIMEOUT, verify=False)
            headers = response.headers
            
            required_headers = {
                'X-Frame-Options': 'Clickjacking protection',
                'X-Content-Type-Options': 'MIME-sniffing protection',
                'X-XSS-Protection': 'XSS filter',
                'Strict-Transport-Security': 'HTTPS enforcement',
                'Content-Security-Policy': 'Content injection protection',
            }
            
            for header, description in required_headers.items():
                if header not in headers:
                    vuln = {
                        'type': 'Missing Security Header',
                        'severity': 'Low',
                        'header': header,
                        'description': f'Missing {header} ({description})'
                    }
                    findings.append(vuln)
                    self.vulnerabilities.append(vuln)
                    print(f"{Fore.YELLOW}[!] Missing Header: {header}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[!] Security header check failed: {e}{Style.RESET_ALL}")
        
        return findings
    
    def check_ssl_tls(self) -> Dict:
        """Check SSL/TLS configuration"""
        print(f"\n{Fore.CYAN}[*] Checking SSL/TLS configuration...{Style.RESET_ALL}")
        
        ssl_info = {}
        if self.url.startswith('https'):
            try:
                response = requests.get(self.url, headers=self.headers, timeout=TIMEOUT)
                ssl_info['enabled'] = True
                print(f"{Fore.GREEN}[+] HTTPS is enabled{Style.RESET_ALL}")
            except requests.exceptions.SSLError as e:
                ssl_info['enabled'] = True
                ssl_info['error'] = str(e)
                vuln = {
                    'type': 'SSL/TLS Issue',
                    'severity': 'High',
                    'description': f'SSL/TLS error: {str(e)}'
                }
                self.vulnerabilities.append(vuln)
                print(f"{Fore.RED}[!] SSL/TLS Error: {e}{Style.RESET_ALL}")
        else:
            ssl_info['enabled'] = False
            print(f"{Fore.YELLOW}[!] HTTPS not enabled{Style.RESET_ALL}")
        
        return ssl_info
    
    def scan_all(self) -> Dict:
        """Run all vulnerability checks"""
        results = {
            'directory_listing': self.check_directory_listing(),
            'exposed_files': self.check_exposed_files(),
            'admin_panels': self.check_admin_panels(),
            'security_headers': self.check_security_headers(),
            'ssl_tls': self.check_ssl_tls(),
            'all_vulnerabilities': self.vulnerabilities
        }
        
        # Summary
        print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        print(f"{Style.BRIGHT}Vulnerability Scan Summary:{Style.RESET_ALL}")
        print(f"Total findings: {len(self.vulnerabilities)}")
        
        severity_count = {'High': 0, 'Medium': 0, 'Low': 0, 'Info': 0}
        for vuln in self.vulnerabilities:
            severity_count[vuln.get('severity', 'Info')] += 1
        
        print(f"{Fore.RED}High: {severity_count['High']}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Medium: {severity_count['Medium']}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Low: {severity_count['Low']}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Info: {severity_count['Info']}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
        
        return results
