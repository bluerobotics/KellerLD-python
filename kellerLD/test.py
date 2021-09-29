#!/usr/bin/python3

from kellerLD import KellerLD
from llog import LLogWriter

device = "kellerLD"
parser = LLogWriter.create_default_parser(__file__, device)
args = parser.parse_args()

with LLogWriter(args.meta, args.output) as log:
    keller = KellerLD()
    if not keller.init():
        print("Failed to initialize Keller LD sensor!")
        exit(1)
    def data_getter():
        keller.read()
        return f'{keller.pressure()} {keller.temperature()}'
    log.log_data_loop(data_getter, parser_args=args)
