#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:04:17 2020
@author: Deney Araujo
"""

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
dirWork = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(dirWork, 'boto_rosa.txt')).read()

#Dados de entrada e saida
maskIn = "templates/marielle_mask.png"
output = "wordImages/"+"word_"+maskIn.rsplit("/")[1]

# read the mask image
mask = np.array(Image.open(path.join(dirWork, maskIn)))

wc = WordCloud(background_color="white", max_words=1000, mask=mask,
               contour_width=1, contour_color='steelblue')

# generate word cloud
wc.generate(text)
wc.to_file(path.join(dirWork, output))

# show
plt.imshow(wc, interpolation='bilinear')
#plt.axis("off")
#plt.figure()
#plt.imshow(mask, cmap=plt.cm.gray, interpolation='bilinear')
#plt.axis("off")
#plt.show()