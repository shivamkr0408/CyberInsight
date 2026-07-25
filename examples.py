#!/usr/bin/env python3
"""
Example script demonstrating programmatic usage of Eye4Eye modules
This shows how to use individual components without running the full scan
"""

from modules.subdomain_scanner import SubdomainScanner
from modules.port_scanner import PortScanner
from modules.tech_detector import TechDetector
from modules.vuln_scanner import VulnerabilityScanner
from modules.api_discovery import APIDiscovery
from visualizations.visualizer import AttackSurfaceVisualizer
from colorama import init, Fore, Style

init(autoreset=True)


def example_subdomain_scan():
    """Example: Subdomain enumeration only"""
    print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Example 1: Subdomain Enumeration{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    
    domain = "example.com"
    scanner = SubdomainScanner(domain)
    
    # Get all subdomains
    subdomains = scanner.get_all_subdomains()
    
    print(f"\n{Fore.GREEN}Found {len(subdomains)} subdomains:{Style.RESET_ALL}")
    for subdomain, ips in list(subdomains.items())[:5]:  # Show first 5
        print(f"  • {subdomain}: {', '.join(ips)}")


def example_port_scan():
    """Example: Port scanning only"""
    print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Example 2: Port Scanning{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    
    target = "scanme.nmap.org"  # Legal test target
    scanner = PortScanner(target)
    
    # Quick scan of common ports
    open_ports = scanner.quick_scan([22, 80, 443, 8080])
    
    print(f"\n{Fore.GREEN}Open ports on {target}:{Style.RESET_ALL}")
    for port, banner in open_ports.items():
        service = scanner.get_service_info(port)
        print(f"  • Port {port} ({service}): {banner}")


def example_tech_detection():
    """Example: Technology detection only"""
    print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Example 3: Technology Detection{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    
    url = "https://example.com"
    detector = TechDetector(url)
    
    # Detect technologies
    tech = detector.get_all_technologies()
    
    print(f"\n{Fore.GREEN}Detected technologies:{Style.RESET_ALL}")
    if tech.get('builtwith'):
        for category, items in tech['builtwith'].items():
            print(f"  • {category}: {', '.join(items)}")


def example_vulnerability_scan():
    """Example: Vulnerability scanning only"""
    print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Example 4: Vulnerability Scanning{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    
    url = "https://example.com"
    scanner = VulnerabilityScanner(url)
    
    # Run specific checks
    exposed_files = scanner.check_exposed_files()
    security_headers = scanner.check_security_headers()
    
    print(f"\n{Fore.GREEN}Vulnerability Summary:{Style.RESET_ALL}")
    print(f"  • Exposed files: {len(exposed_files)}")
    print(f"  • Missing security headers: {len(security_headers)}")


def example_api_discovery():
    """Example: API endpoint discovery only"""
    print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Example 5: API Discovery{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    
    url = "https://api.github.com"
    discovery = APIDiscovery(url)
    
    # Discover API endpoints
    results = discovery.discover_all()
    
    print(f"\n{Fore.GREEN}API Endpoints found:{Style.RESET_ALL}")
    for endpoint in list(results['all_endpoints'])[:10]:  # Show first 10
        print(f"  • {endpoint}")


def example_custom_visualization():
    """Example: Creating custom visualizations"""
    print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Example 6: Custom Visualization{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    
    # Sample data
    sample_data = {
        'subdomains': {
            'www.example.com': ['93.184.216.34'],
            'mail.example.com': ['93.184.216.35'],
            'api.example.com': ['93.184.216.36'],
        },
        'ports': {
            'example.com': {80: 'HTTP', 443: 'HTTPS'}
        },
        'technologies': {
            'web-servers': ['nginx'],
            'cms': ['WordPress']
        },
        'vulnerabilities': [
            {'type': 'Missing Header', 'severity': 'Low'},
            {'type': 'Exposed File', 'severity': 'High'}
        ],
        'api_endpoints': ['/api/v1/users', '/api/v1/posts']
    }
    
    visualizer = AttackSurfaceVisualizer('example.com')
    
    # Create individual visualizations
    subdomain_fig = visualizer.create_subdomain_tree(sample_data['subdomains'])
    port_fig = visualizer.create_port_map(sample_data['ports'])
    
    print(f"\n{Fore.GREEN}Visualizations created!{Style.RESET_ALL}")
    print(f"  • Subdomain tree: {type(subdomain_fig).__name__}")
    print(f"  • Port map: {type(port_fig).__name__}")
    print(f"\n{Fore.CYAN}Use .show() to display or .write_html() to save{Style.RESET_ALL}")


def example_custom_wordlist():
    """Example: Using custom subdomain wordlist"""
    print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Example 7: Custom Wordlist{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    
    domain = "example.com"
    custom_wordlist = ['www', 'mail', 'api', 'dev', 'staging', 'admin']
    
    scanner = SubdomainScanner(domain)
    subdomains = scanner.enumerate_subdomains(wordlist=custom_wordlist)
    
    print(f"\n{Fore.GREEN}Custom wordlist scan complete:{Style.RESET_ALL}")
    print(f"  • Tested: {len(custom_wordlist)} subdomains")
    print(f"  • Found: {len(subdomains)} active subdomains")


def main():
    """Run all examples"""
    print(f"\n{Fore.MAGENTA}{Style.BRIGHT}")
    print("╔════════════════════════════════════════════════════════════╗")
    print("║         Eye4Eye - Programmatic Usage Examples             ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print(f"{Style.RESET_ALL}")
    
    print(f"\n{Fore.YELLOW}This script demonstrates how to use Eye4Eye modules individually.{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Note: Some examples use real domains for demonstration.{Style.RESET_ALL}")
    print(f"{Fore.RED}Always ensure you have permission before scanning!{Style.RESET_ALL}\n")
    
    # Uncomment the examples you want to run:
    
    # example_subdomain_scan()      # May take a while
    # example_port_scan()           # Uses legal test target
    # example_tech_detection()      # Quick
    # example_vulnerability_scan()  # Quick
    # example_api_discovery()       # Quick
    example_custom_visualization()  # Quick, uses sample data
    example_custom_wordlist()       # Quick
    
    print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Examples complete!{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
    
    print(f"{Fore.YELLOW}Tips:{Style.RESET_ALL}")
    print(f"  • Uncomment other examples in main() to run them")
    print(f"  • Modify the code to test with your own targets")
    print(f"  • Check each module's source code for more options")
    print(f"  • Combine modules to create custom scanning workflows\n")


if __name__ == '__main__':
    main()
