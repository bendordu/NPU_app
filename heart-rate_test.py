import time,sys
import grovepi
import RPi.GPIO as GPIO
#from grove.gpio import GPIO
from grove.i2c import Bus

# # use the bus that matches your raspi version
rev = GPIO.RPI_REVISION
if rev == 2 or rev == 3:
    bus = Bus(1)
else:
    bus = Bus(0)

# Connect the Grove Ear Clip Sensor to digital port D5
sensor_is_on = True
sensorPin = 2
counter = 0
heart_rate = 0

class GroveHeartSensor():
    def __init__(self):
        self.sensor_is_on = True
        self.grove_addr = 0x04
        self.sensorPin = 2
        GPIO.setmode(GPIO.BCM)

def main(): 
    print("Начало имзерений...")
    #GPIO.setup(sensorPin, GPIO.IN)
    while sensor_is_on:
        #GPIO.setup(sensorPin,GPIO.OUT)
        #GPIO.output(sensorPin,1)
        # time.sleep(2)
        data = bus.read_byte_data(msr.grove_addr, msr.sensorPin)
        print(data)
        #time.sleep(.1)
        #time.sleep(2)
        GPIO.output(sensorPin,0)
        
        

    
            
if __name__ == '__main__':
    try:
        msr = GroveHeartSensor()
        main()

    except KeyboardInterrupt:
        GPIO.cleanup()
        print('Прервано!')

    


