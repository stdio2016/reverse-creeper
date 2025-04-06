import argparse
import gzip
from nbt import CNBTReader

def printTag(t, lv=0):
    if len(t) == 0:
        print('  ' * lv + '{}')
    for k in t:
        v = t[k]
        if isinstance(v, dict):
            print('  ' * lv + k + ':')
            printTag(v, lv+1)
        elif isinstance(v, list):
            print('  ' * lv + k + ':')
            printList(v, lv+1)
        else:
            print('  ' * lv + f'{k}: {repr(v)}')

def printList(t, lv=0):
    if len(t) == 0:
        print('  ' * lv + '[]')
    for v in t:
        if isinstance(v, dict):
            print('  ' * lv + '-')
            printTag(v, lv+1)
        elif isinstance(v, list):
            print('  ' * lv + '-')
            printList(v, lv+1)
        else:
            print('  ' * lv + f'- {repr(v)}')

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('infile')
arg_parser.add_argument('--out')
args = arg_parser.parse_args()
infile = args.infile
outfile = args.out

with open(infile, 'rb') as fin:
    dat = fin.read()
    orig_size = int.from_bytes(dat[0:4], 'little')
    dat = dat[4:]
    raw = gzip.decompress(dat)
    if args.out:
        with open(args.out, 'wb') as fout:
            fout.write(raw)
    reader = CNBTReader(raw)
    try:
        c = reader.readCompound()
    except:
        print(reader.i)
        raise
    printTag(c)
