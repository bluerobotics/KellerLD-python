#!/usr/bin/python3

import argparse
from kellerLD import KellerLD
from llog import *
import os
import signal
import subprocess
import time

dir_path = os.path.dirname(os.path.realpath(__file__))
defaultMeta = dir_path+'/kellerld.meta'

parser = argparse.ArgumentParser()
parser.add_argument('--bus', action='store', type=int, required=True)
parser.add_argument('--frequency', action='store', type=int,
                    default=5, help="set the measurement frequency")
parser.add_argument('--output', action='store', type=str, default=None)
parser.add_argument('--meta', action='store', type=str, default=defaultMeta)
args = parser.parse_args()

log = LLogWriter(args.meta, args.output)

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
