import requests

def lookup_cve(software, version):
    keyword = f"{software} {version}"
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    params = {
        "keywordSearch": keyword,
        "resultsPerPage":5
    }

    response = requests.get(url, params=params)
    data = response.json()

    cve_list = []

    for vuln in data["vulnerabilities"]:
        cve = vuln["cve"]
        cve_id = cve["id"]
        description = cve["descriptions"][0]["value"]
        metrics = cve["metrics"]["cvssMetricV2"][0]
        score = metrics["cvssData"]["baseScore"]
        severity = metrics["baseSeverity"]

        entry = {
            "cve":cve_id,
            "score":score,
            "severity": severity,
            "description": description
        }

        cve_list.append(entry)
    return cve_list


