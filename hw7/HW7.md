# HW7:
## Questions
##### Describe your solution in detail. What neural network did you use? What dataset was it trained on? What accuracy does it achieve?
Face Recognition with dilib "Built using dlib's state-of-the-art face recognition built with deep learning. The model has an accuracy of 99.38% on the Labeled Faces in the Wild benchmark."

##### Does it achieve reasonable accuracy in your empirical tests? Would you use this solution to develop a robust, production-grade system?
It only captures front facing faces(+/-45 degs). It is good enough for certain applications.

##### What framerate does this method achieve on the Jetson? Where is the bottleneck?
It produces images with no delay. It seem faster than opencv.

##### Which is a better quality detector: the OpenCV or yours?
Mine is very quality.
