import math
import sys
import time
import csv
from grove.adc import ADC

sensor_is_on = True

class GroveGSRSensor:
 
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    @property
    def GSR(self):
        value = self.adc.read(self.channel)
        return value
 
Grove = GroveGSRSensor
  
def main():
    if len(sys.argv) < 2:
        print('Используется: {} adc_channel'.format(sys.argv[0]))
        sys.exit(1)
 
    sensor = GroveGSRSensor(int(sys.argv[1]))
    
    print('Считывание...')
    while sensor_is_on:
        point=sensor.GSR
        Human_Resistance = ((1024+2*point)*10000)/512
        print('Величина GSR: {0} Ом'.format(Human_Resistance))
        time.sleep(.1)
    return l
        
if __name__ == '__main__':
    main()
