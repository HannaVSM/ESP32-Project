import Connection
import File_management
import Sensor
import Send_Requests
from Bno055 import *

import machine
import time


try:                                                        # The configuration file is read to obtain the values ​​of the variables
    import Config
    triggerCon = int(Config.configuration['sensor_HC-SR04']['TriggerPin'])
    echoCon = int(Config.configuration['sensor_HC-SR04']['EchoPin'])
    echo_timeCon = int(Config.configuration['sensor_HC-SR04']['EchoTime'])
    sddiCon = Config.configuration['connection']['Sddi']
    passwordCon = Config.configuration['connection']['Password']
    filenameCon = Config.configuration['file']['Filename']
    urlCon = Config.configuration['requests']['Url']
    dataNumberCon = int(Config.configuration['requests']['Datanumber'])
    bno055_scl_pinCon = int(Config.configuration['bno055']['scl_pin'])
    bno055_sda_pinCon = int(Config.configuration['bno055']['sda_pin'])
    
except ImportError as e:
    print('configuration file not found')
time.sleep_ms(1500)
time1 = machine.Timer(1)
time2 = machine.Timer(2)
time3 = machine.Timer(3)

con = Connection.Connection(wifi_name=sddiCon, password=passwordCon)  # The connection class is initialized
sensor  = Sensor.Sensor(trigger = triggerCon, echo = echoCon, echo_time = echo_timeCon)  # The sensor class is initialized    
file = File_management.FileManagement(nameFile=filenameCon, triggerCon=triggerCon, echoCon=echoCon, echo_timeCon=echo_timeCon)
req = Send_Requests.SendRequest(url=urlCon, filenameCon=filenameCon, triggerCon=triggerCon, echoCon=echoCon, echo_timeCon=echo_timeCon, bno055_scl_pinCon=bno055_scl_pinCon, bno055_sda_pinCon = bno055_sda_pinCon ) # The file management class is initialized
imu = BNO055(machine.I2C(1,scl=machine.Pin(bno055_scl_pinCon), sda=machine.Pin(bno055_sda_pinCon)))
data_number_control = dataNumberCon 

def mainFunction(timer_enevet1):
    file.createFile()
    con.createConnection()

def distanceCm(timer_event2):                       # The function is responsible for obtaining the distance data to later display it on the console
    if con.coneectionIsSuccessful():
        distance = sensor.Distance_Cm()
        print("Distance: ", distance)

def sendData(timer_event3):

    if con.coneectionIsSuccessful():                # Verify that the device has an internet connection
        global data_number_control
        file.addText()
        data_number_control -= 1
        if data_number_control == 0:
            print("Sending data")
            req.send()
            data_number_control = dataNumberCon + 1
    else:                                           #If there is no internet connection, retry the connection every 30 seconds
        print("No internet connection")
        if time.time() % 30 == 0:
            con.createConnection()


time1.init(freq = 1, mode = machine.Timer.ONE_SHOT, callback = mainFunction)             # A timer is created to execute the distance code once and not affect the main flow 
time2.init(freq = 1, mode = machine.Timer.PERIODIC, callback= distanceCm)            # A timer is created to execute the distance code periodically and not affect the main flow
time3.init(freq = 1, mode = machine.Timer.PERIODIC, callback= sendData)                # A timer is created to execute the sending code periodically and not affect the main flow

while True:                                             # Ensures that the code inside the ESP32 will not end
    pass