import tempfile, os, zipfile
os.system("pip install requests")

import requests
response = requests.get("https://github.com/SeanWoo/CalcSeanWoo/archive/master.zip")


file = tempfile.TemporaryFile()
file.write(response.content)
zipArchive = zipfile.ZipFile(file)
zipArchive.extractall('Calc/')
zipArchive.close()

os.system("python Calc/CalcSeanWoo-master/CalcSeanWoo/main.py")