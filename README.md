Object Detection via Viterbi Algorithm
==============

The algorithm applies content-aware image resizing to localise foreground objects via Viterbi algorithm. Instead of cropping objects directly, the algorithm dynamically removes low energy pixels even if belongs to the target object in question. 
## Requirements
- opencv
- numpy


## Implementation detail
Below is an example showing how to run the <code>viterbi.py</code> on sample images located in this repository.

<code>$ python viterbi.py --input-image ../images/animation.jpg --out-height 150 --out-width 200 --output-image ../output/animation.jpg</code>

![Input screenshot](/images/animation.jpg?raw=true)
![Input screenshot](/output/animation.jpg?raw=true)
