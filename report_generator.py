from datetime import datetime

def generate_html_report(scan_result):
    scan_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    total_ports = len(scan_result["results"])
    total_cves = 0
    critical = 0
    high = 0
    medium = 0
    low = 0

    for result in scan_result["results"]:
        for vuln in result["vulnerabilities"]:

            total_cves += 1
            severity = vuln["severity"].upper()
            if severity == "CRITICAL":
                critical+=1
            elif severity == "HIGH":
                high+=1
            elif severity == "MEDIUM":
                medium+=1
            elif severity == "LOW":
                low+=1

    html = f""" 
    <!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF=8">
            <title>VulnScanX Report</title>
            </head>

            <body>
            <h1>VulnScanX</h1>
            <h2>Network Vulnerability Scan Report</h2>
            <hr>
            <h3>Scan Information</h3>
            <p><strong>Target:</strong> {scan_result["target"]}<p>
            <p><strong>Scan Time:</strong>{scan_time}</p>
            <p><strong>Total Open Ports:</strong> {total_ports}</p>
            <p><strong>Total Vulnerabilities:</strong> {total_cves}</p>
            <p><strong>Critical:</strong> {critical}</p>
            <p><strong>High:</strong> {high}</p>
            <p><strong>Medium:</strong> {medium}</p>
            <p><strong>Low:</strong> {low}</p>
            <hr>

            <h2>Open Ports</h2>
            <table border="1" cellspacing="0" cellpadding="8">
            <tr>
            <th>Port</th>
            <th>Service</th>
            <th>Banner</th>
            <th>Software</th>
            <th>Version</th>
            </tr>
            """
    for result in scan_result["results"]:
        html+= f"""
        <tr>
        <td>{result["port"]}</td>
        <td>{result["service"]}</td>
        <td>{result["banner"]}</td>
        <td>{result["software"]}</td>
        <td>{result["version"]}</td>
        </tr>
        """
    
    html+="""
    </table>
    <br>
    <hr>
    """

    html+="""
    <h2>Vulnerabilities</h2>
    """

    for result in scan_result["results"]:
        html+= f"""
        <h3>Port {result["port"]} ({result["service"]})</h3>
        """
        if len(result["vulnerabilities"]) == 0:
            html+= """
            <p>No known vulnerabilities found.</p>
            """
        else:
            for vuln in result["vulnerabilities"]:
                html+=f"""
                <div>
                <p><strong>CVE:</strong> {vuln["cve"]}</p>
                <p><strong>Severity:</strong> {vuln["severity"]}</p>
                <p><strong>CVSS Score:</strong> {vuln["score"]}</p>
                <p><strong>Description:</strong></p>
                <p>{vuln["description"]}</p>
                <hr>
                </div>
                """



    with open("report.html","w") as file:
        file.write(html)
    print("[+] HTML report generated succesfully.")

    

    