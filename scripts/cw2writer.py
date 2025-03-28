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
    tree = ET.parse(infile).getroot()
    prettyxml.unpretty_xml(tree)
    dat = ET.tostring(tree)
    compressed = zlib.compress(dat)
    encrypted = rc4.encrypt_rc4(compressed, ENCRYPT_KEY)
    hexcode = encrypted.hex()
    with open(outfile, 'w') as fout:
        fout.write(hexcode)
