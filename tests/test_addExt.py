import pytest
from utilspy_g4 import addExt


def test_1():
    path = 'c:\\test\\test.png'
    ext = 'ext'
    newPath = addExt(path, ext)
    assert newPath == 'c:\\test\\test.ext.png'


def test_2():
    path = '/test/test.png'
    ext = 'ext'
    newPath = addExt(path, ext)
    assert newPath == '/test/test.ext.png'


def test_3():
    path = 'test.png'
    ext = 'ext'
    newPath = addExt(path, ext)
    assert newPath == 'test.ext.png'


def test_4():
    path = 'c:\\test\\test'
    ext = 'ext'
    newPath = addExt(path, ext)
    assert newPath == 'c:\\test\\test.ext'


def test_5():
    path = 'c:\\test\\test.2.png'
    ext = 'ext'
    newPath = addExt(path, ext)
    assert newPath == 'c:\\test\\test.2.ext.png'

