from grove.adc import ADC

  
def main():

	emg_list = [12940]

    while True: 

        point = ADC().read_voltage(4)
        emg_list += point

        if abs((emg_list[-2] - point) / 0.1) < 100000:		
		    return point

        else:
        	return 'Ошибка! Проверьте датчик!'
  
        
if __name__ == '__main__':
    main()
