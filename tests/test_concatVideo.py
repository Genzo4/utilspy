"""
For tests install:
 - ffmpeg (https://ffmpeg.org)

and add it to PATH
"""

import pytest
from utilspy_g4 import concatVideo
import os
import ffmpeg


def test_1():
    outFile = 'tests/test_concatVideo/out.ts'

    if os.path.exists(outFile):
        os.remove(outFile)

    concatVideo(
        'tests/test_concatVideo/in_1.ts',
        'tests/test_concatVideo/in_2.ts',
        outFile)

    assert os.path.exists(outFile)

    info = ffmpeg.probe(outFile)

    assert info['streams'][0]['codec_name'] == 'h264'
    assert float(info['streams'][0]['duration']) >= 20.0

    os.remove(outFile)