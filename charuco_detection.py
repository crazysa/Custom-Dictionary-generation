import cv2
from cv2 import aruco
import numpy as np
import json


with open('custom_8x8_dictionary.json', 'r') as file:
    dictionary_selected_np_array = np.array(json.load(file), dtype=np.uint8)
the_byte_list_to_use = []
aruco_dict = aruco.custom_dictionary(1000, 8)
for value in dictionary_selected_np_array:
    the_byte_list_to_use.append(aruco.Dictionary_getByteListFromBits(value)[0])
aruco_dict.bytesList = np.array(the_byte_list_to_use)
# SUB PIXEL CORNER DETECTION CRITERIA
criteria = (cv2.TERM_CRITERIA_EPS +
            cv2.TERM_CRITERIA_MAX_ITER, 100, 0.00001)

image = cv2.imread("1.jpg")
try:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
except:
    gray_image = image
marker_corners, marker_ids, rejectedImgPoints = cv2.aruco.detectMarkers(
        gray_image, aruco_dict)
board = aruco.CharucoBoard_create(
        5, 5, 1, 0.8, aruco_dict)
if len(marker_corners) > 0:
    for corner in marker_corners:
        cv2.cornerSubPix(gray_image, corner, winSize=(
            3, 3), zeroZone=(-1, -1), criteria=criteria)
    retval, charuco_corners, charuco_ids = cv2.aruco.interpolateCornersCharuco(
        marker_corners, marker_ids, gray_image, board)
    image_shape = gray_image.shape
print(marker_corners, marker_ids)




