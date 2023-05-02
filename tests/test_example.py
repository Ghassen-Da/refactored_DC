import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import metrics

print(metrics)
# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4