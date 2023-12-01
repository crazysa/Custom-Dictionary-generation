import cv2
import cv2.aruco as aruco
import numpy as np

def create_custom_charuco_dictionary():
    # Define parameters for the custom dictionary
    dictionary_size = 50  # You can adjust this based on your needs
    marker_size = 100  # Adjust the size of the markers as needed

    # Create a custom dictionary
    dictionary = aruco.custom_dictionary(dictionary_size, marker_size)

    # Add markers to the custom dictionary
    for i in range(dictionary_size):
        marker_image = np.zeros((marker_size, marker_size), dtype=np.uint8)
        marker_image.fill(255)  # Set marker background to white

        # You can customize the marker patterns here
        # For example, you can draw shapes or text on the markers
        cv2.putText(marker_image, str(i), (marker_size // 4, marker_size // 2),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, 0, 2, cv2.LINE_AA)

        dictionary[i] = aruco.customMarker(marker_image, i, marker_size, marker_size)

    return dictionary

# Save the custom dictionary to a file (optional)
def save_custom_dictionary(dictionary, filename):
    dictionary.save(filename)

# Example usage:
custom_dictionary = create_custom_charuco_dictionary()

# Save the custom dictionary to a file (optional)
save_custom_dictionary(custom_dictionary, 'custom_charuco_dictionary.yml')

# Use the dictionary for Charuco board generation as needed
