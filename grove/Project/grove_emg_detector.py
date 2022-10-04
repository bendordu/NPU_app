import math
import sys
import time
import csv
from grove.adc import ADC

sys.argv=[sys.argv[0],'4'] #Датчик подключен к аналоговому порту А4, поэтому "4"
sensor_is_on = True

class GroveEMGdetector:
 
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    @property
    def EMG(self):
        value = self.adc.read(self.channel)
        return value
 
Grove = GroveEMGdetector
  
def main():
    if len(sys.argv) < 2:
        print('Используется: {} adc_channel'.format(sys.argv[0]))
        sys.exit(1)
 
    sensor = GroveEMGdetector(int(sys.argv[1]))
    
    print('Считывание...')
    while sensor_is_on:
        point=sensor.EMG
        print('Величина EMG: {0} '.format(point))
        time.sleep(.01)        
        
if __name__ == '__main__':
    main()

