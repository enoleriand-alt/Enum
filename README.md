# Installing

sudo apt update

sudo apt upgrade

sudo apt install git python3-venv

git clone https://github.com/enoleriand-alt/Enum

# run

python3 -m venv strails

cd strails/

source bin/activate

pip install requests

cd Enum/

python3 Enogans.py 

## you must enter your key

```bash
#!/usr/local/bin/python
import requests
import json
import os

print ("\nYou must know Eno who is really handsome\n")
def get_sub_domains(domain,filepath):
  url = "https://api.securitytrails.com/v1/domain/"+domain+"/subdomains"
  #print(url)
  querystring = {"children_only":"true"}
  headers = {
  'accept': "application/json",
  'apikey': "Your API Key"
  }
  response = requests.request("GET", url, headers=headers, params=querystring)
  result_json=json.loads(response.text)
  sub_domains=[i+'.'+domain for i in result_json['subdomains']]
  f=open(filepath,'w+')
  for i in sub_domains:
  f.write(i+'\n')
  f.close()
  return sub_domains

domain = input("\nEnter Domain name : ")
filepath = input("\nPlease provide a file name to save : ")

get_sub_domains(domain,filepat)
```
