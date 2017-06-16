import time
import smbus
import struct

class KellerLD(object):

	_SLAVE_ADDRESS = 0x40
	_REQUEST_MEASUREMENT = 0xAC

	def __init__(self, bus=1):
		try:
			self._bus = smbus.SMBus(bus)
		except:
			print("Bus %d is not available.") % bus
			print("Available busses are listed as /dev/i2c*")

	def init(self):
		if self._bus is None:
			print "No bus!"
			return False

		# Read out minimum pressure reading
		self._bus.write_byte(self._SLAVE_ADDRESS, 0x13)
		data = self._bus.read_i2c_block_data(self._SLAVE_ADDRESS, 0, 3)
		
		MSWord = data[1] << 8 | data[2]

		self._bus.write_byte(self._SLAVE_ADDRESS, 0x14)
		data = self._bus.read_i2c_block_data(self._SLAVE_ADDRESS, 0, 3)

		LSWord = data[1] << 8 | data[2]

		self.pMin = MSWord << 16 | LSWord

		# Read out maximum pressure reading
		self._bus.write_byte(self._SLAVE_ADDRESS, 0x15)
		data = self._bus.read_i2c_block_data(self._SLAVE_ADDRESS, 0, 3)
		
		MSWord = data[1] << 8 | data[2]

		self._bus.write_byte(self._SLAVE_ADDRESS, 0x16)
		data = self._bus.read_i2c_block_data(self._SLAVE_ADDRESS, 0, 3)

		LSWord = data[1] << 8 | data[2]

		self.pMax = MSWord << 16 | LSWord
		
		# 'I' for 32bit unsigned int
		self.pMin = struct.unpack('f', struct.pack('I', self.pMin))[0]
		self.pMax = struct.unpack('f', struct.pack('I', self.pMax))[0]

	def read(self):
		if self._bus is None:
			print "No bus!"
			return False
		
		if self.pMin is None or self.pMax is None:
			print "Init required!"
			print "Call init() at least one time before attempting to read()"
			return False

		self._bus.write_byte(self._SLAVE_ADDRESS, self._REQUEST_MEASUREMENT)

		time.sleep(0.01) #10 ms, plenty of time according to spec.

		data = self._bus.read_i2c_block_data(self._SLAVE_ADDRESS, 0, 5)

		statusByte = data[0]
		pressureRaw = data[1] << 8 | data[2]
		temperatureRaw = data[3] << 8 | data[4]

		'''
		# Always busy for some reason
		busy = statusByte & 1 << 5

		if busy:
			print("Conversion is not complete.")
			return
		'''

		if statusByte & 0b11 << 3 :
			print("Invalid mode: %d, expected 0!") % ((statusByte & 0b11 << 3) >> 3)
			exit(1)

		if statusByte & 1 << 2 :
			print("Memory checksum error!")
			exit(1)

		self._pressure = (pressureRaw - 16384) * (self.pMax - self.pMin) / 32768 + self.pMin
		self._temperature = ((temperatureRaw >> 4) - 24) * 0.05 - 50

	def temperature(self):
		if self._temperature is None:
			print "Call read() first to get a measurement"
			return
		return self._temperature

	def pressure(self):
		if self._pressure is None:
			print "Call read() first to get a measurement"
			return
		return self._pressure

if __name__ == '__main__':

	sensor = KellerLD()
	sensor.init()

	while True:
		try:
			sensor.read()
			print("pressure: %7.4f bar\ttemperature: %0.2f C") % (sensor.pressure(), sensor.temperature())
		except Exception as e:
			print e

