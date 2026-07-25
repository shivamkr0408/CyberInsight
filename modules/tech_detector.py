"""
Technology Stack Detection Module
Identifies web technologies, frameworks, and CMS
"""

import requests
import builtwith
from bs4 import BeautifulSoup
from typing import Dict, List
from config import USER_AGENT, TIMEOUT
from colorama import Fore, Style
import re


class TechDetector:
    def __init__(self, url: str):
        self.url = url if url.startswith('http') else f'http://{url}'
        self.technologies: Dict[str, List[str]] = {}
        self.headers = {'User-Agent': USER_AGENT}
        
    def detect_builtwith(self) -> dict:
        """Use builtwith library for tech detection"""
        print(f"\n{Fore.CYAN}[*] Detecting technologies for {self.url}...{Style.RESET_ALL}")
        
        try:
            tech = builtwith.parse(self.url)
            for category, items in tech.items():
                if items:
                    self.technologies[category] = items
                    print(f"{Fore.GREEN}[+] {category}: {', '.join(items)}{Style.RESET_ALL}")
            return tech
        except Exception as e:
            print(f"{Fore.YELLOW}[!] BuiltWith detection failed: {e}{Style.RESET_ALL}")
            return {}
    
    def detect_headers(self) -> dict:
        """Analyze HTTP headers for technology fingerprints"""
        print(f"\n{Fore.CYAN}[*] Analyzing HTTP headers...{Style.RESET_ALL}")
        
        header_info = {}
        try:
            response = requests.get(self.url, headers=self.headers, timeout=TIMEOUT, verify=False)
            headers = response.headers
            
            # Server information
            if 'Server' in headers:
                header_info['Server'] = headers['Server']
                print(f"{Fore.GREEN}[+] Server: {headers['Server']}{Style.RESET_ALL}")
            
            # Powered by
            if 'X-Powered-By' in headers:
                header_info['X-Powered-By'] = headers['X-Powered-By']
                print(f"{Fore.GREEN}[+] X-Powered-By: {headers['X-Powered-By']}{Style.RESET_ALL}")
            
            # Framework headers
            framework_headers = ['X-AspNet-Version', 'X-AspNetMvc-Version', 'X-Framework', 
                                'X-Generator', 'X-Drupal-Cache', 'X-Powered-CMS']
            for header in framework_headers:
                if header in headers:
                    header_info[header] = headers[header]
                    print(f"{Fore.GREEN}[+] {header}: {headers[header]}{Style.RESET_ALL}")
            
            # Security headers
            security_headers = ['X-Frame-Options', 'X-XSS-Protection', 'X-Content-Type-Options',
                              'Strict-Transport-Security', 'Content-Security-Policy']
            header_info['security'] = {}
            for header in security_headers:
                if header in headers:
                    header_info['security'][header] = headers[header]
            
            return header_info
        except Exception as e:
            print(f"{Fore.YELLOW}[!] Header analysis failed: {e}{Style.RESET_ALL}")
            return {}
    
    def detect_meta_tags(self) -> dict:
        """Extract technology info from meta tags"""
        print(f"\n{Fore.CYAN}[*] Analyzing meta tags...{Style.RESET_ALL}")
        
        meta_info = {}
        try:
            response = requests.get(self.url, headers=self.headers, timeout=TIMEOUT, verify=False)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Generator meta tag
            generator = soup.find('meta', attrs={'name': 'generator'})
            if generator and generator.get('content'):
                meta_info['generator'] = generator['content']
                print(f"{Fore.GREEN}[+] Generator: {generator['content']}{Style.RESET_ALL}")
            
            # Look for common CMS patterns
            cms_patterns = {
                'WordPress': ['/wp-content/', '/wp-includes/', 'wp-json'],
                'Joomla': ['/components/com_', '/modules/mod_', 'Joomla!'],
                'Drupal': ['/sites/all/', '/sites/default/', 'Drupal'],
                'Magento': ['/skin/frontend/', 'Mage.Cookies', 'Magento'],
                'Shopify': ['cdn.shopify.com', 'Shopify'],
            }
            
            html_content = str(soup)
            detected_cms = []
            for cms, patterns in cms_patterns.items():
                if any(pattern in html_content for pattern in patterns):
                    detected_cms.append(cms)
                    print(f"{Fore.GREEN}[+] Detected CMS: {cms}{Style.RESET_ALL}")
            
            if detected_cms:
                meta_info['cms'] = detected_cms
            
            # JavaScript frameworks
            js_frameworks = {
                'React': ['react', 'react-dom'],
                'Vue.js': ['vue.js', 'vue.min.js', '__vue__'],
                'Angular': ['angular', 'ng-app', 'ng-controller'],
                'jQuery': ['jquery'],
            }
            
            scripts = soup.find_all('script', src=True)
            detected_frameworks = []
            for framework, patterns in js_frameworks.items():
                for script in scripts:
                    src = script.get('src', '').lower()
                    if any(pattern in src for pattern in patterns):
                        detected_frameworks.append(framework)
                        print(f"{Fore.GREEN}[+] JavaScript Framework: {framework}{Style.RESET_ALL}")
                        break
            
            if detected_frameworks:
                meta_info['javascript_frameworks'] = detected_frameworks
            
            return meta_info
        except Exception as e:
            print(f"{Fore.YELLOW}[!] Meta tag analysis failed: {e}{Style.RESET_ALL}")
            return {}
    
    def get_all_technologies(self) -> dict:
        """Combine all detection methods"""
        all_tech = {
            'builtwith': self.detect_builtwith(),
            'headers': self.detect_headers(),
            'meta_tags': self.detect_meta_tags(),
        }
        return all_tech
