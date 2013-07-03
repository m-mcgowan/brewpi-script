
import time
from brewpiVersion import AvrInfo


def fetchVersionNumber(ser, maxRetries=5):
	retries = 0
	avrVersion = None
	ser.write('n')
	requestVersion = True
	while requestVersion:  # read all lines on serial interface
		lines = ser.readlines()
		for line in lines:
			if line[0] == 'N':
				data = line.strip('\n')[2:]
				avrVersion = AvrInfo(data)
				requestVersion = False
				break
		else:
			retries += 1
			if retries > maxRetries:
				break
			ser.write('n')
			time.sleep(1)

	return avrVersion
