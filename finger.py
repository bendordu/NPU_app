import time,sys
import RPi.GPIO as GPIO
import smbus

sensorPin = 5
grove_addr = 0x04

# use the bus that matches your raspi version
rev = GPIO.RPI_REVISION
if rev == 2 or rev == 3:
    bus = smbus.SMBus(1)
else:
    bus = smbus.SMBus(0)

class grove_fingerclip_heart_sensor:
	address = 0x04

	def pulse_read(self):
		print(bus.read_byte_data(grove_addr, sensorPin))
		#return bus.read_i2c_block_data(self.address, 1,1)
		#print(bus.read_byte(grove_addr))
        

if __name__ == "__main__":		
	
	pulse= grove_fingerclip_heart_sensor()
	while True:
		try:
			pulse.pulse_read()
		except IOError:
			print("Error")
		time.sleep(.5)