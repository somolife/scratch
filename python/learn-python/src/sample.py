__author__ = 'nigel'


def increment_by(n):
    return lambda x: x + n


by42 = increment_by(42)
print(by42(3))


def average(l):
    return reduce((lambda x, y: x + y), l, 0) / len(l)


myList = [51, 64, 87, 33, 29]
print(average(myList))
print(filter(lambda x: x > 50, myList))
print(map(lambda x: x + 1, myList))

words = ['cat', 'window', 'defenestrate']
for w in words:
    print w, len(w)
for i in range(len(words)):
    print i, words[i]

print (range(10))

tel = {'jack': 4098, 'sape': 4139}
print(tel.get('jack'))
print(tel['sape'])
res = {x: x ** 2 for x in (2, 4, 6)}
print (res)

words2 = words
words2.append(234)
print(words2, len(words2), len(words))


def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


print list(reverse("sgolf"))  # wrapped in list to print, recall the generator is lazy!



# argument unpacking
def parrot(voltage, state='a stiff', action='voom'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it.",
    print "E's", state, "!"


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


class Sic(object):
    """the goal of __repr__ is to be unambiguous and __str__ is to be readable """

    def __repr__(self): return "foo"

    def __str__(self): return "f"


print str(Sic())
print repr(Sic())
