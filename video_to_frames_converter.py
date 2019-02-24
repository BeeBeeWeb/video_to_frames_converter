import sys
import argparse
import cv2

print(cv2.__version__)

# py video_to_frames_converter.py --pathIn="test/hd.mp4" --pathOut=hd_frames"

def extractImages(pathIn, pathOut):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
      vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))  # set video position in millisec
      success,image = vidcap.read()
      print ('Read a new frame: ', success)
      cv2.imwrite( pathOut + "\\frame%d.jpg" % count, image)     # save frame as JPEG file
      count = count + 1  # this will help to forward video by one second

if __name__=="__main__":
    print("aba")
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video")
    a.add_argument("--pathOut", help="path to images")
    args = a.parse_args()
    print(args)
    extractImages(args.pathIn, args.pathOut)