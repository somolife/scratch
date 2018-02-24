"""
split and matching (regex)
"""

import re

print re.split('\W+', 'Words, words, words.')
print re.split('(\W+)', 'Words, words, words.')
print re.split('\W+', 'Words, words, words.', 1)
print re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)

m = re.search('(?<=abc)def', 'abcdef')
print m.group(0)
