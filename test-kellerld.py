#!/usr/bin/python3

import argparse
from kellerLD import KellerLD
from pathlib import Path
import llog
import time

device = "kellerld"
defaultMeta = Path(__file__).resolve().parent / f"{device}.meta"

parser = argparse.ArgumentParser(description=f'{device} test')
parser.add_argument('--output', action='store', type=str, default=None)
parser.add_argument('--meta', action='store', type=str, default=defaultMeta)
parser.add_argument('--frequency', action='store', type=int, default=5,
                    help="set the measurement frequency")
args = parser.parse_args()


with llog.LLogWriter(args.meta, args.output) as log:
    keller = KellerLD(args.bus)
    keller.init()
    log.log(llog.LLOG_ROM, f'{keller.month} {keller.day} {keller.year} {keller.pMin} {keller.pMax} {keller.pModeID}')

    while True:
        try:
            keller.read()
            log.log(llog.LLOG_DATA, f'{keller.pressure():.6f} {keller.temperature():.2f}')
        except Exception as e:
            log.log(llog.LLOG_ERROR, e)
        if args.frequency:
            time.sleep(1.0/args.frequency)
