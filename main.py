import serial_moniter as sm
import propagate_rule as pr
import data_format as dataf
import user2web as u2w
import atexit


esp32 = sm.serial_target('/dev/ttyUSB0',115200)
esp32.serial_init()
esp32.collect_data()
atexit.register(esp32.stop)

#-----------test------------
import testfile

dummy = dataf.user2web_format("home","Lin","safe")

def send():
    esp32.send_data(dataf.d2j(dummy))

testfile.target_fn(send)

#---------------------------


for data in esp32.get():
    print(data)
    data = dataf.j2d(data)   
    if pr.check_iter(data):
        if data['dtype'] == "u2w":
            if u2w.upload(data):
                pass
            else:
                esp32.send_data(dataf.d2j(data))
        
    
