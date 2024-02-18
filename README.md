
### 地震盒－樹梅派與esp32
-----------
##### 環境
 - python

 - - -
 ### 模組關聯性
![](https://raw.githubusercontent.com/ChiaoLingLin/Serial-Monitor-in-python/main/relation.jpg)

---
##### serial_moniter.py
樹梅派與esp32之間使用USB serial的數據傳輸監控視窗，使用class建立不同函式類別  
###### 需要模組:
 - serial
 - time
 - threading
 
###### 程式碼說明:

| function name | description                    |
| ------------- | ------------------------------ |
| `serial_target(<string port> , <int baud>)`| 輸入樹梅派與esp32的port與Baud，即可建立一個serial接口 |
| `serial_target.serial_init()`   |初始化serial接口，回傳值為boolyn       |
| `serial_target.collect_data()`| 樹梅派開始從serial接收資料       |
| `serial_target.send_data(<string data>)` | 樹梅派從serial傳送data至esp32       |
| `serial_target.get()`| 樹梅派從serial拿取資料內容            |
| `serial_target.stop()`| 停止所有工作|

 - - -
##### data_format.py
建立資料在不同裝置間傳送的格式，使用json語法將資料在dictionary與string之間轉換，較容易管理不同資料
###### 需要模組:
 - copy
 - json
 
###### 資料基本格式:
````python
DEFULT_DICT = {
    "iter": 0,             #資料在裝置之間傳送的累積次數，ex.esp32-A傳到esp32-B，iter就+1
    "dtype":"none",        #資料傳送的方法，ex.樹梅派傳送到雲端的dtype為"u2w"
    "o_place":"none",      #記錄使用者原始位置
    "user_name":"none",    #記錄使用者姓名
    "status":"none"        #記錄使用者生命狀態
}
````
###### 程式碼說明:

| function name | description                    |
| ------------- | ------------------------------ |
| `user2web_format(<string place>,<string name>,<string status>)` | 輸入place、name、status，可將使用者的位置、姓名、狀態上傳至雲端資料庫       |
| `raw_gen()`| 建立資料格式副本 |
| `j2d(<string data>)`   |輸入data，將資料格式從string轉換為dictionary   |
| `d2j(<dictionary data>)`| 輸入data，將資料格式從dictionary轉換為 string   |
---

##### propagate_rule.py
定義資料傳送的規則
###### 需要模組:
無
###### 程式碼說明:

| function name | description                    |
| ------------- | ------------------------------ |
| `MAX_ITER` | 自定義資料最大傳送累積次數       |
| `check_iter(<dictionary data>)` | 輸入dictionary格式的data，確認此筆資料中"iter"是否超過自定義的MAX_ITER，回傳值為boolyn      |

 - - -
##### user2web.py (待修改)
將樹梅派蒐集到的資料上傳至雲端
###### 需要模組(待修改):
無
 
###### 程式碼說明(待修改):

| function name | description                    |
| ------------- | ------------------------------ |
| `upload(<data>)`| 將data上傳至雲端，回傳值為boolyn |

###### 程式碼目前架構(待修改):
````python
def upload(data) -> bool:
    try:
        print("uplaod success")
        return True 
    except:
        print('upload fail')
        return False
````
---

##### phone2pi.py (待修改)
手機傳送資料至樹梅派，
###### 需要模組:
- threading
 
###### 程式碼說明:

| function name | description                    |
| ------------- | ------------------------------ |
| ``| ? |
| ``| ? |
###### 程式碼目前架構(待修改):
````python

````
##### testfile.py
測試文件，使用者可在終端機輸入資料按下enter進行測試
###### 需要模組:
- threading
 
###### 程式碼說明:

| function name | description                    |
| ------------- | ------------------------------ |
| `fire(fn)`| ? |
| `target_fn(fn)`| ? |
--------------------------------------------
---


### 基本功能展示
````python
import serial_moniter as sm
import propagate_rule as pr
import data_format as dataf
import user2web as u2w
import atexit


esp32 = sm.serial_target('/dev/ttyUSB0',115200) #create object 
esp32.serial_init() #initialize serial
esp32.collect_data() #start to collect data
atexit.register(esp32.stop) #stop when press ctrl C

#-----------test------------
import testfile

dummy = dataf.user2web_format("home","Lin","safe")

def send():
    esp32.send_data(dataf.d2j(dummy))

testfile.target_fn(send)

#---------------------------


for data in esp32.get(): #esp32.get() envalue to data 
    print(data)
    data = dataf.j2d(data)  #datatype changed from json to dictionary
    if pr.check_iter(data): 
        if data['dtype'] == "u2w": #check propagate type
            if u2w.upload(data):
                pass
            else:
                esp32.send_data(dataf.d2j(data))
        
    

````



