import argparse
import zlib
from xml.etree import ElementTree as ET

import rc4
import prettyxml

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('infile')
arg_parser.add_argument('outfile')
args = arg_parser.parse_args()
infile = args.infile
outfile = args.outfile

ENCRYPT_KEY = b'bsg2004'

with open(infile, 'r', encoding='utf8') as fin:
    hexcode = fin.read()
    encrypted = bytes.fromhex(hexcode)
    compressed = rc4.encrypt_rc4(encrypted, ENCRYPT_KEY)
    dat = zlib.decompress(compressed)
    tree = ET.fromstring(dat.decode('utf8'))
    prettyxml.pretty_xml(tree)
    with open(outfile, 'wb') as fout:
        fout.write(ET.tostring(tree))
