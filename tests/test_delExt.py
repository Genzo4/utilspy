import pytest
from utilspy_g4 import delExt


def test_1():
    path = 'test.png'
    newPath = delExt(path)
    assert newPath == 'test'


def test_2():
    path = '/test/test.jpeg'
    newPath = delExt(path)
    assert newPath == '/test/test'


def test_3():
    path = 'c:\\test\\test.p'
    newPath = delExt(path)
    assert newPath == 'c:\\test\\test'


def test_4():
    path = 'd:\\test\\test.png.jpeg'
    newPath = delExt(path)
    assert newPath == 'd:\\test\\test.png'


def test_5():
    path = 'd:\\test\\test.png.jpeg'
    newPath = delExt(path, 2)
    assert newPath == 'd:\\test\\test'


def test_6():
    path = '/test/test.png.jpeg'
    newPath = delExt(path, 2)
    assert newPath == '/test/test'


def test_7():
    path = 'test.jpeg.png'
    newPath = delExt(path, 2)
    assert newPath == 'test'
