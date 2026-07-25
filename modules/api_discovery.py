"""
API Endpoint Discovery Module
Discovers and maps API endpoints
"""

import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Set
from config import API_PATTERNS, USER_AGENT, TIMEOUT
from colorama import Fore, Style
import re
import json


class APIDiscovery:
    def __init__(self, url: str):
        self.url = url if url.startswith('http') else f'http://{url}'
        self.endpoints: Set[str] = set()
        self.headers = {'User-Agent': USER_AGENT}
        
    def check_common_api_paths(self) -> List[str]:
        """Check for common API documentation and endpoint paths"""
        print(f"\n{Fore.CYAN}[*] Checking for API endpoints...{Style.RESET_ALL}")
        
        found_endpoints = []
        api_docs = [
            '/api', '/api/', '/api/v1', '/api/v2', '/api/v3',
            '/rest', '/rest/', '/graphql', '/graphql/',
            '/swagger', '/swagger/', '/swagger.json', '/swagger/v1/swagger.json',
            '/api-docs', '/api-docs/', '/api/docs', '/api/documentation',
            '/openapi.json', '/openapi.yaml', '/api.json',
            '/v1', '/v2', '/v3', '/.well-known/openapi.json',
            '/docs', '/documentation', '/redoc'
        ]
        
        for path in api_docs:
            try:
                full_url = f"{self.url}{path}"
                response = requests.get(full_url, headers=self.headers, 
                                      timeout=TIMEOUT, verify=False)
                
                if response.status_code == 200:
                    found_endpoints.append(path)
                    self.endpoints.add(path)
                    print(f"{Fore.GREEN}[+] API Endpoint: {path}{Style.RESET_ALL}")
                    
                    # Try to parse as JSON for more endpoints
                    try:
                        data = response.json()
                        self._extract_endpoints_from_json(data, path)
                    except:
                        pass
            except:
                pass
        
        return found_endpoints
    
    def _extract_endpoints_from_json(self, data: dict, base_path: str):
        """Extract endpoint paths from JSON API documentation"""
        if isinstance(data, dict):
            # Swagger/OpenAPI format
            if 'paths' in data:
                for path in data['paths'].keys():
                    endpoint = f"{base_path}{path}"
                    self.endpoints.add(endpoint)
                    print(f"{Fore.GREEN}  └─ {path}{Style.RESET_ALL}")
            
            # Check for nested structures
            for key, value in data.items():
                if isinstance(value, (dict, list)):
                    self._extract_endpoints_from_json(value, base_path)
        
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, (dict, list)):
                    self._extract_endpoints_from_json(item, base_path)
    
    def scan_javascript_files(self) -> List[str]:
        """Scan JavaScript files for API endpoint references"""
        print(f"\n{Fore.CYAN}[*] Scanning JavaScript for API endpoints...{Style.RESET_ALL}")
        
        found_endpoints = []
        try:
            response = requests.get(self.url, headers=self.headers, timeout=TIMEOUT, verify=False)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all script tags
            scripts = soup.find_all('script', src=True)
            
            for script in scripts[:10]:  # Limit to first 10 scripts
                try:
                    script_url = script['src']
                    if not script_url.startswith('http'):
                        script_url = f"{self.url}/{script_url.lstrip('/')}"
                    
                    script_response = requests.get(script_url, headers=self.headers, 
                                                  timeout=TIMEOUT, verify=False)
                    script_content = script_response.text
                    
                    # Look for API patterns in JavaScript
                    api_regex = r'["\']/(api|rest|graphql|v\d+)/[a-zA-Z0-9/_-]+["\']'
                    matches = re.findall(api_regex, script_content)
                    
                    for match in matches:
                        endpoint = match.strip('"\'')
                        if endpoint not in self.endpoints:
                            self.endpoints.add(endpoint)
                            found_endpoints.append(endpoint)
                            print(f"{Fore.GREEN}[+] JS API Endpoint: {endpoint}{Style.RESET_ALL}")
                except:
                    continue
        except Exception as e:
            print(f"{Fore.YELLOW}[!] JavaScript scanning failed: {e}{Style.RESET_ALL}")
        
        return found_endpoints
    
    def check_robots_txt(self) -> List[str]:
        """Check robots.txt for API paths"""
        print(f"\n{Fore.CYAN}[*] Checking robots.txt...{Style.RESET_ALL}")
        
        found_paths = []
        try:
            response = requests.get(f"{self.url}/robots.txt", 
                                  headers=self.headers, timeout=TIMEOUT, verify=False)
            
            if response.status_code == 200:
                for line in response.text.split('\n'):
                    if 'Disallow:' in line or 'Allow:' in line:
                        path = line.split(':', 1)[1].strip()
                        if any(pattern in path.lower() for pattern in ['api', 'rest', 'graphql', 'v1', 'v2']):
                            found_paths.append(path)
                            self.endpoints.add(path)
                            print(f"{Fore.GREEN}[+] robots.txt API path: {path}{Style.RESET_ALL}")
        except:
            pass
        
        return found_paths
    
    def check_sitemap(self) -> List[str]:
        """Check sitemap.xml for API references"""
        print(f"\n{Fore.CYAN}[*] Checking sitemap.xml...{Style.RESET_ALL}")
        
        found_paths = []
        try:
            response = requests.get(f"{self.url}/sitemap.xml", 
                                  headers=self.headers, timeout=TIMEOUT, verify=False)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'xml')
                urls = soup.find_all('loc')
                
                for url in urls:
                    path = url.text.replace(self.url, '')
                    if any(pattern in path.lower() for pattern in ['api', 'rest', 'graphql']):
                        found_paths.append(path)
                        self.endpoints.add(path)
                        print(f"{Fore.GREEN}[+] Sitemap API path: {path}{Style.RESET_ALL}")
        except:
            pass
        
        return found_paths
    
    def discover_all(self) -> Dict:
        """Run all API discovery methods"""
        results = {
            'common_paths': self.check_common_api_paths(),
            'javascript': self.scan_javascript_files(),
            'robots_txt': self.check_robots_txt(),
            'sitemap': self.check_sitemap(),
            'all_endpoints': list(self.endpoints)
        }
        
        print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        print(f"{Style.BRIGHT}API Discovery Summary:{Style.RESET_ALL}")
        print(f"Total endpoints found: {len(self.endpoints)}")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
        
        return results
