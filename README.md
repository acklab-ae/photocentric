# Photocentric... yet another ai bot for social networking.

Author: Andrew Eng

Date: 2020-01-06

Starter code derived from: dingkeyan93/Intrinsic-Image-Popularity


## Summary:
Photocentric is an AI framework that will interact with Instagram.  

To simplify the development across platforms, I created a docker image based on python:3 (currently tested on Phtyon 3.8).  
docker pull andreweng/photocentric:latest

![Sample Image](https://github.com/acklab-ae/photocentric/blob/master/images/example.png)

**mkdir ~/projects**
**cd ~/projects**
**git clone acklab-ae/photocentric**

To get into the environment:

**docker run -it -v $(pwd)/data:/data photocentric:latest /bin/bash**
alternatively, you could just run **sh runme.sh**

Once you get access to the container shell, you can move over to /data

/data contains the following files:

- analyze.ipynb (notebook)
- analyze.py (analyze photos and predict instagram popularity
- images (sample images to analyze)
- model (base model)
- test.py original code from dingkeyan93

To run analyze.py:
  **python analyze.py <image folder to analyze>**



