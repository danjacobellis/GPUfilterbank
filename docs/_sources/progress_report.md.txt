# Progress Report

As of Nov 4, we have [implemented octave-spaced dyadic filter banks in CUDA and achieved perfect reconstruction][1]. This is the basic building block for more complicated constant-Q filter banks.

We have also begun some [initial performance comparisons][2], which are promising. GPU filtering for a one-second audio clip using the [highly optimized CuDNN convolution routines][3] takes just milliseconds. The [most widely used python library for audio analysis][4] takes [43 seconds][2] to produce a constant-Q filter bank output for the same audio clip.

[1]:dyadic.ipynb
[2]:timing.ipynb
[3]:https://docs.nvidia.com/deeplearning/cudnn/developer-guide/index.html
[4]:https://librosa.org