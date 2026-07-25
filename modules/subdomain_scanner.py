"""
Subdomain Enumeration Module
Discovers subdomains using DNS queries and certificate transparency logs
"""

import dns.resolver
import asyncio
import aiohttp
import httpx
from concurrent.futures import ThreadPoolExecutor
from typing import List, Set, Dict, Tuple
import socket
from config import SUBDOMAIN_WORDLIST, TIMEOUT, MAX_THREADS
from colorama import Fore, Style
from tqdm import tqdm


class SubdomainScanner:
    def __init__(self, domain: str):
        self.domain = domain
        self.subdomains: Set[str] = set()
        self.resolver = dns.resolver.Resolver()
        self.resolver.timeout = TIMEOUT
        self.resolver.lifetime = TIMEOUT
        
    def check_subdomain(self, subdomain: str) -> tuple:
        """Check if a subdomain exists and resolve its IP"""
        full_domain = f"{subdomain}.{self.domain}"
        try:
            answers = self.resolver.resolve(full_domain, 'A')
            ips = [str(rdata) for rdata in answers]
            return (full_domain, ips)
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.NoNameservers, dns.exception.Timeout):
            return None
        except Exception:
            return None
    
    def enumerate_subdomains(self, wordlist: List[str] = None) -> dict:
        """Enumerate subdomains using wordlist"""
        if wordlist is None:
            wordlist = SUBDOMAIN_WORDLIST
        
        results = {}
        print(f"\n{Fore.CYAN}[*] Enumerating subdomains for {self.domain}...{Style.RESET_ALL}")
        
        with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
            futures = [executor.submit(self.check_subdomain, sub) for sub in wordlist]
            
            for future in tqdm(futures, desc="Scanning subdomains", unit="subdomain"):
                result = future.result()
                if result:
                    subdomain, ips = result
                    results[subdomain] = ips
                    self.subdomains.add(subdomain)
                    print(f"{Fore.GREEN}[+] Found: {subdomain} -> {', '.join(ips)}{Style.RESET_ALL}")
        
        return results
    
    async def check_crt_sh(self) -> Set[str]:
        """Query crt.sh for certificate transparency logs"""
        print(f"\n{Fore.CYAN}[*] Querying certificate transparency logs...{Style.RESET_ALL}")
        crt_subdomains = set()
        
        try:
            url = f"https://crt.sh/?q=%.{self.domain}&output=json"
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=aiohttp.ClientTimeout(total=30)) as response:
                    if response.status == 200:
                        data = await response.json()
                        for entry in data:
                            name = entry.get('name_value', '')
                            # Handle wildcard and multiple domains
                            for domain in name.split('\n'):
                                domain = domain.strip().replace('*.', '')
                                if domain.endswith(self.domain) and domain != self.domain:
                                    crt_subdomains.add(domain)
                                    print(f"{Fore.GREEN}[+] CT Log: {domain}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.YELLOW}[!] Certificate transparency lookup failed: {e}{Style.RESET_ALL}")
        
        return crt_subdomains
    
    def check_live_subdomain(self, subdomain: str) -> Tuple[str, Dict]:
        """Check if subdomain is live via HTTP/HTTPS"""
        result = {
            'live': False,
            'http': False,
            'https': False,
            'status_code': None,
            'redirect': None,
            'title': None
        }
        
        # Try HTTPS first
        try:
            with httpx.Client(timeout=TIMEOUT, follow_redirects=True, verify=False) as client:
                response = client.get(f"https://{subdomain}")
                result['https'] = True
                result['live'] = True
                result['status_code'] = response.status_code
                
                # Try to extract title
                if 'text/html' in response.headers.get('content-type', ''):
                    try:
                        import re
                        title_match = re.search(r'<title>(.*?)</title>', response.text, re.IGNORECASE)
                        if title_match:
                            result['title'] = title_match.group(1).strip()[:100]
                    except:
                        pass
                
                return (subdomain, result)
        except:
            pass
        
        # Try HTTP if HTTPS fails
        try:
            with httpx.Client(timeout=TIMEOUT, follow_redirects=True, verify=False) as client:
                response = client.get(f"http://{subdomain}")
                result['http'] = True
                result['live'] = True
                result['status_code'] = response.status_code
                
                # Try to extract title
                if 'text/html' in response.headers.get('content-type', ''):
                    try:
                        import re
                        title_match = re.search(r'<title>(.*?)</title>', response.text, re.IGNORECASE)
                        if title_match:
                            result['title'] = title_match.group(1).strip()[:100]
                    except:
                        pass
                
                return (subdomain, result)
        except:
            pass
        
        return (subdomain, result)
    
    def verify_live_subdomains(self, subdomains: Dict[str, List[str]]) -> Dict[str, Dict]:
        """Verify which subdomains are actually live (responding to HTTP/HTTPS)"""
        print(f"\n{Fore.CYAN}[*] Verifying live subdomains with httpx...{Style.RESET_ALL}")
        
        live_results = {}
        subdomain_list = list(subdomains.keys())
        
        with ThreadPoolExecutor(max_workers=min(MAX_THREADS, 20)) as executor:
            futures = [executor.submit(self.check_live_subdomain, sub) for sub in subdomain_list]
            
            for future in tqdm(futures, desc="Checking live status", unit="subdomain"):
                subdomain, result = future.result()
                if result['live']:
                    live_results[subdomain] = {
                        'ips': subdomains[subdomain],
                        'http': result['http'],
                        'https': result['https'],
                        'status_code': result['status_code'],
                        'title': result['title']
                    }
                    
                    protocol = "HTTPS" if result['https'] else "HTTP"
                    status = f"[{result['status_code']}]" if result['status_code'] else ""
                    title = f" - {result['title']}" if result['title'] else ""
                    
                    print(f"{Fore.GREEN}[+] LIVE: {subdomain} ({protocol}) {status}{title}{Style.RESET_ALL}")
        
        print(f"\n{Fore.GREEN}[✓] Found {len(live_results)} live subdomains out of {len(subdomains)} total{Style.RESET_ALL}")
        return live_results
    
    def get_all_subdomains(self, verify_live: bool = True) -> dict:
        """Combine all subdomain discovery methods"""
        # Wordlist enumeration
        wordlist_results = self.enumerate_subdomains()
        
        # Certificate transparency
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            crt_subs = loop.run_until_complete(self.check_crt_sh())
            loop.close()
            
            # Resolve CT log subdomains
            for subdomain in crt_subs:
                if subdomain not in wordlist_results:
                    try:
                        answers = self.resolver.resolve(subdomain, 'A')
                        ips = [str(rdata) for rdata in answers]
                        wordlist_results[subdomain] = ips
                    except:
                        pass
        except Exception as e:
            print(f"{Fore.YELLOW}[!] Error in CT log processing: {e}{Style.RESET_ALL}")
        
        # Verify live subdomains if requested
        if verify_live and wordlist_results:
            live_results = self.verify_live_subdomains(wordlist_results)
            return live_results
        
        return wordlist_results

