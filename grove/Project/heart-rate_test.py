import time,sys
import grovepi
import RPi.GPIO as GPIO
#from grove.gpio import GPIO
from grove.i2c import Bus

# use the bus that matches your raspi version
rev = GPIO.RPI_REVISION
if rev == 2 or rev == 3:
    bus = Bus(1)
else:
    bus = Bus(0)

# Connect the Grove Ear Clip Sensor to digital port D5

class GroveHeartSensor():
    def __init__(self):
        self.sensor_is_on = True
        self.grove_addr = 0x04
        self.sensorPin = 5
        #GPIO.setmode(GPIO.BCM)

def main(): 
    print("Начало имзерений...")
    time.sleep(1)
    while msr.sensor_is_on:
        #GPIO.setup(msr.sensorPin,GPIO.OUT)
        #GPIO.output(msr.sensorPin,1)
        #time.sleep(2)
        data = bus.read_byte_data(msr.grove_addr, msr.sensorPin)
        print(data)
        #GPIO.output(msr.sensorPin,0)
        time.sleep(2)
        

    
            
if __name__ == '__main__':
    try:
        msr = GroveHeartSensor()
        main()

    except KeyboardInterrupt:
        GPIO.cleanup()
        print('Прервано!')

    


