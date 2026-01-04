# Importing all necessary libraries
import cv2
import os
import sys
  
# Read the video from specified path
cam = cv2.VideoCapture(sys.argv[1])
  
try:
      
    # creating a folder named data
    if not os.path.exists('data/input'):
        os.makedirs('data/input')
  
# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')
  

#total video frames
total_frames = int(cam.get(cv2.CAP_PROP_FRAME_COUNT)) - 1 #index starts from 0

#fps of video
fps = cam.get(cv2.CAP_PROP_FPS)

#length of video
length_video = total_frames//fps

#total images needed
num_images = 80

frames_to_retrieve = [ x*total_frames//num_images for x in range(num_images+1)]

print(frames_to_retrieve)

for frame_num in frames_to_retrieve:
    #get a particular frame
    cam.set(cv2.CAP_PROP_POS_FRAMES,frame_num)
    #reading from that frame
    ret, frame = cam.read()
    if ret:
        name = './data/input/frame' + str(frame_num) + '.jpg'
        # writing the extracted images
        cv2.imwrite(name, frame)
    else:
        print("ERROR :" + str(frame_num))
    
# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()