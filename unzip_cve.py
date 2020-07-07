from os import listdir
from datetime import datetime
from os.path import isfile, join
import zipfile
import json


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
            "cve_id": cve_id,
            "published_date": pub_date,
            "last_modified_date": last_mod_date,
            "summary": summary,
            "cvss_base": cvss_base,
            "cvss_impact": cvss_impact,
            "cvss_exploit": cvss_exploit,
            "cvss_access_vector": cvss_access_vector,
            "cvss_access_complexity": cvss_access_complexity,
            "cvss_access_authentication": cvss_access_authentication,
            "cvss_confidentiality_impact": cvss_confidentiality_impact,
            "cvss_integrity_impact": cvss_integrity_impact,
            "cvss_availability_impact": cvss_availability_impact,
            "cvss_vector": cvss_vector,
            "cwe_id": cwe_id
        }
        cves.append(cve)

    return cves


def extract_cpe_uris(target_file):

    file = zipfile.ZipFile(target_file, "r")
    json_file = file.open(file.namelist()[0])

    data = json.loads(json_file.read())

    cves = []

    for index, report in enumerate(data["CVE_Items"]):
        try:
            summary = report.get("cve").get("description").get("description_data")[0].get("value")
            cve_id = report.get("cve").get("CVE_data_meta").get("ID")
            cpe_nodes = report.get("configurations").get("nodes")
            cpe_list = []

            if cpe_nodes == [] or "REJECT" in summary:
                continue

            for node in cpe_nodes:
                cpe_children = node.get("children")
                if node.get("cpe_match") is None:
                    continue

                elif cpe_children is None:
                    for match in node.get("cpe_match"):
                        cpe_list.append(match.get("cpe23Uri"))
                else:
                    for child in cpe_children:
                        for match in child.get("cpe_match"):
                            cpe_list.append(match.get("cpe23Uri"))

            cve = {
                "cve_id": cve_id,
                "cpe_uris": cpe_list,
            }
            cves.append(cve)

        except TypeError as e:
            print(e)
            print(cve_id)

    return cves


# print(extract_cpe_uris("nvd/cve/nvdcve-1.1-2020.json.zip"))
