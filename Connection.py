import network
import time
    
class Connection:

        
    def __init__(self, wifi_name, password):
        
        self.wifi_name=wifi_name
        self.password=password
        self.con = network.WLAN(network.STA_IF)

    def createConnection(self):                         # The function is responsible for creating the connection with the wifi network

        elapsed_time = 0
        try:
            self.con.active(True)
            self.con.connect(self.wifi_name, self.password)
            while not self.con.isconnected():
                print("connecting...  time elapsed: ", elapsed_time ,"seconds")
                time.sleep(1)
                elapsed_time += 1
                if elapsed_time == 45:
                    break
        except OSError as e:
            print("An error has occurred in the connection: ",e)
        finally:
            if not self.con.isconnected():
                raise Exception("The connection has not been possible, check your name and password")
            else:
                print("Connected to: ", self.wifi_name)
                print(self.con.ifconfig())
    def coneectionIsSuccessful(self):
        return self.con.isconnected()
    
        