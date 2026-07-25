"""
Port Scanning Module
Scans for open ports on discovered hosts
"""

import socket
import nmap
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict
from config import COMMON_PORTS, TIMEOUT, MAX_THREADS
from colorama import Fore, Style
from tqdm import tqdm


class PortScanner:
    def __init__(self, target: str):
        self.target = target
        self.open_ports: Dict[int, str] = {}
        
    def scan_port(self, port: int) -> tuple:
        """Scan a single port"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(TIMEOUT)
            result = sock.connect_ex((self.target, port))
            sock.close()
            
            if result == 0:
                # Try to grab banner
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(2)
                    sock.connect((self.target, port))
                    sock.send(b'HEAD / HTTP/1.0\r\n\r\n')
                    banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
                    sock.close()
                    return (port, banner[:100] if banner else "Open")
                except:
                    return (port, "Open")
        except:
            pass
        return None
    
    def quick_scan(self, ports: List[int] = None) -> Dict[int, str]:
        """Quick scan of common ports"""
        if ports is None:
            ports = COMMON_PORTS
        
        print(f"\n{Fore.CYAN}[*] Scanning {len(ports)} ports on {self.target}...{Style.RESET_ALL}")
        
        with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
            futures = [executor.submit(self.scan_port, port) for port in ports]
            
            for future in tqdm(futures, desc="Port scanning", unit="port"):
                result = future.result()
                if result:
                    port, banner = result
                    self.open_ports[port] = banner
                    print(f"{Fore.GREEN}[+] Port {port}/tcp open - {banner}{Style.RESET_ALL}")
        
        return self.open_ports
    
    def nmap_scan(self, arguments: str = "-sV -sC") -> dict:
        """Advanced scan using nmap"""
        print(f"\n{Fore.CYAN}[*] Running nmap scan on {self.target}...{Style.RESET_ALL}")
        
        try:
            nm = nmap.PortScanner()
            nm.scan(self.target, arguments=arguments)
            
            results = {}
            for host in nm.all_hosts():
                results[host] = {
                    'state': nm[host].state(),
                    'protocols': {}
                }
                
                for proto in nm[host].all_protocols():
                    results[host]['protocols'][proto] = {}
                    ports = nm[host][proto].keys()
                    
                    for port in ports:
                        port_info = nm[host][proto][port]
                        results[host]['protocols'][proto][port] = {
                            'state': port_info['state'],
                            'name': port_info.get('name', ''),
                            'product': port_info.get('product', ''),
                            'version': port_info.get('version', ''),
                            'extrainfo': port_info.get('extrainfo', ''),
                        }
                        
                        print(f"{Fore.GREEN}[+] {port}/tcp {port_info['state']} - "
                              f"{port_info.get('name', 'unknown')} "
                              f"{port_info.get('product', '')} "
                              f"{port_info.get('version', '')}{Style.RESET_ALL}")
            
            return results
        except Exception as e:
            print(f"{Fore.RED}[!] Nmap scan failed: {e}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}[!] Falling back to basic scan...{Style.RESET_ALL}")
            return {'error': str(e)}
    
    def get_service_info(self, port: int) -> str:
        """Get common service name for a port"""
        common_services = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
            53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
            443: "HTTPS", 445: "SMB", 3306: "MySQL", 3389: "RDP",
            5432: "PostgreSQL", 5900: "VNC", 8000: "HTTP-Alt",
            8080: "HTTP-Proxy", 8443: "HTTPS-Alt", 8888: "HTTP-Alt"
        }
        return common_services.get(port, "Unknown")
