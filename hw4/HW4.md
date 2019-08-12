# 1. Classification of a 2D dataset using ConvnetJS

#### Add a few red dots in previously green areas by clicking the left mouse button. Is the network able to adjust and correctly predict the color now?
#### Add a few green dots in previously red areas by clicking the shift left mouse button. Can the network adapt?
#### Review the network structure in the text box. Can you name the layers and explain what they do?
#### Reduce the number of neurons in the conv layers and see how the network responds. Does it become less accurate?
#### Increase the number of neurons and layers and cause an overfit. Make sure you understand the concept
#### Play with activation functions.. -- relu vs sigmoid vs tanh... Do you see a difference ? Relu is supposed to be faster but less accurate.
# 2. ConvnetJS MNIST demo


#### Name all the layers in parameters in the network, make sure you understand what they do. 
1. Input layer (24x24x1)
2. 24x24x8 convolution layer keeps 2D features but adds a depth of 8. This layer has relu activation.
4. pool layer (reduces the 2D convolution by 2x keeping depth the same)
5. Another layer of convolution, relu, and pool same as before but a filter of 16.
6. a deep layer softmax with 10 classifications
 
#### Experiment with the number and size of filters in each layer. Does it improve the accuracy?
I made size 6 and made the filter 10 for the first layer. It seems to have made things worse because it's over fitting now. So I changed the learning rate.
#### Remove the pooling layers. Does it impact the accuracy?
It looks like it slowed the rate of convergence down. It also over fits a bit. 98% Training, 0.94 validation. 
#### Add one more conv layer. Does it help with accuracy?
It is converging a lot faster.
#### Increase the batch size. What impact does it have?
My guess it that a small increase will help. A large increase will hurt. It has a large learning rate, so it should be able to handle an increase in batch size and improve the over fitting that seems to be occurring.

#### What is the best accuracy you can achieve? Are you over 99%? 99.5%? 
An extra conv2D+ max pooling a simple copy of layer two + a batch size of 32 got me to a validation schore of 1 and sometime 99. 

