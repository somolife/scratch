"""
run as follows ==>
    python json-to-csv.py ${JSON_INPUT_FILE}
    e.g. /usr/bin/python2.7 json-to-csv.py interview.otg-datasample.json

    requires python 2.7
"""

import json

import sys

OBJECT = -1
LIST = 0
DICT = 1


def get_type(item):
    if isinstance(item, list):
        return LIST
    elif isinstance(item, dict):
        return DICT
    else:
        return OBJECT


def create_indent(num):
    val = ""
    for i in range(num):
        val += ","
    return val


def print_indented(indent, values):
    print indent,
    for v in values:
        print v, ",",
    print ""


def format_map(depth, item):
    keys = item.keys()
    key_set = set()
    extras = dict()
    for key in keys:
        value = item[key]
        if get_type(value) == OBJECT:
            key_set.add(key)
        else:
            extras[key] = value
    indent = create_indent(depth)
    for key, value in extras.items():
        print "---"
        print indent, key
        format_item(value, depth + 1)
    keys = list(key_set)
    print_indented(indent, keys)
    print_indented(indent, map(lambda x: item[x], keys))


def format_item(item, depth):
    d_type = get_type(item)
    if d_type == LIST:
        map(lambda x: format_item(x, depth + 1), item)
    elif d_type == DICT:
        format_map(depth, item)
    else:
        print item


filename = sys.argv[1]
f = open(filename, 'r')
data = json.load(f)
f.close()

format_item(data, 0)
