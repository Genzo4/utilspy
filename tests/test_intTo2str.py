import pytest
from utilspy_g4 import intTo2str
import os


def test_1():
    assert intTo2str(2) == '02'

    assert intTo2str(0) == '00'

    assert intTo2str(34) == '34'

    assert intTo2str(10) == '10'
