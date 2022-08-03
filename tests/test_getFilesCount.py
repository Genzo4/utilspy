import pytest
from utilspy_g4 import getFilesCount
import os


def test_1():
    assert getFilesCount('tests/test_getFilesCount/foo_?.txt') == 3

    assert getFilesCount('tests/test_getFilesCount/bar_*.txt') == 2

    assert getFilesCount('tests/test_getFilesCount/foo.txt') == 1

    assert getFilesCount('tests/test_getFilesCount/test_?.txt') == 0

    assert getFilesCount('tests/test_getFilesCount_test/foo_?.txt') == 0
