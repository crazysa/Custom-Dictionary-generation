from itertools import product
import random
import numpy as np
import cv2.aruco as aruco
import cv2
import json

def hamming_distance(str1, str2):

    if len(str1) != len(str2):
        raise ValueError("Unequal length")

    distance = sum(c1 != c2 for c1, c2 in zip(str1, str2))
    return distance


# Define the values to permute
values = [0, 1]

# Generate all permutations of the list of size 8 with values 0 and 1
all_permutations = list(product(values, repeat=8))

# Print the permutations
# for perm in all_permutations:
#     print(perm)
selected_code = set()
selected_np_array = []
for i in range(20):
    random_selection  = random.choices(all_permutations, k=8)
    # print(random_selection)
    result_string = ""
    for row in random_selection:
        for value in row:
            result_string += str(value)

    if result_string not in selected_code:
        high_hamming_distance = True
        for value in selected_code:
            if hamming_distance(value,result_string) < 19:
                high_hamming_distance=False
                break
        if high_hamming_distance:
            selected_code.add(result_string)
            selected_np_array.append(random_selection)
changed_selected_np_array = np.array(selected_np_array,dtype=np.uint8)
print(selected_code)
print(changed_selected_np_array)
# print(type(changed_selected_np_array))

my_dict = aruco.custom_dictionary(20, 8)

the_byte_list_to_use = []
for value in changed_selected_np_array:
    the_byte_list_to_use.append(aruco.Dictionary_getByteListFromBits(value)[0])

print("Value before writing to json", selected_np_array)
with open('custom_8x8_dictionary.json', 'w') as file:
    json.dump(selected_np_array, file)

with open('custom_8x8_dictionary.json', 'r') as file:
    print(json.load(file))

my_dict.bytesList = np.array(the_byte_list_to_use)

for i in range(len(my_dict.bytesList)):
    cv2.imwrite("custom_aruco_test" + str(i) + ".png", aruco.drawMarker(my_dict, i, 256))

# charuco_board = cv2.aruco.CharucoBoard_create(
#         5  , 5, 1, 0.9, my_dict)

board = aruco.CharucoBoard_create(
        5, 5, 1, 1*0.8, my_dict)
imboard = board.draw((1020, 1980))
cv2.imwrite("charuco_value.png", imboard)