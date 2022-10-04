from adc import ADC


class GroveGSRSensor:
 
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    @property
    def GSR(self):
        value = self.adc.read(self.channel)
        return value

    
def main():
    sensor = GroveGSRSensor(0)
        
    while True:

        point = sensor.GSR

        if point < 512:            
            Human_Resistance = ((1024+2*point)*10000)/(512-point)
            return Human_Resistance

        elif point > 130000:
        	return 'Ошибка! Проверьте датчик!'

        else:
            return 0

    
if __name__ == '__main__':
    main()
