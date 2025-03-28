from xml.etree import ElementTree as ET

def pretty_xml(tree: ET.Element, lv=0):
    if len(tree) > 0:
        can_pretty = tree.text is None or tree.text.strip() == ''
        for ch in tree:
            if ch.tail is not None and ch.tail.strip() != '':
                can_pretty = False
            pretty_xml(ch, lv+1)
        if can_pretty:
            tree.text = '\n' + '\t' * (lv+1)
            for ch in tree:
                ch.tail = '\n' + '\t' * (lv+1)
            tree[-1].tail = '\n' + '\t' * lv
        else:
            print('mixed content found!!', tree)

def unpretty_xml(tree: ET.Element):
    if len(tree) > 0:
        can_unpretty = tree.text is None or tree.text.strip() == ''
        for ch in tree:
            if ch.tail is not None and ch.tail.strip() != '':
                can_unpretty = False
            unpretty_xml(ch)
        if can_unpretty:
            tree.text = ''
            for ch in tree:
                ch.tail = ''
            tree[-1].tail = ''
        else:
            print('mixed content found!!', tree)
