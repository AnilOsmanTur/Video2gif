#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 15:07:56 2019

@author: anilosmantur
"""

import os
import imageio


gif_file = 'earthquake.gif'

nFrames = len(os.listdir("images"))

print(gif_file, ' - file will be created.')
with imageio.get_writer(gif_file, duration=1, mode='I', subrectangles=True) as writer:
    print('started...')
    for i in range(nFrames):
        print('\r{:5.2f}% [{}/{}]'.format(i/nFrames*100, int(i), nFrames), end='')
        image = imageio.imread('images/{}.png'.format(i+1))
        writer.append_data(image)
    print('\nDone.')
print('gif converting finished.')