import os
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element
import collections
import json
import re
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('infile')
arg_parser.add_argument('outfile')
args = arg_parser.parse_args()
infile = args.infile
outfile = args.outfile

int_pattern = re.compile('^-?(0|[1-9][0-9]*)$')
float_pattern = re.compile(r'^-?(0|[1-9][0-9]*)(\.\d*)?$')

def can_be_int(s):
    return int_pattern.match(s) is not None

def can_be_float(s):
    return float_pattern.match(s) is not None

class GenSchema:
    children: dict[str, "GenSchema"]
    def __init__(self, name: str):
        self.name = name
        self.optional = False
        self.multiple = False
        self.content = set()
        self.children = collections.OrderedDict()
        self.first_time = True
        self.unordered = False
    def analyze(self, e: Element):
        if len(e) == 0 and e.text is not None:
            self.content.add(e.text[:100])
            return
        count = collections.Counter()
        for ch in e:
            name = ch.tag
            count[name] += 1
            if name not in self.children:
                self.children[name] = GenSchema(name)
                if not self.first_time:
                    self.children[name].optional = True
            self.children[name].analyze(ch)
        # set optional
        for name in self.children:
            if name not in count:
                self.children[name].optional = True
        # set multiple
        has_multiple = 0
        for name in count:
            if count[name] > 1:
                self.children[name].multiple = True
                has_multiple += 1
        self.first_time = False
    def tojson(self):
        return {
            "name": self.name,
            "optional": self.optional,
            "multiple": self.multiple,
            "content": list(self.content)[:10],
            "unordered": self.unordered,
            "children": [self.children[x].tojson() for x in self.children],
        }
    def fromjson(self, j: dict):
        self.name = j['name']
        self.optional = j['optional']
        self.multiple = j['multiple']
        self.content = set(j['content'])
        self.first_time = False
        self.unordered = j.get('unordered', False)
        for x in j['children']:
            name = x['name']
            ch = GenSchema(name)
            ch.fromjson(x)
            self.children[name] = ch
    def quant(self):
        if self.multiple:
            if self.optional:
                return "*"
            return "+"
        if self.optional:
            return "?"
        return ""
    def print(self, lv=0, comma=''):
        if len(self.children) > 0:
            joinchar = ' &' if self.unordered else ','
            print('\t' * lv + 'element ' + self.name + ' {')
            children = self.children.values()
            for i, ch in enumerate(children):
                ch.print(lv+1, joinchar if i < len(children)-1 else '')
            print('\t' * lv + '}' + self.quant() + comma)
        else:
            datatype = 'text'
            if len(self.content) == 0:
                datatype = 'empty'
            else:
                # auto detect type
                if self.content.issubset({'true','false'}):
                    datatype = 'boolean'
                elif all(can_be_int(x) for x in self.content):
                    datatype = 'xsd:integer'
                elif all(can_be_float(x) for x in self.content):
                    datatype = 'xsd:float'
            print('\t' * lv + f'element {self.name} {{ {datatype} }}{self.quant()}{comma}')

with open(infile, 'r', encoding='utf8') as fin:
    dat = fin.read()
    tree = ET.fromstring(dat)

sch = GenSchema(tree.tag)
if os.path.exists(outfile):
    with open(outfile, 'r') as fin:
        sch.fromjson(json.load(fin))

sch.analyze(tree)
with open(outfile, 'w') as fout:
    json.dump(sch.tojson(), fout, indent=1)
print('start = ',end='')
sch.print()
print('boolean = "true" | "false"')
