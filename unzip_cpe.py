import pprint
import zipfile
from lxml import etree


# print(root[1].getchildren())

# for c in root[1].getchildren():
#     print(c.tag)

# print(etree.QName(root[1]).localname)

# for child in root[1:]:
#     print(child.items())

# # gets all subelements
# for child in root[1].getiterator():
#     print(child.text if child.text is not None else "")


def check_empty(val):
    return None if val == "*" else val


def check_len(val):
    return [None, val] if len(val.split(" ")) > 1 else [val, None]


def parse_xml(target_file):
    file = zipfile.ZipFile(target_file)
    root = etree.parse(file.open(file.namelist()[0])).getroot()

    cpe_items = []

    vendors = set()

    products = set()

    for cpe_item in root[1:]:
        references = []
        for child in cpe_item.getchildren():
            if etree.QName(child).localname == "title":
                title = child.text

            if etree.QName(child).localname == "cpe23-item":
                name = child.get("name").split(":")

                part = check_empty(name[2].replace("/", ""))
                vendor = check_empty(name[3].replace("\\", ""))  # noqa: F841
                product = check_empty(name[4].replace("\\", ""))  # noqa: F841
                version = check_empty(name[5])
                update_version = check_empty(name[6])
                edition = check_empty(name[7])
                lang = check_empty(name[8])
                sw_edition = check_empty(name[9])
                target_sw = check_empty(name[10])
                target_hw = check_empty(name[11])
                other = check_empty(name[12])

            if etree.QName(child).localname == "references":
                refs = child.getchildren()
                for reference in refs:
                    url = reference.attrib.get("href")
                    ref_type, description = check_len(reference.text)

                    ref_data = {"url": url, "desc": description, "type": ref_type}
                    references.append(ref_data)

        cpe_data = {
            "title": title,
            "part": part,
            "version": version,
            "update_version": update_version,
            "version": version,
            "update_version": update_version,
            "edition": edition,
            "lang": lang,
            "sw_edition": sw_edition,
            "target_sw": target_sw,
            "target_hw": target_hw,
            "other": other,
            "references": references,
            "vendor": {
                "name": vendor,
            },
            "product": {
                "name": product
            },
        }

        cpe_items.append(cpe_data)
        vendors.add(vendor)
        products.add(product)

    return {
        "cpes": cpe_items,
        "vendors": vendors,
        "products": products,
    }


# print(parse_xml("nvd/cpe/test.xml.zip")["cpes"][3])
# print(len(parse_xml("nvd/cpe/test.xml.zip")["products"]))
