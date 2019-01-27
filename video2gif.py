# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 19:35:54 2019

@author: anilosmantur
"""

import cv2
import imageio

video_file = 'segregation_demo.mp4'
gif_file = video_file[:-3] + 'gif'

cap = cv2.VideoCapture(video_file)
nFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(video_file, ' - file will be converted.')
with imageio.get_writer(gif_file, duration=0.001, mode='I') as writer:
    print('video to gif started...')
    for i in range(nFrames):
        ret, frame = cap.read()
        if ret and i % 8 == 0:
            print('\r{:6.2f}%({}/{})'.format(100*(i+1)/nFrames, i+1, nFrames), end='')
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (int(width/2), int(height/2)))
            writer.append_data(frame)
        else:
            pass
    print()
print('gif converting finished.')

