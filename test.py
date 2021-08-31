from kellerLD import KellerLD
import time

sensor = KellerLD(4)

if not sensor.init():
    print("Failed to initialize Keller LD sensor!")
    exit(1)

print("Testing Keller LD series pressure sensor")

for i in range(10):
    try:
        sensor.read()
        print("pressure: %7.4f bar\ttemperature: %0.2f C" % (sensor.pressure(), sensor.temperature()))
        # we shouldn't get anything out of these values in the test hardware
        assert 5 < sensor.temperature() < 50
        assert -1 < sensor.pressure() < 1
        time.sleep(0.2)
    except Exception as e:
        print(e)
