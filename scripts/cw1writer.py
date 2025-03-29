import argparse
import zlib

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('infile')
arg_parser.add_argument('outfile')
args = arg_parser.parse_args()
infile = args.infile
outfile = args.outfile

with open(infile, 'rb') as fin:
    raw = fin.read()
    dat = zlib.compress(raw)
    with open(outfile, 'wb') as fout:
        fout.write(dat)
