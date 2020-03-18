#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:04:17 2020

@author: Deney Araujo
"""

"""
Image-colored wordcloud with boundary map
=========================================
A slightly more elaborate version of an image-colored wordcloud
that also takes edges in the image into account.
Recreating an image similar to the parrot example.
"""

import os
from PIL import Image

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_gradient_magnitude

from wordcloud import WordCloud, ImageColorGenerator

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
dirWork = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# load wikipedia text on rainbow
text = open(os.path.join(dirWork, 'boto_rosa.txt')).read()

#Dados de entrada e saida
maskIn = "templates/parrot_mask.jpg"
output = "wordImages/"+"word_"+maskIn.rsplit("/")[1]

# load image. This has been modified in gimp to be brighter and have more saturation.
mask_color = np.array(Image.open(os.path.join(dirWork, maskIn)))
# subsample by factor of 3. Very lossy but for a wordcloud we don't really care.
mask_color = mask_color[::3, ::3]

# create mask  white is "masked out"
maskIn = mask_color.copy()
maskIn[maskIn.sum(axis=2) == 0] = 255

# some finesse: we enforce boundaries between colors so they get less washed out.
# For that we do some edge detection in the image
edges = np.mean([gaussian_gradient_magnitude(mask_color[:, :, i] / 255., 2) for i in range(3)], axis=0)
maskIn[edges > .08] = 255

# create wordcloud. A bit sluggish, you can subsample more strongly for quicker rendering
# relative_scaling=0 means the frequencies in the data are reflected less
# acurately but it makes a better picture
wc = WordCloud(max_words=1000, mask=maskIn, max_font_size=40, random_state=42, relative_scaling=0)#,contour_width=1, contour_color='steelblue')

# generate word cloud
wc.generate(text)
#plt.imshow(wc)

# create coloring from image
image_colors = ImageColorGenerator(mask_color)
wc.recolor(color_func=image_colors)
plt.figure(figsize=(10, 10))
plt.imshow(wc, interpolation="bilinear")
wc.to_file(output)

#plt.figure(figsize=(10, 10))
#plt.title("Original Image")
#plt.imshow(mask_color)
#
#plt.figure(figsize=(10, 10))
#plt.title("Edge map")
#plt.imshow(edges)
#plt.show()