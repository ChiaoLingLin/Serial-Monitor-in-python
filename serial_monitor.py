import universal_collector as uc
import threading
import asyncio
import time

class monitor(uc.serial_target):
    def __init__(self, Port: str, Baud: int):
        super().__init__(Port, Baud)


    def send(self,data):
        asyncio.run(self._send(data))
        print("in")

    async def _send(self,data: str):
        #change here if you want to do something with send data
        self._ser.write(data.encode())
    
    async def activity(self,data):
        #change here if you want to do something with arrived data
        print(data)


def main():
    #start to collect
    collect_monitor = monitor("COM5","115200")

    collect_monitor.serial_init()
        
    task = threading.Thread(target = collect_monitor.collect)
    task.start()
    #start to send
    while True:
        collect_monitor.send(string="as4d65as4d6")
        time.sleep(1)

if __name__ == "__main__":
    main()