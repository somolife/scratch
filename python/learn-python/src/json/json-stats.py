"""
run as follows ==>
    python json-stats.py ${JSON_INPUT_FILE}
    e.g. /usr/bin/python2.7 json-stats.py interview.otg-datasample.json

    requires python 2.7
"""

import json

import sys

TYPE = 0
WEIGHT = 1
c_pts = [  # collection points
    ["", "header", "type"],
    ["", "items", "", "weight"]]

collected_types = dict()
collected_weight = 0.0


def collect_stats(item, depth):
    global collected_types, collected_weight

    if isinstance(item, list):
        for x in item:
            collect_stats(x, depth + 1)  # nothing to collect from lists
    elif isinstance(item, dict):
        for i, c_pt in enumerate(c_pts):  # (a) for every collection point
            if len(c_pt) > depth:
                for filtered in filter(lambda (_key, _val): c_pt[depth] == _key, item.items()):  # (b) filter applicable
                    if depth + 1 == len(c_pt):
                        value = filtered[1]  # (c) collect stats
                        if i == TYPE:
                            if value in collected_types:
                                collected_types[value] += 1
                            else:
                                collected_types[value] = 1
                        elif i == WEIGHT:
                            collected_weight += float(value)
                    else:
                        collect_stats(filtered[1], depth + 1)  # (d) recursively


filename = sys.argv[1]
f = open(filename, 'r')
data = json.load(f)
f.close()

collect_stats(data, 0)
print "Data types: "
for k, v in collected_types.items():
    print " " + k + ": " + str(v)
print "Total weight: ", collected_weight
