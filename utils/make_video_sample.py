import cv2
import config
import os
import sys
"""
    Utility script used to create a video out of 
    test set samples, 'stiching' contiguous frames
    together.
"""

# # get fps as script args
# fps = int(sys.argv[1])
# # max number of data folder to read
# max_folders = int(sys.argv[2])
fps = 10
max_folders = 5

# skip first n folders
skip_first = 0

# get video frames of a day of shooting
# test_set_dir = config.ts_root +'/'+ config.ts_subdirs[0]
test_set_dir = "C:\\Users\\arind\\Downloads\\actual_dataset\\0313-222"
print(test_set_dir)
frames = []
for nfolder, clipfolder in enumerate(sorted(os.listdir(test_set_dir))):
    print(nfolder, clipfolder)
    if clipfolder.startswith('.') or nfolder < skip_first:
        continue

    subfolder = os.path.join(test_set_dir, clipfolder)
    for imgname in range(1, 21):
        frames.append(cv2.imread(os.path.join(subfolder, str(imgname) + ".jpg")))
        # print(os.path.join(subfolder, str(imgname) + ".jpg"))

    # decide when to finish
    if nfolder-skip_first == max_folders:
        break

# all frames are assumed to be of same size
height , width , layers = frames[0].shape
# todo save resized images directly

video = cv2.VideoWriter('video4.mp4', -1, fps, (width, height))
print(height, width, layers)
print("Done!!!")

for frame in frames:
    video.write(frame)

cv2.destroyAllWindows()
video.release()