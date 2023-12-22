import Sensor
from Bno055 import * 

import os
import machine

class FileManagement:
    
    def __init__(self, nameFile, triggerCon, echoCon, echo_timeCon, bno055_scl_pinCon, bno055_sda_pinCon):
        
        self.nameFile = nameFile
        self.sensor = Sensor.Sensor(trigger = triggerCon, echo = echoCon, echo_time = echo_timeCon)     # The sensor class is initialized
        self.imu = BNO055(machine.I2C(1,scl=machine.Pin(bno055_scl_pinCon), sda=machine.Pin(bno055_sda_pinCon)))

    def createFile(self):               # The function is responsible for creating the file

        try:        
            with open(self.nameFile, "x") as csv_file:
                csv_file.write("Distance")
        except OSError as e:
            if e.args[0] == 17:
                print("the file already exists")
            else:
                print(e)
        else:
            print("the file was created")

    def addText(self):              # The function is responsible for adding text to the file
        distance = str(self.sensor.Distance_Cm())
        bno_temperature = self.imu.temperature()
        bno_
        try:
            with open(self.nameFile, "a") as csv_file:
                csv_file.write(distance + ',')
        except OSError as e:
            print(e)
    def getText(self):          # The function reads the csv file and returns a list with all the data
        try:
            csv_file = open(self.nameFile, "r")
            lines = csv_file.readlines()
            for line in lines:
                    data = line.split(',')
            csv_file.close()
            os.remove(self.nameFile)
            return data
        except OSError as e:
            print("An error has occurred while handling files", e)    
