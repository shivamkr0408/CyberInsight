"""
Visualization Module
Creates interactive visual representations of attack surface data
"""

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import networkx as nx
from typing import Dict, List
import json
from datetime import datetime


class AttackSurfaceVisualizer:
    def __init__(self, domain: str):
        self.domain = domain
        self.colors = {
            'primary': '#00d4ff',
            'secondary': '#ff006e',
            'success': '#06ffa5',
            'warning': '#ffbe0b',
            'danger': '#ff006e',
            'info': '#8338ec'
        }
        
    def create_subdomain_tree(self, subdomains: Dict[str, List[str]]) -> go.Figure:
        """Create interactive tree visualization of subdomains"""
        
        # Create network graph
        G = nx.DiGraph()
        G.add_node(self.domain, level=0, node_type='root')
        
        for subdomain, ips in subdomains.items():
            # Add subdomain node
            G.add_node(subdomain, level=1, node_type='subdomain', ips=ips)
            G.add_edge(self.domain, subdomain)
            
            # Add IP nodes
            for ip in ips:
                G.add_node(ip, level=2, node_type='ip')
                G.add_edge(subdomain, ip)
        
        # Create hierarchical layout
        pos = nx.spring_layout(G, k=2, iterations=50)
        
        # Separate nodes by type
        edge_trace = []
        for edge in G.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_trace.append(
                go.Scatter(
                    x=[x0, x1, None],
                    y=[y0, y1, None],
                    mode='lines',
                    line=dict(width=2, color='rgba(0, 212, 255, 0.3)'),
                    hoverinfo='none',
                    showlegend=False
                )
            )
        
        # Node traces
        node_traces = {
            'root': {'x': [], 'y': [], 'text': [], 'color': self.colors['danger']},
            'subdomain': {'x': [], 'y': [], 'text': [], 'color': self.colors['primary']},
            'ip': {'x': [], 'y': [], 'text': [], 'color': self.colors['success']}
        }
        
        for node in G.nodes():
            x, y = pos[node]
            node_type = G.nodes[node].get('node_type', 'subdomain')
            node_traces[node_type]['x'].append(x)
            node_traces[node_type]['y'].append(y)
            
            if node_type == 'subdomain':
                ips = G.nodes[node].get('ips', [])
                text = f"{node}<br>IPs: {', '.join(ips)}"
            else:
                text = node
            
            node_traces[node_type]['text'].append(text)
        
        # Create figure
        fig = go.Figure()
        
        # Add edges
        for trace in edge_trace:
            fig.add_trace(trace)
        
        # Add nodes
        for node_type, data in node_traces.items():
            if data['x']:
                fig.add_trace(go.Scatter(
                    x=data['x'],
                    y=data['y'],
                    mode='markers+text',
                    name=node_type.capitalize(),
                    text=data['text'],
                    textposition='top center',
                    hoverinfo='text',
                    marker=dict(
                        size=20 if node_type == 'root' else 15 if node_type == 'subdomain' else 10,
                        color=data['color'],
                        line=dict(width=2, color='white')
                    )
                ))
        
        fig.update_layout(
            title=f'Subdomain Tree - {self.domain}',
            showlegend=True,
            hovermode='closest',
            plot_bgcolor='#0a0e27',
            paper_bgcolor='#0a0e27',
            font=dict(color='white', size=12),
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            height=800
        )
        
        return fig
    
    def create_port_map(self, port_data: Dict[str, Dict[int, str]]) -> go.Figure:
        """Create visual map of open ports across hosts"""
        
        hosts = list(port_data.keys())
        all_ports = set()
        for ports in port_data.values():
            all_ports.update(ports.keys())
        all_ports = sorted(all_ports)
        
        # Create matrix data
        z_data = []
        hover_text = []
        
        for host in hosts:
            row = []
            hover_row = []
            for port in all_ports:
                if port in port_data[host]:
                    row.append(1)
                    banner = port_data[host][port]
                    hover_row.append(f"Host: {host}<br>Port: {port}<br>Service: {banner}")
                else:
                    row.append(0)
                    hover_row.append(f"Host: {host}<br>Port: {port}<br>Closed")
            z_data.append(row)
            hover_text.append(hover_row)
        
        fig = go.Figure(data=go.Heatmap(
            z=z_data,
            x=[f"Port {p}" for p in all_ports],
            y=hosts,
            colorscale=[
                [0, '#1a1d35'],
                [1, self.colors['primary']]
            ],
            text=hover_text,
            hoverinfo='text',
            showscale=False
        ))
        
        fig.update_layout(
            title='Open Ports Heatmap',
            xaxis_title='Ports',
            yaxis_title='Hosts',
            plot_bgcolor='#0a0e27',
            paper_bgcolor='#0a0e27',
            font=dict(color='white', size=12),
            height=max(400, len(hosts) * 50)
        )
        
        return fig
    
    def create_tech_stack_graph(self, tech_data: Dict) -> go.Figure:
        """Create visual representation of technology stack"""
        
        categories = []
        technologies = []
        values = []
        colors_list = []
        
        color_map = {
            'web-servers': self.colors['primary'],
            'web-frameworks': self.colors['secondary'],
            'javascript-frameworks': self.colors['success'],
            'cms': self.colors['warning'],
            'programming-languages': self.colors['info'],
        }
        
        for category, techs in tech_data.items():
            if isinstance(techs, list):
                for tech in techs:
                    categories.append(category)
                    technologies.append(tech)
                    values.append(1)
                    colors_list.append(color_map.get(category.lower(), self.colors['primary']))
        
        if not technologies:
            # Create empty figure with message
            fig = go.Figure()
            fig.add_annotation(
                text="No technology data available",
                xref="paper", yref="paper",
                x=0.5, y=0.5, showarrow=False,
                font=dict(size=20, color='white')
            )
        else:
            fig = go.Figure(data=[go.Bar(
                x=technologies,
                y=values,
                marker=dict(color=colors_list),
                text=categories,
                hovertemplate='<b>%{x}</b><br>Category: %{text}<extra></extra>'
            )])
        
        fig.update_layout(
            title='Technology Stack',
            xaxis_title='Technologies',
            yaxis_title='',
            plot_bgcolor='#0a0e27',
            paper_bgcolor='#0a0e27',
            font=dict(color='white', size=12),
            showlegend=False,
            height=500,
            yaxis=dict(showticklabels=False)
        )
        
        return fig
    
    def create_vulnerability_chart(self, vulnerabilities: List[Dict]) -> go.Figure:
        """Create visualization of vulnerabilities by severity"""
        
        severity_counts = {'High': 0, 'Medium': 0, 'Low': 0, 'Info': 0}
        vuln_types = {}
        
        for vuln in vulnerabilities:
            severity = vuln.get('severity', 'Info')
            vuln_type = vuln.get('type', 'Unknown')
            
            severity_counts[severity] += 1
            vuln_types[vuln_type] = vuln_types.get(vuln_type, 0) + 1
        
        # Create subplots
        fig = make_subplots(
            rows=1, cols=2,
            subplot_titles=('Vulnerabilities by Severity', 'Vulnerabilities by Type'),
            specs=[[{'type': 'pie'}, {'type': 'bar'}]]
        )
        
        # Severity pie chart
        severity_colors = {
            'High': self.colors['danger'],
            'Medium': self.colors['warning'],
            'Low': self.colors['info'],
            'Info': self.colors['primary']
        }
        
        fig.add_trace(
            go.Pie(
                labels=list(severity_counts.keys()),
                values=list(severity_counts.values()),
                marker=dict(colors=[severity_colors[s] for s in severity_counts.keys()]),
                hole=0.4
            ),
            row=1, col=1
        )
        
        # Type bar chart
        fig.add_trace(
            go.Bar(
                x=list(vuln_types.keys()),
                y=list(vuln_types.values()),
                marker=dict(color=self.colors['primary'])
            ),
            row=1, col=2
        )
        
        fig.update_layout(
            plot_bgcolor='#0a0e27',
            paper_bgcolor='#0a0e27',
            font=dict(color='white', size=12),
            height=500,
            showlegend=True
        )
        
        return fig
    
    def create_api_endpoint_map(self, endpoints: List[str]) -> go.Figure:
        """Create visual map of API endpoints"""
        
        # Group endpoints by base path
        endpoint_tree = {}
        for endpoint in endpoints:
            parts = endpoint.strip('/').split('/')
            if parts:
                base = parts[0]
                if base not in endpoint_tree:
                    endpoint_tree[base] = []
                endpoint_tree[base].append(endpoint)
        
        # Create sunburst chart
        labels = ['API Root']
        parents = ['']
        values = [len(endpoints)]
        colors_list = [self.colors['primary']]
        
        for base, eps in endpoint_tree.items():
            labels.append(base)
            parents.append('API Root')
            values.append(len(eps))
            colors_list.append(self.colors['secondary'])
            
            for ep in eps[:10]:  # Limit to 10 per base
                labels.append(ep)
                parents.append(base)
                values.append(1)
                colors_list.append(self.colors['success'])
        
        fig = go.Figure(go.Sunburst(
            labels=labels,
            parents=parents,
            values=values,
            marker=dict(colors=colors_list),
            branchvalues='total'
        ))
        
        fig.update_layout(
            title='API Endpoint Structure',
            plot_bgcolor='#0a0e27',
            paper_bgcolor='#0a0e27',
            font=dict(color='white', size=12),
            height=600
        )
        
        return fig
    
    def create_dashboard(self, all_data: Dict) -> str:
        """Create comprehensive HTML dashboard with all visualizations"""
        
        html_parts = ['''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Eye4Eye - Attack Surface Report</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0a0e27 0%, #1a1d35 100%);
            color: white;
            padding: 20px;
        }
        
        .header {
            text-align: center;
            padding: 40px 20px;
            background: linear-gradient(135deg, #00d4ff 0%, #8338ec 100%);
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0 10px 40px rgba(0, 212, 255, 0.3);
        }
        
        .header h1 {
            font-size: 3em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
        
        .header p {
            font-size: 1.2em;
            opacity: 0.9;
        }
        
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .stat-card {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 25px;
            text-align: center;
            transition: transform 0.3s, box-shadow 0.3s;
        }
        
        .stat-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0, 212, 255, 0.3);
        }
        
        .stat-card h3 {
            color: #00d4ff;
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        
        .stat-card p {
            color: rgba(255, 255, 255, 0.7);
            font-size: 1.1em;
        }
        
        .visualization {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 30px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
        }
        
        .visualization h2 {
            color: #00d4ff;
            margin-bottom: 20px;
            font-size: 1.8em;
        }
        
        .footer {
            text-align: center;
            padding: 20px;
            color: rgba(255, 255, 255, 0.5);
            margin-top: 40px;
        }
        
        .timestamp {
            background: rgba(255, 255, 255, 0.05);
            padding: 10px 20px;
            border-radius: 10px;
            display: inline-block;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>👁️ Eye4Eye</h1>
        <p>Attack Surface Analysis Report</p>
        <p style="font-size: 1.5em; margin-top: 15px;">''' + self.domain + '''</p>
        <div class="timestamp">
            Generated: ''' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '''
        </div>
    </div>
''']
        
        # Add statistics
        subdomains_count = len(all_data.get('subdomains', {}))
        total_ports = sum(len(ports) for ports in all_data.get('ports', {}).values())
        vulnerabilities_count = len(all_data.get('vulnerabilities', []))
        endpoints_count = len(all_data.get('api_endpoints', []))
        
        html_parts.append(f'''
    <div class="stats">
        <div class="stat-card">
            <h3>{subdomains_count}</h3>
            <p>Subdomains Found</p>
        </div>
        <div class="stat-card">
            <h3>{total_ports}</h3>
            <p>Open Ports</p>
        </div>
        <div class="stat-card">
            <h3>{vulnerabilities_count}</h3>
            <p>Potential Issues</p>
        </div>
        <div class="stat-card">
            <h3>{endpoints_count}</h3>
            <p>API Endpoints</p>
        </div>
    </div>
''')
        
        # Add visualizations
        if all_data.get('subdomains'):
            fig = self.create_subdomain_tree(all_data['subdomains'])
            html_parts.append('<div class="visualization"><h2>🌳 Subdomain Tree</h2>')
            html_parts.append(fig.to_html(include_plotlyjs=False, div_id='subdomain-tree'))
            html_parts.append('</div>')
        
        if all_data.get('ports'):
            fig = self.create_port_map(all_data['ports'])
            html_parts.append('<div class="visualization"><h2>🔌 Port Map</h2>')
            html_parts.append(fig.to_html(include_plotlyjs=False, div_id='port-map'))
            html_parts.append('</div>')
        
        if all_data.get('technologies'):
            fig = self.create_tech_stack_graph(all_data['technologies'])
            html_parts.append('<div class="visualization"><h2>⚙️ Technology Stack</h2>')
            html_parts.append(fig.to_html(include_plotlyjs=False, div_id='tech-stack'))
            html_parts.append('</div>')
        
        if all_data.get('vulnerabilities'):
            fig = self.create_vulnerability_chart(all_data['vulnerabilities'])
            html_parts.append('<div class="visualization"><h2>🔒 Vulnerability Analysis</h2>')
            html_parts.append(fig.to_html(include_plotlyjs=False, div_id='vulnerabilities'))
            html_parts.append('</div>')
        
        if all_data.get('api_endpoints'):
            fig = self.create_api_endpoint_map(all_data['api_endpoints'])
            html_parts.append('<div class="visualization"><h2>🔗 API Endpoints</h2>')
            html_parts.append(fig.to_html(include_plotlyjs=False, div_id='api-endpoints'))
            html_parts.append('</div>')
        
        html_parts.append('''
    <div class="footer">
        <p>Generated by Eye4Eye - Attack Surface Mapper</p>
        <p style="margin-top: 10px; font-size: 0.9em;">
            ⚠️ This tool is for authorized security testing only. 
            Unauthorized access to computer systems is illegal.
        </p>
    </div>
</body>
</html>
''')
        
        return ''.join(html_parts)
