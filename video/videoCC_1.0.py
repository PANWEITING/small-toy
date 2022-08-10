from PIL import ImageGrab
from PIL import Image
import numpy as np
import cv2
import time

tt=15#錄製秒數
fps=15
i=0
videoname=time.strftime("%Y%m%d-%H%M%S")+'.avi'

#設定畫質
#width, height = 1920,1080
width, height = 1280,720
#width, height = 640,480


fourcc = cv2.VideoWriter_fourcc(*'XVID')# 使用 XVID 編碼
video = cv2.VideoWriter(videoname, fourcc, fps, (width, height))

print("開始錄製%f秒" % tt)
End_Time=time.time()+tt

while True:
    img_rgb = ImageGrab.grab()
    img_rgb=img_rgb.resize((width, height), Image.Resampling.LANCZOS)
    i+=1
    img_bgr = cv2.cvtColor(np.array(img_rgb), cv2.COLOR_RGB2BGR)
    video.write(img_bgr)
    if time.time() >= End_Time:
        break

video.release()
cv2.destroyAllWindows()
print("結束錄製")
print("畫質%dx%d" % (width, height))
print("擷取張數%d" % i)
print("FPS %d" % fps)