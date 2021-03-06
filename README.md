![Language](https://img.shields.io/badge/English-brigthgreen)

# utilspy

![PyPI](https://img.shields.io/pypi/v/utilspy-g4)
![PyPI - License](https://img.shields.io/pypi/l/utilspy-g4)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/utilspy-g4)


Small utils for python

***

## Installation

### Package Installation from PyPi

```bash
$ pip install utilspy-g4
```

### Package Installation from Source Code

The source code is available on [GitHub](https://github.com/Genzo4/utilspy).  
Download and install the package:

```bash
$ git clone https://github.com/Genzo4/utilspy
$ cd utilspy
$ pip install -r requirements.txt
$ pip install .
```

***

## Utils

- ### addExt
Add extension to path.

Support Windows and Linux paths.

```python
from utilspy_g4 import addExt

path = '/test/test.png'
ext = '2'
newPath = addExt(path, ext)     # newPath = '/test/test.2.png'
```

- ### compareFrames
Compare 2 frames.

```python
from utilspy_g4 import compareFrames

is_equal = compareFrames('path_to_frame_1.png', 'path_to_frame_2.png')
```

- ### delExt
Del extension from path.

Support Windows and Linux paths.

```python
from utilspy_g4 import delExt

path = '/test/test.png'
newPath = delExt(path)     # newPath = '/test/test'

path = '/test/test.2.png'
newPath = delExt(path)     # newPath = '/test/test.2'

path = '/test/test.2.png'
newPath = delExt(path, 2)     # newPath = '/test/test'
```

- ### templatedRemoveFiles
Remove files by template

```python
from utilspy_g4 import templatedRemoveFiles

templatedRemoveFiles('/tmp/test_*.txt')
```

- ### getExt
Get extension from path.

Support Windows and Linux paths.

```python
from utilspy_g4 import getExt

path = '/test/test.png'
ext = getExt(path)     # ext = 'png'

path = '/test/test.jpeg.png'
ext = getExt(path)     # ext = 'png'

path = '/test/test.jpeg.png'
ext = getExt(path, 2)     # ext = 'jpeg'

path = '/test/test.jpeg.png'
ext = getExt(path, 0)     # ext = ''
```

- ### concatVideo
Concat 2 video files with same codecs and params.
It use ffmpeg. Install [ffmpeg](https://ffmpeg.org) and add it to PATH.

```python
from utilspy_g4 import concatVideo

concatVideo('path_to_video_1.ts', 'path_to_video_2.ts', 'path_to_output_video.ts')
```

***

[Changelog](https://github.com/Genzo4/utilspy/blob/main/CHANGELOG.md)

***

![Language](https://img.shields.io/badge/??????????????-brigthgreen)

# utilspy

![PyPI](https://img.shields.io/pypi/v/utilspy-g4)
![PyPI - License](https://img.shields.io/pypi/l/utilspy-g4)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/utilspy-g4)

?????????????????? ???????????????? ?????? Python.

***

## ??????????????????

### ?????????????????? ???????????? ?? PyPi

```bash
$ pip install utilspy-g4
```

### ?????????????????? ???????????? ???? ?????????????????? ????????

???????????????? ?????? ?????????????????????? ???? [GitHub](https://github.com/Genzo4/utilspy).  
???????????????? ?????? ?? ???????????????????? ??????????:

```bash
$ git clone https://github.com/Genzo4/utilspy
$ cd utilspy
$ pip install -r requirements.txt
$ pip install .
```

***

## ??????????????

- ### addExt
?????????????????? ???????????????????????????? ???????????????????? ?????????? ?????????? ?????? ?????????????????? ??????????????????????.

???????????????????????? ?????? Windows ????????, ?????? ?? Linux.

```python
from utilspy_g4 import addExt

path = '/test/test.png'
ext = '2'
newPath = addExt(path, ext)     # newPath = '/test/test.2.png'
```

- ### compareFrames
?????????????????? ???????? ???????????? (??????????????????????).

```python
from utilspy_g4 import compareFrames

is_equal = compareFrames('path_to_frame_1.png', 'path_to_frame_2.png')
```

- ### delExt
?????????????? ???????? ?????? ?????????????????? ???????????????????? ??????????

???????????????????????? ?????? Windows ????????, ?????? ?? Linux.

```python
from utilspy_g4 import delExt

path = '/test/test.png'
newPath = delExt(path)     # newPath = '/test/test'

path = '/test/test.2.png'
newPath = delExt(path)     # newPath = '/test/test.2'

path = '/test/test.2.png'
newPath = delExt(path, 2)     # newPath = '/test/test'
```

- ### templatedRemoveFiles
???????????????? ???????????? ???? ??????????????

```python
from utilspy_g4 import templatedRemoveFiles

templatedRemoveFiles('/tmp/test_*.txt')
```

- ### getExt
???????????????????? ???????????????????? ??????????.
?????????? ?????????????? ?????????? ???? ?????????? ???????????????????? ???????? ??????????????.

???????????????????????? ?????? Windows ????????, ?????? ?? Linux.

```python
from utilspy_g4 import getExt

path = '/test/test.png'
ext = getExt(path)     # ext = 'png'

path = '/test/test.jpeg.png'
ext = getExt(path)     # ext = 'png'

path = '/test/test.jpeg.png'
ext = getExt(path, 2)     # ext = 'jpeg'

path = '/test/test.jpeg.png'
ext = getExt(path, 0)     # ext = ''
```

- ### concatVideo
?????????????????????? ???????? ?????????? ???????????? ?? ?????????????????????? ???????????????? ?? ?????????????????????? ?? ???????? ????????.
???????????????????????? ffmpeg. ?????? ?????????????????????????? ???????????????????? [ffmpeg](https://ffmpeg.org) 
?? ?????????????????? ?????? ?? PATH.

```python
from utilspy_g4 import concatVideo

concatVideo('path_to_video_1.ts', 'path_to_video_2.ts', 'path_to_output_video.ts')
```

***

[Changelog](https://github.com/Genzo4/utilspy/blob/main/CHANGELOG.md)
