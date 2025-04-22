import argparse
import lzma

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('infile', help='cw3 file')
arg_parser.add_argument('outfile', help='xml file')
args = arg_parser.parse_args()
infile = args.infile
outfile = args.outfile

with open(infile, 'rb') as fin:
    dat = fin.read()
    raw = lzma.decompress(dat)
    with open(outfile, 'wb') as fout:
        fout.write(raw)
