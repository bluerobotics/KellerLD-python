#!/usr/bin/python3

import argparse
from llog import LLogReader
import matplotlib.pyplot as plt
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
defaultMeta = dir_path+'/kellerld.meta'

parser = argparse.ArgumentParser(description='kellerld test report')
parser.add_argument('--input', action='store', type=str, required=True)
parser.add_argument('--output-dir', action='store', type=str, required=True)
parser.add_argument('--meta', action='store', type=str, default=defaultMeta)
args = parser.parse_args()

log = LLogReader(args.input, args.meta)

p = log.data.pressure
t = log.data.temperature

p.ll.pplot(t)
plt.title('KellerLD Pressure + Temperature')
plt.show()
