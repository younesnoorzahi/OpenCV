# Here’s a simple example to read and display an image using OpenCV:
import cv2

# Load an image from file
image = cv2.imread('path_to_your_image.jpg')

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load image.")
else:
    # Display the image in a window
    cv2.imshow('Image', image)

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
