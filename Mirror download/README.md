# Mirror download

## 使用b374k_windows_download
1. 基於windows拿到webshell上傳b374k_v2.3
2. 目標cmd執行 chcp 65001 | dir "D:\*.pdf" /b /s >> filepath.txt
3. 產出filepath.txt拖回本機 執行 python3 b374k_windows_download.py filepath.txt
4. 依序產出資料夾並把目標個資料夾資料鏡像下載  
注意:pool可以加快下載，但較容易被發現
