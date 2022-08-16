# -*- coding: UTF-8 -*-
'''
datapng可關360殺毒、360安全衛士、火絨，缺什麼自己增加
關閉防毒
有administrator權限(需要控制滑鼠)與opencv就能關
win10編exe可正常執行，其他windows系統要解決環境問題，截圖拉回來定位比較實際
'''
import cv2
import pyautogui
import time
import base64
import os
import datapng
import aircv as ac
import sys
        
def Comparison(bigpicture,Smallpicture):#小圖對比大圖抓定位
    try:
        source = cv2.imread(bigpicture)
        target = cv2.imread(Smallpicture)
        match_result = ac.find_template(source, target, 0.5)#圖片準確度，icon話質低自行調整
        print(match_result)
        rect = match_result['rectangle']
        pos_x = (int(rect[0][0]) + int(rect[2][0]))/2
        pos_y = (int(rect[0][1]) + int(rect[1][1]))/2 
        return pos_x, pos_y
    except:
        pass  

def killer():
    try:
        pyautogui.screenshot('desktop.png')
        time.sleep(2)
        pyautogui.hotkey('win', 'b')
        time.sleep(2)
        pyautogui.hotkey('enter')
        time.sleep(2)
        pyautogui.screenshot('desktop.png')
        time.sleep(2)
        pyautogui.rightClick(Comparison(r'desktop.png',r'av.png'))
        time.sleep(2)
        pyautogui.screenshot('desktop.png')
        time.sleep(2)
        pyautogui.moveTo(Comparison(r'desktop.png',r'exit.png'),duration=1)
        pyautogui.click()
        time.sleep(2)    
        pyautogui.screenshot('desktop.png')
        time.sleep(2)
        pyautogui.moveTo(Comparison(r'desktop.png',r'check.png'),duration=1)
        pyautogui.click()
    except:
        pass

def dump_img(img_av,img_exit,img_check):#產生需要圖片
    with open('av.png', 'wb') as img:
        img.write(base64.b64decode(img_av))
    with open('exit.png', 'wb') as img:
        img.write(base64.b64decode(img_exit))
    with open('check.png', 'wb') as img:
        img.write(base64.b64decode(img_check))


def del_img():#刪產生圖片
    os.popen('del /q desktop.png av.png exit.png check.png')

def Prepare(tasklist,working_system):#判斷是否存在防毒，若存在準備對應比對小圖
    for process in tasklist:
        if process in working_system:
            img_av = working_system[process]['icon']
            img_exit = working_system[process]['exit']
            img_check = working_system[process]['check']            
            dump_img(img_av,img_exit,img_check)
            time.sleep(1)
            killer()
            time.sleep(1)
            del_img()

if __name__ == "__main__":
    tasklist = os.popen('wmic process get name').read().replace(' ','').split('\n')
    for process in tasklist:
        if process in datapng.win10_taskname:
            img_av = datapng.win10_taskname[process]['icon']
            img_exit = datapng.win10_taskname[process]['exit']
            img_check = datapng.win10_taskname[process]['check']            
            dump_img(img_av,img_exit,img_check)
            time.sleep(1)
            killer()
            time.sleep(1)
            del_img()
