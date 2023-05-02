from refactored_DC import metrics
from refactored_DC.metadata import DNNState, InputData
from refactored_DC.utils import readable
import data as data
import refactored_DC.utils as utils
import refactored_DC.interfaceData as interfaceData
import refactored_DC.settings as settings

from refactored_DC.settings import CLASSIFICATION_KEY, REGRESSION_KEY


# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4