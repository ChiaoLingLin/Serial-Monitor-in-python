
### 地震盒－樹梅派與esp32
-----------
##### 環境
 - python

 - - -
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