# Image tools

[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/TomasGadea/image-tools/issues/new)
[![HitCount](http://hits.dwyl.com/TomasGadea/image-tools.svg)](http://hits.dwyl.com/TomasGadea/image-tools)

[![GitHub followers](https://img.shields.io/github/followers/TomasGadea?label=Follow&style=social)](https://github.com/TomasGadea)
[![Linkedin](https://img.shields.io/static/v1?label=LinkedIn&message=Contact&style=social&logo=Linkedin)](https://www.linkedin.com/in/tomas-gadea/)



## Installing

You will need to install
* [**Matplotlib**](https://matplotlib.org/)
* [**Pillow**](https://pypi.org/project/Pillow/)

They can be installed in your machine with the following commands:

_(make sure you have python3 and pip3 updated)_

```
pip3 install matplotlib
pip3 install PIL
```

## Usage

### Resize Image

To resize an image run ```python3 resize.py``` with the following arguments _(if needed)_ on your terminal:

One of these two is compulsory:

* ```--scale```: a real number greater than 0 _(excluded)_

or

* ```--size```: two integers both greater than 0 _(excluded)_

You must add:

* ```--path```: the path of the image to transform

You can add _(optional)_:

* ```--filename```: the name of the generated image storing the result

### Convert image

To change the color encoding of an image run ```python3 convert.py``` with the following arguments _(if needed)_ on your terminal:

* ```--format```: The format you want your image to be encoded in. Could be either **_'RGB'_**, **_'CMYK'_** or **_'BW' (Black and White)_**

You must add:

* ```--path```: the path of the image to transform

You can add _(optional)_:

* ```--filename```: the name of the generated image storing the result
