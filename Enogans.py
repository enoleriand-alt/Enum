#!/usr/local/bin/python
import requests
import json
import os
print ("""
					.,,cccd$$$$$$$$$$$ccc,
                                     ,cc$$$$$$$$$$$$$$$$$$$$$$$$$cc,
                                   ,d$$$$$$$$$$$$$$$$"J$$$$$$$$$$$$$$c,
                                 d$$$$$$$$$$$$$$$$$$,$" ,,`?$$$$$$$$$$$$L
                               ,$$$$$$$$$$$$$$$$$$$$$',J$$$$$$$$$$$$$$$$$b
                              ,$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$i `$h
                              $$$$$$$$$$$$$$$$$$$$$$$$$P'  "$$$$$$$$$$$h $$
                             ;$$$$$$$$$$$$$$$$$$$$$$$$F,$$$h,?$$$$$$$$$$h$F
                             `$$$$$$$$$$$$$$$$$$$$$$$F:??$$$:)$$$$P",. $$F
                              ?$$$$$$$$$$$$$$$$$$$$$$(   `$$ J$$F"d$$F,$F
                               ?$$$$$$$$$$$$$$$$$$$$$h,  :P'J$$F  ,$F,$"
                                ?$$$$$$$$$$$$$$$$$$$$$$$ccd$$`$h, ",d$
                                 "$$$$$$$$$$$$$$$$$$$$$$$$",cdc $$$$"
                        ,uu,      `?$$$$$$$$$$$$$$$$$$$$$$$$$$$c$$$$h
                    .,d$$$$$$$cc,   `$$$$$$$$$$$$$$$$??$$$$$$$$$$$$$$$,
                  ,d$$$$$$$$$$$$$$$bcccc,,??$$$$$$ccf `"??$$$$??$$$$$$$
                 d$$$$$$$$$$$$$$$$$$$$$$$$$h`?$$$$$$h`:...  d$$$$$$$$P
                d$$$$$$$$$$$$$$$$$$$$$$$$$$$$`$$$$$$$hc,,cd$$$$$$$$P"
            =$$?$$$$$$$$P' ?$$$$$$$$$$$$$$$$$;$$$$$$$$$???????",,
               =$$$$$$F       `"?????$$$$$$$$$$$$$$$$$$$$$$$$$$$$$bc
               d$$F"?$$k ,ccc$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$i
        .     ,ccc$$c`""u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P",$$$$$$$$$$$$h
     ,d$$$L  J$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" `""$$$??$$$$$$$
   ,d$$$$$$c,"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F       `?J$$$$$$$'
  ,$$$$$$$$$$h`$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F           ?$$$$$$$P""=,
 ,$$$F?$$$$$$$ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F              3$$$$II"?$h,
 $$$$$`$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P"               ;$$$??$$$,"?"
 $$$$F ?$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P",z'                3$$h   ?$F
        `?$$$$$$$$$$$$$$$??$$$$$$$$$PF"',d$P"                  "?$F
           """""""         ,z$$$$$$$$$$$$$P
                          J$$$$$$$$$$$$$$F
                         ,$$$$$$$$$$$$$$F
                         :$$$$$c?$$$$PF'
                         `$$$$$$$P
                          `?$$$$F""")
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

domain=input("\nEnter Domain name : ")
filepath=input("\nPlease provide a file name to save : ")
get_sub_domains(domain,filepath)
