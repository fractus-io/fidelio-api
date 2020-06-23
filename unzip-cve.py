from os import listdir
from os.path import isfile, join
import zipfile
import json

files = [f for f in listdir("nvd/") if isfile(join("nvd/", f))]
files.sort()
# print(files)

num = 0

for file in files:
    print(join("nvd/", file))

    archive = zipfile.ZipFile(join("nvd/", file), 'r')

    jsonfile = archive.open(archive.namelist()[0])
    cve_dict = json.loads(jsonfile.read())

    # print("CVE_data_timestamp: " + str(cve_dict['CVE_data_timestamp']))
    # print("CVE_data_version: " + str(cve_dict['CVE_data_version']))
    # print("CVE_data_format: " + str(cve_dict['CVE_data_format']))
    print("CVE_data_numberOfCVEs: " + str(cve_dict['CVE_data_numberOfCVEs']))
    num += int(cve_dict.get("CVE_data_numberOfCVEs"))
    # print("CVE_data_type: " + str(cve_dict['CVE_data_type']))

    jsonfile.close()

print(f"number of records in future db: {num}")
