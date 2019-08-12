Homework 8:
Part 1: Image Annotation
Questions:

In the time allowed, how many images did you annotate? 300. 
Home many instances of the Millennium Falcon did you annotate? How many TIE Fighters?
Based on this experience, how would you handle the annotation of large image data set? 
It needs to be precise methodical and verified. One minute breaks every ten minutes. Validation is very important, not sure what the best method is.

Think about image augmentation? How would augmentations such as flip, rotation, scale, cropping, and translation effect the annotations?
Annotations such scale, flip, and translation are straight forward because they the same equation can be used on the image and the augmentation. However, for cropping the annotation will need to be cropped appropiately. Unfortunately, rotations might need to be redone by hand if the object is oblong.  

Part 2: Image Augmentation
Questions:

Describe the following augmentations in your own words
Flip- Invert an image so that left becomes right. This is great for profiles.
Rotation- rotate 
Scale- change the number of pixes in an image. This sound trivial, but it matters a lot in image detection.
Crop. 
Translation add white space to any of the three corners of an image. It also works well with scale.
Noise - gaussian, bluring, random dotting all make the image more difficult to read for image detectors


Part 3: Audio Annotation
Take a look at and explore the audio annotation tool CrowdCurio https://github.com/CrowdCurio/audio-annotator)

Questions:

Image annotations require the coordinates of the objects and their classes; in your option, what is needed for an audio annotation?
In audio annotations time and encoding(meaning) are important. Especially encoding consonants, vowels, words, etc.
