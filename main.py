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
        
    
