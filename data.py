import os
import requests 
print("downloading with requests")
url = 'https://github.com/gitvcae/mytest/raw/master/ggzero_train' 
r = requests.get(url)
with open("data1", "wb") as code:
  code.write(r.content)

url = 'https://github.com/leedavid/leela-chess-to-Chinese-Chess/raw/master/lc0/ggzero' 
r = requests.get(url)
with open("data0", "wb") as code:
  code.write(r.content)
os.system("data1 --user colabpython --password googlecolab --lc0name data0 --runtime 3600")


