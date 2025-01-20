# KellerLD-python

A python module to interface with the LD line of pressure sensors from Keller. Tested on Raspberry Pi 3 with Raspbian.

See the [Keller Communication Protocol 4LD-9LD](http://www.keller-druck2.ch/swupdate/InstallerD-LineAddressManager/manual/Communication_Protocol_4LD-9LD_en.pdf) document for more details on the I<sup>2</sup>C communication protocol, and the [Keller 4LD-9LD Datasheet](https://download.keller-druck.com/api/download/2LfcGMzMbeHdjFbyUd5DWA/en/latest) for sensor specification details.

# Requirements

The python SMBus library must be installed.

```sh
	sudo apt-get install python-smbus
```

# Installation
Run the following to install KellerLD-python

```sh
	pip install git+https://github.com/bluerobotics/KellerLD-python.git@master
```

# Example

Check the minimal example [available here](https://github.com/bluerobotics/KellerLD-python/blob/master/example.py).

# Usage

```py
    from kellerLD import KellerLD
    sensor = KellerLD()
```

### init()

Initialize the sensor. This needs to be called before using any other methods.

```py
    sensor.init()
```

Returns true if the sensor was successfully initialized, false otherwise.

### read()

Read the sensor and update the pressure and temperature.

```py
    sensor.read()
```

Returns True if read was successful, False otherwise.

### pressure()

Get the most recent pressure measurement.

```py
	sensor.pressure()
```

Returns the most recent pressure in bar. Call read() to update.

### temperature()

Get the most recent temperature measurement.

```py
	sensor.temperature()
```

Returns the most recent temperature in degrees Centigrade. Call read() to update.