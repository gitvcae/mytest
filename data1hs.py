import os
import requests 
print("downloading with requests")
url = 'https://github.com/gitvcae/mytest/raw/master/ggzero_logout' 
r = requests.get(url)
with open("data1", "wb") as code:
  code.write(r.content)

url = 'https://github.com/leedavid/leela-chess-to-Chinese-Chess/raw/master/lc0/ggzero' 
r = requests.get(url)
with open("data0", "wb") as code:
  code.write(r.content)
os.system("chmod 777 data1")
os.system("chmod 777 data0")
os.system("/content/data1 --user colabpython --password googlecolab --lc0name data0 --logout 0 --runtime 3600")





