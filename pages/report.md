# Team Members

Dan Jacobellis

Utsha Khondkar

# Abstract

In our project, we implement a class of perfect-reconstruction filterbanks for audio analysis. We exploit parallelism across CPU threads for part of our algorithm and use a GPU to solve embarassingly parallel subtasks. We also introduce a novel type of time-frequency tiling which retains the benefits of constant-Q transforms without requiring their cumbersome data structure.

# Background

For audio signal processing problems such as compression, denoising, and various types of pattern recognition, deep learning has taken over. For example, the search interest for "wavelet" has followed the opposite trajectory as "convolutional neural network"

![](img/trends1.svg)

A current trend of audio signal processing research is to apply 2D convolutional neural networks to time-frequency representations of audio. Although great progress was made in the pre-deep learning era on perfect reconstruction filterbanks and wavelet transforms, most of the algorithms and techniques have been abandoned by practitioners of deep learning because no standardized and free implementations were ever widely disseminated. As a result, the standarized set of triangular "Mel" filterbanks dating back nearly 50 years appears to have remained the dominant tool, and have even seen a resurgance despite their [impending obsolescence.][1]

![](img/trends2.svg)

The use of these methods is accumulating a considerable debt. Compared to the most recent iterations of constant-Q filterbanks, these methods for time-frequency analysis lack several desirable properties

* Parameterization/tunability
* Perfect reconstruction
* Meaningful/interpretable phase representation
* Generalization to multiple channels/phased arrays
* Efficient implementation for oversampled representations.

# Filter Banks and Wavelet Transforms

Filter banks are the oldest method of time-frequency analysis, dating back to the first analog spectrum analyzer built by Hermann von Helmholtz in the 19th century.

![](img/helmholtz.svg)

In 1909, mathematician Alfréd Haar discovered that a list of $2^n$ numbers can be represented by recursively taking the sum and difference of adjacent pairs. This property is now commonly referred to 'alias cancellation'

In the 1970s, engineers created the first discrete, invertible filterbanks by expoiting this property. Using what are known as 'conjugate mirror filters'. In the following decade, a massive research effort took place, resulting in a rigorous mathematical understanding of these processes and the development of various "wavelet transforms."

Unfortunately, deep learning has begun to displace these techniques in education, leading to considerable confusion and technical debt.

# GPU convolution

what is CUDA doing?

https://docs.nvidia.com/deeplearning/cudnn/developer-guide/index.html

If you repeat your data and construct 

https://en.wikipedia.org/wiki/Toeplitz_matrix

Then convolution is equivalent to matrix multiply

Not actually doing matrix multiplication, but create a mapping from "virtual matrix" to corresponding array location

(fold in some of the theory from lecture on mat mul)

# Parallel FFT algorithms

not sure what to say about these atm

# Decimation filterbank

filter then downsample

!= dilation + stride (but close)

show toeplitz matrix multiplication with upsampling/downsampling

# Polyphase filterbank

upsample then filter
 
?= transposed convolution with dilation and stride

Another oppurtunity to add CPU parallelism

show mathematically that it's equivalent to splitting filter into L pieces where L is the upsampling factor, and applying filters in parallel

# Oversampled filterbanks

You get exploit more CPU parallelism

# Undersampled filterbanks

we need to do more research

# Demo our program

## Analysis filterbank

## Do stuff

* denoising
* compression
* source separation
* Vocoder

## Synthesis filterbank

[1]:https://asmp-eurasipjournals.springeropen.com/articles/10.1186/s13636-021-00217-4
[2]:https://doi.org/10.1109/TSP.2011.2143711
[3]:https://www.mathworks.com/help/wavelet/ref/tqwt.html