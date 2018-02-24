# coding=utf-8
class Base:
    def __init__(self, v):
        self.derived_val = v

    def __repr__(self):
        """
        unambiguous representation of this object
        :return:
        """
        return repr(self.derived_val)

    derived_val = 0


t1 = Base(10)
t2 = Base(20)

t2.derived_val += 1
t2.__class__.derived_val += 2

print t2.derived_val  # --> instance variable
print t2.__class__.derived_val  # --> class variable


class Parent(object):
    x = 1


class Child1(Parent):
    pass


class Child2(Parent):
    pass


print Parent.x, Child1.x, Child2.x
Child1.x = 2
print Parent.x, Child1.x, Child2.x
Parent.x = 3
print Parent.x, Child1.x, Child2.x
"""
What confuses or surprises many about this is that the last line of output is 3 2 3 rather than 3 2 1. Why does changing
the value of Parent.x also change the value of Child2.x, but at the same time not change the value of Child1.x?
The key to the answer is that, in Python, class variables are internally handled as dictionaries. If a variable name is
not found in the dictionary of the current class, the class hierarchy (i.e., its parent classes) are searched until the
referenced variable name is found (if the referenced variable name is not found in the class itself or anywhere in its
hierarchy, an AttributeError occurs).

Therefore, setting x = 1 in the Parent class makes the class variable x (with a value of 1) referenceable in that class
and any of its children. That’s why the first print statement outputs 1 1 1.

Subsequently, if any of its child classes overrides that value (for example, when we execute the statement Child1.x = 2),
then the value is changed in that child only. That’s why the second print statement outputs 1 2 1.

Finally, if the value is then changed in the Parent (for example, when we execute the statement Parent.x = 3), that
change is reflected also by any children that have not yet overridden the value (which in this case would be Child2).
That’s why the third print statement outputs 3 2 3.
"""
