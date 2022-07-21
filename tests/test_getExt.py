import pytest
from utilspy_g4 import getExt


def test_1():
    path = 'test.png'
    ext = getExt(path)
    assert ext == 'png'


def test_2():
    path = 'test.png'
    ext = getExt(path, 0)
    assert ext == ''


def test_3():
    path = '/test/test/test.png.jpeg'
    ext = getExt(path)
    assert ext == 'jpeg'


def test_4():
    path = 'd:\\test\\test.png.jpeg'
    ext = getExt(path, 2)
    assert ext == 'png'


def test_5():
    path = '/foo/bar/test.txt.png.jpeg'
    ext = getExt(path, 3)
    assert ext == 'txt'
