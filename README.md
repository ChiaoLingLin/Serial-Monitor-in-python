# Serial-Monitor-in-python
 
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
| `serial_target.serial_init()`   |初始化serial接口       |
| `serial_target.collect_data()`| 樹梅派開始從serial接收資料       |
| `serial_target.send_data(<string data>)` | 樹梅派從serial傳送data至esp32       |
| `serial_target.get()`| 樹梅派從serial拿取資料內容            |
| `serial_target.stop()`| 停止所有工作|