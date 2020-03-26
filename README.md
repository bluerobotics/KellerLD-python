# KellerLD-python

A python module to interface with the LD line of pressure sensors from Keller. Tested on Raspberry Pi 3 with Raspbian.

The python SMBus library must be installed.

	`pip install --user --upgrade smbus`

# Usage

    from kellerLD import KellerLD
    sensor = KellerLD()

### init()

Initialize the sensor. This needs to be called before using any other methods.

    sensor.init()

Returns true if the sensor was successfully initialized, false otherwise.

### read()

Read the sensor and update the pressure and temperature.

    sensor.read()

Returns True if read was successful, False otherwise.

### pressure()

Get the most recent pressure measurement.

	sensor.pressure()

Returns the most recent pressure in bar. Call read() to update.

### temperature()

Get the most recent temperature measurement.

	sensor.temperature()

Returns the most recent temperature in degrees Centigrade. Call read() to update.
