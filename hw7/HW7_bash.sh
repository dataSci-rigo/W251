#!/bin/bash
# My first script

apt-get update
apt-get -y install python3-pip cmake libopenblas-dev liblapack-dev libjpeg-dev

pip install numpy
apt-get -y install wget
wget http://dlib.net/files/dlib-19.17.tar.bz2 
tar jxvf dlib-19.17.tar.bz2
cd /dlib-19.17


#sed "${NUM}q;d" dlib/cuda/cudnn_dlibapi.cpp


echo "854c854
<                 forward_algo = forward_best_algo;
---
>                 //forward_algo = forward_best_algo;
" > patch.patch
patch dlib/cuda/cudnn_dlibapi.cpp patch.patch
python setup.py install
pip install face_recognition
