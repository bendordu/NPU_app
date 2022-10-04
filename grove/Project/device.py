import sys
from sys import argv 
import grove_gsr_sensor
import battery_check

value_list = []

def make_measure_GSR():
    sys.argv=[sys.argv[0],'0'] #Передача параметра в список аргументов командной строки, передаваемых сценарию Python. Подключен к аналоговому порту А0, поэтому "0"
    measure = grove_gsr_sensor.main() #Вызов функции модуля, проводящей измерения.
    print(measure)

def check_b():
    battery_data=battery_check.check()
    print(battery_data)

    
if __name__ == '__main__':
    try:
        make_measure_GSR()
        #check_b()
    except KeyboardInterrupt:
        print('Прервано!')
        #data_writer(measure)
