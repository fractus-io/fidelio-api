import requests

r_file = requests.get("https://nvd.nist.gov/feeds/xml/cpe/dictionary/official-cpe-dictionary_v2.3.xml.zip",
                      stream=True
                      )
with open("nvd/cpe/test.xml.zip", "wb") as f:
    for chunk in r_file:
        f.write(chunk)
