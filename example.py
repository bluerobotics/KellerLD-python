from kellerLD import KellerLD
import time

sensor = KellerLD()

if not sensor.init():
	print("Failed to initialize Keller LD sensor!")
	exit(1)

print("Testing Keller LD series pressure sensor")
print("Press Ctrl + C to quit")
time.sleep(3)

while True:
	try:
		sensor.read()
		print("pressure: %7.4f bar\ttemperature: %0.2f C\tdepth: %4.2f m\taltitude %4.2f m" % (sensor.pressure(), sensor.temperature(), sensor.depth(), sensor.altitude()))
		time.sleep(0.2)
	except KeyboardInterrupt:
		break
