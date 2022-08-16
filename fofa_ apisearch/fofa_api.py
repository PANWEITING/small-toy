import requests
import json
import base64
from multiprocessing import Pool
import sys
import re

def getdata(name):
    query = str(base64.b64encode(bytes(name,'utf8')),encoding='utf8')
    url=f'{FOFA_URL}/api/v1/search/all?email={FOFA_EMAIL}&key={FOFA_KEY}&size=10000&qbase64={query}'
    res=requests.get(url)
    data=json.loads(res.text)['results']
    print('%s搜尋到%d筆資料' % (name,len(data)))
    
    outputfilename=re.sub(r'[\\/:*?|<>"]', "", name)
    f = open(outputfilename+'.txt','a+',encoding="UTF-8")
    for i in data: 
        f.write('%s\n' % (i[0]))
    f.close()

if __name__ == '__main__':
    FOFA_URL="https://fofa.info"
    FOFA_EMAIL="" #YOU fofa email
    FOFA_KEY="" #YOU fofa key
    inputfilename= sys.argv[1]

    with open(inputfilename, 'r',encoding="UTF-8") as f:
        inputdata = f.readlines()

    for d in inputdata:
        name=d.strip('\n')
        getdata(name)
        