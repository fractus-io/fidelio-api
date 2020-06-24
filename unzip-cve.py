from os import listdir
from os.path import isfile, join
import zipfile
import json

files = [f for f in listdir("nvd/") if isfile(join("nvd/", f))]
files.sort()
# print(files)


# for file in files:
#     print(join("nvd/", file))

#     archive = zipfile.ZipFile(join("nvd/", file), 'r')

#     jsonfile = archive.open(archive.namelist()[0])
#     cve_dict = json.loads(jsonfile.read())

#     # print("CVE_data_timestamp: " + str(cve_dict['CVE_data_timestamp']))
#     # print("CVE_data_version: " + str(cve_dict['CVE_data_version']))
#     # print("CVE_data_format: " + str(cve_dict['CVE_data_format']))
#     print("CVE_data_numberOfCVEs: " + str(cve_dict['CVE_data_numberOfCVEs']))
#     num += int(cve_dict.get("CVE_data_numberOfCVEs"))
#     # print("CVE_data_type: " + str(cve_dict['CVE_data_type']))

#     jsonfile.close()

file = zipfile.ZipFile("nvd/nvdcve-1.1-2020.json.zip", "r")
json_file = file.open(file.namelist()[0])

data = json.loads(json_file.read())

# print(data.get("CVE_data_type"))
# print(data.get("CVE_data_format"))
# print(data.get("CVE_data_version"))
# print(data.get("CVE_data_numberOfCVEs"))
# print("------------")

print(data.get("CVE_Items")[0].keys())
print("------------")
print(data.get("CVE_Items")[0].get("cve"))
print("------------")
print(data.get("CVE_Items")[0].get("impact"))
print("------------")
print(data.get("CVE_Items")[0].get("configurations"))

# for index, thing in enumerate(data.get("CVE_Items")):
#     print(index, "nice"
#           if all([data.get("CVE_Items")[0].get("cve"),
#                  data.get("CVE_Items")[0].get("impact"),
#                  data.get("CVE_Items")[0].get("configurations")
#                   ]) else ":(")
