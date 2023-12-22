import machine 
import time

class Sensor:

    def __init__(self, trigger, echo, echo_time= 500*2*30):

        self.triger = machine.Pin(trigger, machine.Pin.OUT)       # Create the trigger pin
        self.triger.value(0)                                      # turn off the trigger pin  
        self.echo = machine.Pin(echo, machine.Pin.IN)             # Create the echo pin
        self.echo_time = echo_time                                # Set a maximum time for read echo pulse 
    
    def Pulse(selft):
        selft.triger.value(0)                   # Set triger off
        time.sleep_us(2)                        # Wait 2us to avoid problems sending the pulse    
        selft.triger.value(1)                   # Send a pulse
        time.sleep_us(10)                       # Sends the pulse for 10 us to the sensor trigger
        selft.triger.value(0)                   # Stops the pulse

        try:
            pulse = machine.time_pulse_us(selft.echo, 1, selft.echo_time)

            '''
            Reads the pulse sent by the receiver, which the variable selft.echo_time 
            indicates the maximum time (in us) that the echo input can take to give 
            a signal

            '''
            return pulse                        # If it detects the pulse, it returns the time it took
        except OSError as e:                    # If it does not detect the pulse, an error occurs
            if e.args[0] == 110:
                raise e('out of range')
            else:
                print("An error has occurred in the sensor reading: ",e)
        
    def Distance_Cm(self):

        pulse_time = self.Pulse()              # Creates a pulse and records the arrival delay time
        distance = (pulse_time/2)/29.15         # Calculate the distance based on the time it takes for the sound signal to travel 1 cm
        return distance