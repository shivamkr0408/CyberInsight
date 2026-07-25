#!/usr/bin/env python3
"""
Eye4Eye - Attack Surface Mapper
A comprehensive tool for mapping and visualizing website attack surfaces

Author: Security Research Team
Version: 1.0.0
"""

import argparse
import sys
import os
import json
from datetime import datetime
from colorama import init, Fore, Style
import pyfiglet
from tqdm import tqdm

# Initialize colorama
init(autoreset=True)

# Import modules
from modules.subdomain_scanner import SubdomainScanner
from modules.port_scanner import PortScanner
from modules.tech_detector import TechDetector
from modules.vuln_scanner import VulnerabilityScanner
from modules.api_discovery import APIDiscovery
from visualizations.visualizer import AttackSurfaceVisualizer
from config import OUTPUT_DIR, COMMON_PORTS


class Eye4Eye:
    def __init__(self, domain: str, options: dict):
        self.domain = domain.replace('http://', '').replace('https://', '').split('/')[0]
        self.options = options
        self.results = {
            'domain': self.domain,
            'timestamp': datetime.now().isoformat(),
            'subdomains': {},
            'ports': {},
            'technologies': {},
            'vulnerabilities': [],
            'api_endpoints': []
        }
        
        # Create output directory
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        
    def print_banner(self):
        """Print ASCII art banner"""
        banner = pyfiglet.figlet_format("Eye4Eye", font="slant")
        print(f"{Fore.CYAN}{banner}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Attack Surface Mapper v1.0.0{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Target: {self.domain}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'='*70}{Style.RESET_ALL}\n")
        
    def scan_subdomains(self):
        """Enumerate subdomains"""
        if not self.options.get('skip_subdomains'):
            print(f"\n{Fore.MAGENTA}[*] Phase 1: Subdomain Enumeration{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'─'*70}{Style.RESET_ALL}")
            
            scanner = SubdomainScanner(self.domain)
            verify_live = self.options.get('verify_live', True)
            self.results['subdomains'] = scanner.get_all_subdomains(verify_live=verify_live)
            
            print(f"\n{Fore.GREEN}[✓] Found {len(self.results['subdomains'])} subdomains{Style.RESET_ALL}")
    
    def scan_ports(self):
        """Scan ports on discovered hosts"""
        if not self.options.get('skip_ports'):
            print(f"\n{Fore.MAGENTA}[*] Phase 2: Port Scanning{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'─'*70}{Style.RESET_ALL}")
            
            # Scan main domain
            targets = [self.domain]
            
            # Add subdomains if available
            if self.results['subdomains'] and not self.options.get('main_only'):
                targets.extend(list(self.results['subdomains'].keys())[:5])  # Limit to 5 subdomains
            
            for target in targets:
                try:
                    scanner = PortScanner(target)
                    
                    if self.options.get('full_scan'):
                        # Use nmap for detailed scan
                        ports = scanner.nmap_scan()
                    else:
                        # Quick scan of common ports
                        ports = scanner.quick_scan(COMMON_PORTS)
                    
                    if ports:
                        self.results['ports'][target] = ports
                except Exception as e:
                    print(f"{Fore.RED}[!] Port scan failed for {target}: {e}{Style.RESET_ALL}")
            
            total_ports = sum(len(p) for p in self.results['ports'].values())
            print(f"\n{Fore.GREEN}[✓] Found {total_ports} open ports across {len(self.results['ports'])} hosts{Style.RESET_ALL}")
    
    def detect_technologies(self):
        """Detect web technologies"""
        if not self.options.get('skip_tech'):
            print(f"\n{Fore.MAGENTA}[*] Phase 3: Technology Detection{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'─'*70}{Style.RESET_ALL}")
            
            url = f"http://{self.domain}"
            if 443 in self.results.get('ports', {}).get(self.domain, {}):
                url = f"https://{self.domain}"
            
            try:
                detector = TechDetector(url)
                self.results['technologies'] = detector.get_all_technologies()
                print(f"\n{Fore.GREEN}[✓] Technology detection complete{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}[!] Technology detection failed: {e}{Style.RESET_ALL}")
    
    def scan_vulnerabilities(self):
        """Scan for vulnerabilities"""
        if not self.options.get('skip_vulns'):
            print(f"\n{Fore.MAGENTA}[*] Phase 4: Vulnerability Scanning{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'─'*70}{Style.RESET_ALL}")
            
            url = f"http://{self.domain}"
            if 443 in self.results.get('ports', {}).get(self.domain, {}):
                url = f"https://{self.domain}"
            
            try:
                scanner = VulnerabilityScanner(url)
                vuln_results = scanner.scan_all()
                self.results['vulnerabilities'] = vuln_results.get('all_vulnerabilities', [])
                print(f"\n{Fore.GREEN}[✓] Vulnerability scan complete{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}[!] Vulnerability scan failed: {e}{Style.RESET_ALL}")
    
    def discover_apis(self):
        """Discover API endpoints"""
        if not self.options.get('skip_api'):
            print(f"\n{Fore.MAGENTA}[*] Phase 5: API Endpoint Discovery{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'─'*70}{Style.RESET_ALL}")
            
            url = f"http://{self.domain}"
            if 443 in self.results.get('ports', {}).get(self.domain, {}):
                url = f"https://{self.domain}"
            
            try:
                discovery = APIDiscovery(url)
                api_results = discovery.discover_all()
                self.results['api_endpoints'] = api_results.get('all_endpoints', [])
                print(f"\n{Fore.GREEN}[✓] API discovery complete{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}[!] API discovery failed: {e}{Style.RESET_ALL}")
    
    def generate_visualizations(self):
        """Generate visual reports"""
        print(f"\n{Fore.MAGENTA}[*] Phase 6: Generating Visualizations{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'─'*70}{Style.RESET_ALL}")
        
        visualizer = AttackSurfaceVisualizer(self.domain)
        
        # Generate HTML dashboard
        html_report = visualizer.create_dashboard(self.results)
        
        # Save reports
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Save HTML report
        html_path = os.path.join(OUTPUT_DIR, f"{self.domain}_{timestamp}_report.html")
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_report)
        print(f"{Fore.GREEN}[+] HTML report saved: {html_path}{Style.RESET_ALL}")
        
        # Save JSON data
        json_path = os.path.join(OUTPUT_DIR, f"{self.domain}_{timestamp}_data.json")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2)
        print(f"{Fore.GREEN}[+] JSON data saved: {json_path}{Style.RESET_ALL}")
        
        print(f"\n{Fore.GREEN}[✓] All visualizations generated successfully!{Style.RESET_ALL}")
        print(f"\n{Fore.CYAN}Open the HTML report in your browser:{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}file://{os.path.abspath(html_path)}{Style.RESET_ALL}\n")
    
    def run(self):
        """Execute the full attack surface mapping"""
        self.print_banner()
        
        try:
            # Phase 1: Subdomain Enumeration
            self.scan_subdomains()
            
            # Phase 2: Port Scanning
            self.scan_ports()
            
            # Phase 3: Technology Detection
            self.detect_technologies()
            
            # Phase 4: Vulnerability Scanning
            self.scan_vulnerabilities()
            
            # Phase 5: API Discovery
            self.discover_apis()
            
            # Phase 6: Generate Visualizations
            self.generate_visualizations()
            
            # Print summary
            print(f"\n{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}{Style.BRIGHT}Scan Complete!{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
            print(f"\n{Fore.YELLOW}Summary:{Style.RESET_ALL}")
            print(f"  • Subdomains: {len(self.results['subdomains'])}")
            print(f"  • Open Ports: {sum(len(p) for p in self.results['ports'].values())}")
            print(f"  • Vulnerabilities: {len(self.results['vulnerabilities'])}")
            print(f"  • API Endpoints: {len(self.results['api_endpoints'])}")
            print(f"\n{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")
            
        except KeyboardInterrupt:
            print(f"\n\n{Fore.YELLOW}[!] Scan interrupted by user{Style.RESET_ALL}")
            sys.exit(1)
        except Exception as e:
            print(f"\n{Fore.RED}[!] Fatal error: {e}{Style.RESET_ALL}")
            sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='Eye4Eye - Attack Surface Mapper',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python eye4eye.py example.com
  python eye4eye.py example.com --full-scan
  python eye4eye.py example.com --skip-subdomains --skip-ports
  python eye4eye.py example.com --main-only

Note: This tool is for authorized security testing only.
        '''
    )
    
    parser.add_argument('domain', help='Target domain to scan')
    parser.add_argument('--skip-subdomains', action='store_true', 
                       help='Skip subdomain enumeration')
    parser.add_argument('--skip-ports', action='store_true',
                       help='Skip port scanning')
    parser.add_argument('--skip-tech', action='store_true',
                       help='Skip technology detection')
    parser.add_argument('--skip-vulns', action='store_true',
                       help='Skip vulnerability scanning')
    parser.add_argument('--skip-api', action='store_true',
                       help='Skip API discovery')
    parser.add_argument('--full-scan', action='store_true',
                       help='Perform full port scan using nmap (slower but more detailed)')
    parser.add_argument('--main-only', action='store_true',
                       help='Only scan main domain, skip subdomains')
    parser.add_argument('--verify-live', action='store_true', default=True,
                       help='Verify live subdomains using httpx (default: enabled)')
    parser.add_argument('--no-verify-live', dest='verify_live', action='store_false',
                       help='Skip live subdomain verification')
    
    args = parser.parse_args()
    
    # Convert args to options dict
    options = {
        'skip_subdomains': args.skip_subdomains,
        'skip_ports': args.skip_ports,
        'skip_tech': args.skip_tech,
        'skip_vulns': args.skip_vulns,
        'skip_api': args.skip_api,
        'full_scan': args.full_scan,
        'main_only': args.main_only,
        'verify_live': args.verify_live,
    }
    
    # Create and run scanner
    scanner = Eye4Eye(args.domain, options)
    scanner.run()


if __name__ == '__main__':
    main()
