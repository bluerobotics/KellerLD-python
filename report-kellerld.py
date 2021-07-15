#!/usr/bin/python3

import argparse
from llogger import LLogReader
import matplotlib.pyplot as plt
parser = argparse.ArgumentParser(description='kellerld test report')
parser.add_argument('--input', action='store', type=str, required=True)
# parser.add_argument('--output', action='store', type=str, required=True)
args = parser.parse_args()

log = LLogReader(args.input)

log.scatter('measurement', ['temperature'], ['pressure', 'pressure'])
log.scatter('measurement', ['temperature'])
log.scatter('measurement', ['pressure'])
# log.scatter('measurement', ['pressure', 'temperature'])
plt.title('BMP280 Pressure + Temperature')
plt.show()
