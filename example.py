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
		if sensor.read():
			print(f"pressure: {sensor.pressure():7.4f} bar\ttemperature: {sensor.temperature():0.2f} C")
		time.sleep(0.2)
	except Exception as e:
		print(e)
