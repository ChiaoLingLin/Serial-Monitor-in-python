"""
#允許資料來回跳n次
#用封包header計數
#???how
"""



import serial
import time
import threading

class serial_target():
    def __init__(self,Port: str,Baud: int):
        self._Port:str = Port
        self._Baud:int = Baud
        self._collect_interval:float = 0.1 #how long to check serial input
        self._ser: serial.Serial
        self._stop: bool = False
        self._S_INIT: bool = False
        self._buff: str = ""


    #initialize serial
    def serial_init(self)->bool:
        self._S_INIT = False
        try:
            self._ser = serial.Serial(self._Port,self._Baud)# ERROR!!!!
            print("SERIAL INITIALIZATION SUCCESS")
            try:
                self._ser.read(self._ser.in_waiting)
            except:
                pass
            self._S_INIT = True
            return self._S_INIT
        except:
            print("SERIAL INITIALIZATION FAIL")
            self._S_INIT = False
            return self._S_INIT

    def get(self):
        while not self._stop:
            if len(self._buff) > 10:
                yield self._buff
                self._buff = ""


    def _collect_data(self):
        time.sleep(1)
        while not self._stop:
            try:
                data =  self._ser.read(self._ser.in_waiting).decode() #utf-8 ---> str
                if len(data) > 10:
                    self._buff = data
            except:
                data = ""
            time.sleep(self._collect_interval)
    
    def collect_data(self):
        self.task = threading.Thread(target=self._collect_data)# address finction no()
        self.task.start()

    def stop(self):
        self._stop = True
        self.task.join()


    def send_data(self,data):
        self._ser.write(data.encode())

