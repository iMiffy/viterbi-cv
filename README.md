Object Detection via Viterbi Algorithm
==============

The algorithm applies content-aware image resizing to localise foreground objects via Viterbi algorithm. Instead of cropping objects directly, the algorithm dynamically removes low energy pixels even if belongs to the target object in question. 

## Intuition
For a given image, adjacent pixels with significant value difference imply a potential edge exists between them while no-visible content change among pixels could be inferred based on slight value difference. If pixels with huge difference are removed, they are likely to be an edge, thus harming the content in the image. Therefore, this algorithm serves to identify a path _p_ with minimum differences for a given image I∈R^(m×n) and remove the pixels in _p_ from the image iteratively, where pixels in path _p_ are supposed to be pixels with slight differences. 

## Requirements
- opencv
- numpy


## Implementation detail
Below is an example showing how to run the <code>viterbi.py</code> on sample images located in this repository.

<code>$ python viterbi.py --input-image ../images/animation.jpg --out-height 150 --out-width 200 --output-image ../output/animation.jpg</code>

![Input screenshot](/images/animation.jpg?raw=true)
![Input screenshot](/output/animation.jpg?raw=true)
