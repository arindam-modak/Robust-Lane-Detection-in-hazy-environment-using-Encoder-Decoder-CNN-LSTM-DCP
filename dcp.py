import Automold as am
import Helpers as hp
import matplotlib as plt
from PIL import Image
import glob

import math
import numpy as np
import cv2 as cv
import os
import shutil
import sys

L = 256


def get_dark_channel(img, *, size):
    """Get dark channel for an image.

    @param img: The source image.

    @param size: Patch size.

    @return The dark channel of the image.
    """
    minch = np.amin(img, axis=2)
    box = cv.getStructuringElement(cv.MORPH_RECT, (size // 2, size // 2))
    return cv.erode(minch, box)


def get_atmospheric_light(img, *, size, percent):
    """Estimate atmospheric light for an image.

    @param img: the source image.

    @param size: Patch size for calculating the dark channel.

    @param percent: Percentage of brightest pixels in the dark channel
    considered for the estimation.

    @return The estimated atmospheric light.
    """
    m, n, _ = img.shape

    flat_img = img.reshape(m * n, 3)
    flat_dark = get_dark_channel(img, size=size).ravel()
    count = math.ceil(m * n * percent / 100)
    indices = np.argpartition(flat_dark, -count)[:-count]

    return np.amax(np.take(flat_img, indices, axis=0), axis=0)


def get_transmission(img, atmosphere, *, size, omega, radius, epsilon):
    """Estimate transmission map of an image.

    @param img: The source image.

    @param atmosphere: The atmospheric light for the image.

    @param omega: Factor to preserve minor amounts of haze [1].

    @param radius: (default: 40) Radius for the guided filter [2].

    @param epsilon: (default: 0.001) Epsilon for the guided filter [2].

    @return The transmission map for the source image.
    """
    division = np.float64(img) / np.float64(atmosphere)
    raw = (1 - omega * get_dark_channel(division, size=size)).astype(np.float32)
    return cv.ximgproc.guidedFilter(img, raw, radius, epsilon)


def get_scene_radiance(img,
                       *,
                       size=15,
                       omega=0.95,
                       trans_lb=0.1,
                       percent=0.1,
                       radius=40,
                       epsilon=0.001):
    """Get recovered scene radiance for a hazy image.

    @param img: The source image to be dehazed.

    @param omega: (default: 0.95) Factor to preserve minor amounts of haze [1].

    @param trans_lb: (default: 0.1) Lower bound for transmission [1].

    @param size: (default: 15) Patch size for filtering etc [1].

    @param percent: (default: 0.1) Percentage of pixels chosen to compute atmospheric light [1].

    @param radius: (default: 40) Radius for the guided filter [2].

    @param epsilon: (default: 0.001) Epsilon for the guided filter [2].

    @return The final dehazed image.
    """
    atmosphere = get_atmospheric_light(img, size=size, percent=percent)
    trans = get_transmission(img, atmosphere, size=size, omega=omega, radius=radius, epsilon=epsilon)
    clamped = np.clip(trans, trans_lb, omega)[:, :, None]
    img = np.float64(img)
    return np.uint8(((img - atmosphere) / clamped + atmosphere).clip(0, L - 1))



# path='D:/semproject/road_dataset/road_dataset/clips/0313-1/60/*.jpg'
# images= hp.load_images(path)
# bright_images= am.brighten(images[5:8],brightness_coeff=0.7) 
# path2='D:/semproject/road_datasetnew2/'
# i=0
# for img in bright_images:
#     plt.image.imsave(path2 + str(i)+'bname.png', img)
#     i=i+1    

# hp.visualize(images, column=3, fig_size=(20,10))

# path1 = 'C:/Users/arind/Downloads/clips/0313-1/*/'
# path2 = 'C:/Users/arind/Downloads/clips/0313-2/*/'

# path1n = 'C:/Users/arind/Downloads/actual_dataset/0313-1'
# path2n = 'C:/Users/arind/Downloads/actual_dataset/0313-2'



# sub2 = glob.glob(path2)
# for finalpath in sub2:
#     finalpath=finalpath+'*.jpg'
#     images= hp.load_images(finalpath)
#     bright_images= am.brighten(images,brightness_coeff=0.6)
#     x = finalpath.split('\\')
#     os.makedirs(path2n + '/' + x[1])
#     i=1
#     for img in bright_images:
#         dehazed = get_scene_radiance(img)
#         plt.image.imsave(path2n + '/' + x[1] + '/'+ str(i)+'.png', dehazed)
#         i=i+1


# def sortKeyFunc(s):
#     return int(os.path.basename(s)[:-4])

# def load_images(path):
#     image_list=[]
#     images = glob.glob(path)
#     images.sort(key=sortKeyFunc)
#     return images


# path2n = 'C:/Users/arind/Downloads/actual_dataset/0313-2/*/'
# path2m = 'C:/Users/arind/Downloads/actual_dataset/0313-22'
# sub2 = glob.glob(path2n)
# for finalpath in sub2:
#     finalpath=finalpath+'*.png'
#     images = load_images(finalpath)
#     x = finalpath.split('\\')
#     os.makedirs(path2m + '/' + x[1])
#     i=1
#     for img in images:
#         im1 = Image.open(img)  
#         im1 = im1.convert('RGB')
#         im1 = im1.save(path2m + '/' + x[1] + '/'+ str(i)+'.jpg')
#         i=i+1


path1 = 'C:/Users/arind/Downloads/clips/0313-1/*/'
path2 = 'C:/Users/arind/Downloads/clips/0313-2/*/'

path1n = 'C:/Users/arind/Downloads/actual_dataset/0313-1'
path2n = 'C:/Users/arind/Downloads/actual_dataset/0313-22'



sub2 = glob.glob(path2)
for finalpath in sub2:
    finalpath=finalpath+'*.jpg'
    images= hp.load_images(finalpath)
    bright_images= am.brighten(images,brightness_coeff=0.6)
    x = finalpath.split('\\')
    os.makedirs(path2n + '/' + x[1])
    i=1
    for img in bright_images:
        im = Image.fromarray(img)
        im.save(path2n + '/' + x[1] + '/'+ str(i)+'.jpg')
        i=i+1