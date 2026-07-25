# Eye4Eye Output Directory

This directory contains generated scan reports and data exports.

## File Naming Convention

Files are automatically named using the pattern:
```
{domain}_{timestamp}_report.html
{domain}_{timestamp}_data.json
```

Where:
- `{domain}` is the scanned target domain
- `{timestamp}` is in format YYYYMMDD_HHMMSS

## File Types

### HTML Reports
Interactive dashboards with visualizations including:
- Subdomain tree graphs
- Port heatmaps
- Technology stack charts
- Vulnerability analysis
- API endpoint maps

### JSON Data
Raw scan data in JSON format for:
- Integration with other tools
- Custom analysis
- Automation workflows
- Data archival

## Example

After scanning `example.com`, you might see:
```
example.com_20241124_153045_report.html
example.com_20241124_153045_data.json
```

Open the HTML file in any modern web browser to view the interactive report.
