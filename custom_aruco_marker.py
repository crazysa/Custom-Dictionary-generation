import cv2
import cv2.aruco as aruco
import numpy as np

# define an empty custom dictionary with
aruco_dict = aruco.custom_dictionary( 2, 3)
# add empty bytesList array to fill with 3 markers later
# aruco_dict.bytesList = np.empty(shape = (3, 2, 4), dtype = np.uint8)

my_dict = aruco.custom_dictionary(2, 7)
bits_H = np.array([[1, 0, 1,1,1,0,1],
                   [1, 1, 1,1,0,1,1],
                   [1, 0, 1,0,1,1,1],
                   [1, 0, 1, 1, 1, 0, 1],
                   [1, 1, 1, 1, 0, 1, 1],
                   [1, 0, 1, 0, 1, 1, 1],
                    [1, 0, 1, 0, 1, 1, 1]
                   ],
                  dtype=np.uint8)
bits_I = np.array([[0, 1, 0,1,1,1,1],
                   [0, 1, 0,1,1,1,1],
                   [0, 1, 0,1,1,1,1],
                   [0, 1, 0, 1, 1, 1, 1],
                   [0, 1, 0, 1, 1, 1, 1],
                   [0, 1, 0, 1, 1, 1, 1],
                    [0, 1, 0, 1, 1, 1, 1]
                   ],
                  dtype=np.uint8)

my_dict.bytesList = np.array([aruco.Dictionary_getByteListFromBits(bits_H)[0],
                              aruco.Dictionary_getByteListFromBits(bits_I)[0]])
# add new marker(s)
# mybits = np.array([[1,1,1,1],[1,0,0,0],[1,1,1,0],[1,0,0,0]], dtype = np.uint8)
# aruco_dict.bytesList[0] = aruco.Dictionary_getByteListFromBits(mybits)
# mybits = np.array([[0,1,1,0],[1,0,0,1],[1,1,1,1],[1,0,0,1],], dtype = np.uint8)
# aruco_dict.bytesList[1] = aruco.Dictionary_getByteListFromBits(mybits)
# mybits = np.array([[0,1,1,1],[1,0,0,0],[1,0,0,0],[1,1,1,1]], dtype = np.uint8)
# aruco_dict.bytesList[2] = aruco.Dictionary_getByteListFromBits(mybits)

for i in range(len(my_dict.bytesList)):
    cv2.imwrite("custom_aruco_test" + str(i) + ".png", aruco.drawMarker(my_dict, i, 128))