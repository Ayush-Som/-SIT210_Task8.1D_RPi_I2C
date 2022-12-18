#System management bus library preinstalled after enabling I2C option
import smbus
import time

#I2C addresses 7 bit addresses in hexa decimal format for BH1750 sensor
address = 0x23	#BH1750 sensor default address given by the industry itself
start = 0x01	#LSB for starting the data transfer
stop = 0x00	#LSB for stopping the data transfer
reset = 0x07	#An address used for resetting the whole process

#Instantiatng
bus = smbus.SMBus(1)

#A fucntion to read the data from the sensor in bytes and convert it to recognizable values
def lightRead():
	newAddress = bus.read_i2c_block_data(address, address)
	value = lightConversion(newAddress)
	return value
	
def lightConversion(newAddress):
	conversion = ((newAddress[1] + (256 * newAddress[0]))/1.2)
	return conversion

#Main conditions and overall output
try:
	while 1:
		intensity = lightRead()
		print(f"Intensity Reading: {intensity}")
		
		if(intensity >= 4000):
			print("Status: Brightest")
		elif(intensity >= 500 and intensity < 4000):
			print("Status: Bright")
		elif(intensity >= 100 and intensity < 500):
			print("Status: Medium")
		elif(intensity > 50 and intensity < 100):
			print("Status: Dark")
		elif(intensity < 50):
			print("Status: Darkest")
		time.sleep(1)
except KeyboardInterrupt:
	print("Exitting")
