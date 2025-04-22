import argparse
import lzma

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('infile', help='xml file')
arg_parser.add_argument('outfile', help='cw3 file')
args = arg_parser.parse_args()
infile = args.infile
outfile = args.outfile

with open(infile, 'rb') as fin:
    raw = fin.read()
    dat = lzma.compress(raw)
    with open(outfile, 'wb') as fout:
        fout.write(dat)
