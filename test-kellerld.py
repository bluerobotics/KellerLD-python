#!/usr/bin/python3

from kellerLD import KellerLD
from llog import LLogWriter

device = "kellerld"
parser = LLogWriter.create_default_parser(__file__, device, default_frequency=5)
args = parser.parse_args()


with llog.LLogWriter(args.meta, args.output) as log:
    keller = KellerLD(args.bus)
    keller.init()
    log.log_rom(f'{keller.month} {keller.day} {keller.year} {keller.pMin} {keller.pMax} {keller.pModeID}')
    
    def data_getter():
      keller.read()
      return f'{keller.pressure():.6f} {keller.temperature():.2f}'
    
    log.log_data_loop(data_getter, parser_args=args)
