import os
imageDirectory = os.listdir('inputImages')
for i in range(1,len(imageDirectory)+1):
	os.system('ffmpeg.exe -framerate 1 -i inputImages/video' + str(i) + '_frame%d.jpg -c:v libx264 -vf \"pad=ceil(iw/2)*2:ceil(ih/2)*2\" -r 30 outputVideos/video' + str(i) + '.mp4')
	print(str(i) + " video(s) created")