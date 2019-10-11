import numpy as np
import matplotlib.pyplot as plt
import cv2

lanes = [[-2, -2, -2, -2, 632, 625, 617, 609, 601, 594, 586, 578, 570, 563, 555, 547, 539, 532, 524, 516, 508, 501, 493, 485, 477, 469, 462, 454, 446, 438, 431, 423, 415, 407, 400, 392, 384, 376, 369, 361, 353, 345, 338, 330, 322, 314, 307, 299], [-2, -2, -2, -2, 719, 734, 748, 762, 777, 791, 805, 820, 834, 848, 863, 877, 891, 906, 920, 934, 949, 963, 978, 992, 1006, 1021, 1035, 1049, 1064, 1078, 1092, 1107, 1121, 1135, 1150, 1164, 1178, 1193, 1207, 1221, 1236, 1250, 1265, -2, -2, -2, -2, -2], [-2, -2, -2, -2, -2, 532, 503, 474, 445, 416, 387, 358, 329, 300, 271, 241, 212, 183, 154, 125, 96, 67, 38, 9, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2], [-2, -2, -2, 781, 822, 862, 903, 944, 984, 1025, 1066, 1107, 1147, 1188, 1229, 1269, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2]]
h_samples = [240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710]

arr = []
brr = []

ann_img = np.zeros((720,1280,3)).astype('uint8')

for j in range(len(lanes)):
	prev = -1
	for i in range(len(h_samples)):
		if lanes[j][i] != -2:
			if prev == -1:
				arr.append(lanes[j][i])
				brr.append(720 - h_samples[i])
				ann_img[ 720 - h_samples[i], lanes[j][i]] = 255
			else:
				for k in range(720 - h_samples[i] + 10, 720 - h_samples[i] - 1, -1):
					# print (k, int(((lanes[j][i] - prev)*(k - 720 + h_samples[i] - 10))/(-10) + prev))
					ann_img[ k, int(((lanes[j][i] - prev)*(k - 720 + h_samples[i] - 10))/(-10) + prev)] = 255
			prev = lanes[j][i]

ann_img = np.flipud(ann_img)
cv2.imwrite( "ann_1.png" ,ann_img )

from PIL import Image

img = Image.open('ann_1.png') # image extension *.png,*.jpg
new_width  = 300
new_height = 150
img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save('ann_1.png') # format may what u want ,*.png,*jpg,*.gif

# plt.plot(arr, brr, 'ro')
# plt.axis([0, 1280, 0, 720])
# plt.show()

# import keras_segmentation

#model = keras_segmentation.pretrained.pspnet_50_ADE_20K() # load the pretrained model trained on ADE20k dataset

#model = keras_segmentation.pretrained.pspnet_101_cityscapes() # load the pretrained model trained on Cityscapes dataset

# model = keras_segmentation.pretrained.pspnet_101_voc12() # load the pretrained model trained on Pascal VOC 2012 dataset

# # load any of the 3 pretrained models

# out = model.predict_segmentation(
#     inp="C:/Users/arind/Downloads/clips/0313-1/6040/20.jpg",
#     out_fname="C:/Users/arind/Downloads/clips/0313-1/6040/out.png"
# )

# plt.imshow(out)