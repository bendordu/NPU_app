import math
import sys
import time
import csv
from grove.adc import ADC

sensor_is_on = True
sys.argv=[sys.argv[0],'2'] 

class GroveHRSensor:
 
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    @property
    def HR(self):
        value = self.adc.read(self.channel)
        return value
 
# Grove = GroveHRSensor
  
def main():
    if len(sys.argv) < 2:
        print('Используется: {} adc_channel'.format(sys.argv[0]))
        sys.exit(1)
 
    sensor = GroveHRSensor(int(sys.argv[1]))
    
    print(sensor.HR)
        
if __name__ == '__main__':
    main()
