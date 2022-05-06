import cv2
import os


listOfMP4files = []

allFiles = os.listdir('inputVideos')
for file in allFiles:
    if file.endswith(".mp4"):
        listOfMP4files.append(file)

print(listOfMP4files)
print(len(listOfMP4files))



videoCount = 1

def getFrame(sec,videoCount, frameCount):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("outputImages/video" + str(videoCount) + "_frame" + str(frameCount) +".jpg", image)     # save frame as JPG file
    return hasFrames

for file in listOfMP4files:
    frameCount = 1
    print("We are processing video " + str(file) + " (video " + str(videoCount) + " )")
    vidcap = cv2.VideoCapture('inputVideos\\' + str(file))
    sec = 0
    frameRate = 2
    success = getFrame(sec,videoCount, frameCount)
    while success:
        frameCount = frameCount + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec,videoCount, frameCount)
    videoCount += 1