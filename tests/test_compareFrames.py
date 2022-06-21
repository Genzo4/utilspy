import pytest
from utilspy_g4 import compareFrames


def test_1():
    assert compareFrames('tests/frames_compareFrames/frame_1.png',
                         'tests/frames_compareFrames/frame_1_good.png') == True

    assert compareFrames('tests/frames_compareFrames/frame_1.png',
                         'tests/frames_compareFrames/frame_1_bad.png') == False
