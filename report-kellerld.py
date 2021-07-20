#!/usr/bin/python3

import argparse
from fpdf import FPDF
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

plt.figure()
log.data.ll.plot(['temperature', 'pressure'], ['temperature'])

plt.show()


pdf = FPDF()
pdf.add_page()
pdf.set_font('Courier')

def table(df):
    widths = {}
    for c in df:
        widths[c] = pdf.get_string_width(c)
        for r in df[c]:
            d = str(r)
            width = pdf.get_string_width(d)
            if width > widths[c]:
                widths[c] = width
        pdf.cell(widths[c]+2, 4, c, border=1)
    pdf.ln(4)
    for r in df.index:
        for c in df:
            pdf.cell(widths[c]+2, 4, str(df[c][r]), border=1)


table(log.rom)
pdf.output('test.pdf')

# def table_helper(pdf, epw, th, table_data, col_num):
#     for row in table_data:
#         maxwidth=0
#         for datum in row:
#             d = str(datum)
#             w = pdf.get_string_width(d)
#             if w > maxwidth:
#                 maxwidth = w
#         for datum in row:
#             # Enter data in columns
#             d = str(datum)
#             pdf.cell(maxwidth + 2, 2 * th, d, border=1)
#         pdf.ln(2 * th)