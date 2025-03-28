import gzip
import zlib
import lzma
import argparse
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
arg_parser.add_argument('file')
args = arg_parser.parse_args()
file = args.file
with open(file, 'rb') as fin:
    dat = fin.read()
    reader = CNBTReader(dat)
    try:
        c = reader.readCompound()
    except:
        print(reader.i)
        raise
    #assert len(dat) == reader.i == uncompressed_len, 'file size error'
    printTag(c)
