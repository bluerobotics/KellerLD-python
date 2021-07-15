#!/usr/bin/python3

import argparse
from kellerLD import KellerLD
from llogger import LLogger
import signal
import subprocess
import time

parser = argparse.ArgumentParser()
parser.add_argument('--bus', action='store', type=int, required=True)
parser.add_argument('--frequency', action='store', type=int,
                    default=5, help="set the measurement frequency")
parser.add_argument('--output', action='store', type=str, default=None)
args = parser.parse_args()

LLOG_ERROR = 0
# read only memory + factory calibration and serialization type information
LLOG_ROM = 1
# application-specific configuration information
LLOG_CONFIG = 2
# measurement data
LLOG_DATA = 4
# calibration data
LLOG_CALIBRATION = 5

categories = {
    LLOG_ERROR: {
        'name': 'error',
        'columns': [
            ['error code', '-']
        ]
    },
    LLOG_ROM: {
        'name': 'rom',
        'columns': [
            ['month', '-'],
            ['day', '-'],
            ['year', '-'],
            ['pmin', 'bar'],
            ['pmax', 'bar'],
            ['pmode', '[PA,PR,PAA]']
        ]
    },
    LLOG_DATA: {
        'name': 'measurement',
        'columns': [
            ['pressure', 'mbar'],
            ['temperature', 'C'],
        ],
    },
}


log = LLogger(categories, console=True, logfile=args.output)

def cleanup(_signo, _stack):
    log.close()
    exit(0)

signal.signal(signal.SIGTERM, cleanup)
signal.signal(signal.SIGINT, cleanup)

keller = KellerLD(args.bus)
keller.init()
log.log(LLOG_ROM, f'{keller.month} {keller.day} {keller.year} {keller.pMin} {keller.pMax} {keller.pModeID}')

while True:
    try:
        keller.read()
        log.log(LLOG_DATA, f'{keller.pressure():.6f} {keller.temperature():.2f}')
    except Exception as e:
        log.log(LLOG_ERROR, e)
    if args.frequency:
        time.sleep(1.0/args.frequency)
