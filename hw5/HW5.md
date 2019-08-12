# Homework 5:
## Questions:
#### What is TensorFlow? Which company is the leading contributor to TensorFlow?

#### What is TensorRT? How is it different from TensorFlow?
Tensor RT is an NVidia product built on Cuda that optimizes models build using other tools, such as Tensorflow.
In a nutshell it allows pretrained models to be ran efficiently on an IOT.

#### What is ImageNet? How many images does it contain? How many classes?
there are 100k synesets in wordnet and Imaget aims to provide 1k images per synset.
#### Please research and explain the differences between MobileNet and GoogleNet (Inception) architectures.
mobile nets are class of efficient models used on IOT devices. They are based on depthwise separable convolutions.
googlenet is 22 layers deep and but only has 4 million parameters. They booth use depthwise convolutions, but google net was made to win a competition.
#### In your own words, what is a bottleneck?
The bottleneck it the last layer before the output. It is a very dense layer and it takes in all of the last features and generates the classification. It is not a time bottleneck.

####How is a bottleneck different from the concept of layer freezing?
Theoretically they should be the same. Except that one takes more time as it recomputes the features for all of the images. 

#### In this lab, you trained the last layer (all the previous layers retain their already-trained state). Explain how the lab used the previous layers (where did they come from? how were they used in the process?)
the previous layers are already trained the parameters are store in a file. After images are processed once, the output value of the previous layers is cached. However, dropout might still work 

#### How does a low --learning_rate (step 7) value (like 0.005) affect the precision? How much longer does training take?
It doesn't seem to take much longer over all. It seems to take longer to 
#### How about a --learning_rate (step 7) of 1.0? Is the precision still good enough to produce a usable graph?
No, the training validation accuracy moves around a lot. 

#### For step 8, you can use any images you like. Pictures of food, people, or animals work well. You can even use ImageNet images. How accurate was your model? Were you able to train it using a few images, or did you need a lot?


#### Run the script on the CPU (see instructions above) How does the training time compare to the default network training (section 4)? Why?

#### Try the training again, but this time do export ARCHITECTURE="inception_v3" Are CPU and GPU training times different?
Inception takes longer.

#### Given the hints under the notes section, if we trained Inception_v3, what do we need to pass to replace ??? below to the label_image script? Can we also glean the answer from examining TensorBoard?
```python
python -m scripts.label_image --input_layer=Mul --input_height=299 --input_width=299  --graph=tf_files/retrained_graph.pb --image=tf_files/flower_photos/daisy/21652746_cc379e0eea_m.jpg
```
