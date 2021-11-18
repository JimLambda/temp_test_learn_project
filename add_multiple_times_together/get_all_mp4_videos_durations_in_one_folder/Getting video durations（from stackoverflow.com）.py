import cv2
cv2video = cv2.VideoCapture( videofilename)
height = cv2video.get(cv2.CAP_PROP_FRAME_HEIGHT)
width  = cv2video.get(cv2.CAP_PROP_FRAME_WIDTH)
print ("Video Dimension: height:{} width:{}".format( height, width))

framecount = cv2video.get(cv2.CAP_PROP_FRAME_COUNT )
frames_per_sec = cv2video.get(cv2.CAP_PROP_FPS)
print("Video duration (sec):", framecount / frames_per_sec)

# equally easy to get this info from images
cv2image = cv2.imread(imagefilename, flags=cv2.IMREAD_COLOR  )
height, width, channel  = cv2image.shape
print ("Image Dimension: height:{} width:{}".format( height, width))