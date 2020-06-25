from os import listdir
from datetime import datetime
from os.path import isfile, join
import zipfile
import json

files = [f for f in listdir("nvd/") if isfile(join("nvd/", f))]
files.sort()

file = zipfile.ZipFile("nvd/nvdcve-1.1-2020.json.zip", "r")
json_file = file.open(file.namelist()[0])

data = json.loads(json_file.read())

# print(data.get("CVE_data_type"))
# print(data.get("CVE_data_format"))
# print(data.get("CVE_data_version"))
# print(data.get("CVE_data_numberOfCVEs"))
# print("------------")

cve = data.get("CVE_Items")[0]

# print(cve)
# print(json.dumps(cve, indent=4))


def extract_data_from_zip(target_file):
    """unzip the file, parse the data and return a list of CVEs"""

    file = zipfile.ZipFile(target_file, "r")
    json_file = file.open(file.namelist()[0])

    data = json.loads(json_file.read())

    cves = []

    for index, report in enumerate(data["CVE_Items"]):

        try:

            cve_id = report.get("cve").get("CVE_data_meta").get("ID")
            last_mod_date = datetime.strptime(report.get("lastModifiedDate"), "%Y-%m-%dT%H:%MZ")
            pub_date = datetime.strptime(report.get("publishedDate"), "%Y-%m-%dT%H:%MZ")
            summary = report.get("cve").get("description").get("description_data")[0].get("value")
            impact = report.get("impact")

            if "REJECT" in summary:
                continue

            if impact != {}:
                baseMetricV2 = impact.get("baseMetricV2")

                cvss_base = baseMetricV2.get("cvssV2").get("baseScore")
                cvss_impact = baseMetricV2.get("impactScore")
                cvss_exploit = baseMetricV2.get("exploitabilityScore")
                cvss_access_vector = baseMetricV2.get("cvssV2").get("accessVector")
                cvss_access_complexity = baseMetricV2.get("cvssV2").get("accessComplexity")
                cvss_access_authentication = baseMetricV2.get("cvssV2").get("authentication")
                cvss_confidentiality_impact = baseMetricV2.get("cvssV2").get("confidentialityImpact")
                cvss_integrity_impact = baseMetricV2.get("cvssV2").get("integrityImpact")
                cvss_availability_impact = baseMetricV2.get("cvssV2").get("availabilityImpact")
                cvss_vector = baseMetricV2.get("cvssV2").get("vectorString")
                cwe_id = report.get("cve").get("problemtype").get("problemtype_data")[0].get("description")[0].get("value")
            else:

                cvss_base = None
                cvss_impact = None
                cvss_exploit = None
                cvss_access_vector = None
                cvss_access_complexity = None
                cvss_access_authentication = None
                cvss_confidentiality_impact = None
                cvss_integrity_impact = None
                cvss_availability_impact = None
                cvss_vector = None

        except AttributeError as e:
            print(e)
            print(cve_id)
            print(report.get("impact"))
            print(summary)
            print("------------")
            continue

        cve = {
            "cveId": cve_id,
            "publishedDate": pub_date,
            "lastModifiedDate": last_mod_date,
            "summary": summary,
            "cvssBase": cvss_base,
            "cvssImpact": cvss_impact,
            "cvssExploit": cvss_exploit,
            "cvssAccessVector": cvss_access_vector,
            "cvssAccessComplexity": cvss_access_complexity,
            "cvssAccessAuthentication": cvss_access_authentication,
            "cvssConfidentialityImpact": cvss_confidentiality_impact,
            "cvssIntegrityImpact": cvss_integrity_impact,
            "cvssAvailabilityImpact": cvss_availability_impact,
            "cvssVector": cvss_vector,
            "cweId": cwe_id
        }
        cves.append(cve)

    return cves


print(extract_data_from_zip("nvd/nvdcve-1.1-2020.json.zip")[-1]["cveId"])
