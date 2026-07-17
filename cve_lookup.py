import requests

def lookup_cve(software, version):
    keyword = f"{software} {version}"
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    params = {
        "keywordSearch": keyword,
        "resultsPerPage":5
    }

    try:
        response = requests.get(
            url, 
            params=params,
            timeout=10)
    except requests.exceptions.RequestException:
        return[]


    data = response.json()

    cve_list = []

    for vuln in data["vulnerabilities"]:
        cve = vuln["cve"]
        cve_id = cve["id"]
        description = cve["descriptions"][0]["value"]
        #metrics = cve["metrics"]["cvssMetricV2"][0]
        metrics = cve.get("metrics",{})
        score = None
        severity = None
        if "cvssMetricV31" in metrics:
            metric = metrics["cvssMetricV31"][0]

            score = metric["cvssData"]["baseScore"]
            severity = metric["cvssData"]["baseSeverity"]
        elif "cvssMetricV30" in metrics:
            metric = metrics["cvssMetricV30"][0]

            score = metric["cvssData"]["baseScore"]
            severity = metric["cvssData"]["baseSeverity"]
        elif "cvssMetricV2" in metrics:
            metric = metrics["cvssMetricV2"][0]

            score = metric["cvssData"]["baseScore"]
            severity = metric["baseSeverity"]



        entry = {
            "cve":cve_id,
            "score":score if score else "N/A",
            "severity": severity if severity else "UNKNOWN",
            "description": description
        }

        cve_list.append(entry)
    return cve_list


