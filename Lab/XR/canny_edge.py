import cv2
import numpy as np

# Function to fill the selected region based on left-right averaging


def fill_selection_with_average(image, x1, y1, x2, y2):
    # Create a copy of the image to avoid modifying the original
    filled_image = image.copy()

    # Loop over each row in the selected area
    for y in range(y1, y2):
        # For each column in the selected area, average left and right pixels
        for x in range(x1, x2):
            # Get the left and right pixel values, handle edge cases
            left_pixel = filled_image[y, x1 -
                                      1] if x1 > 0 else filled_image[y, x1]
            right_pixel = filled_image[y, x2] if x2 < filled_image.shape[1] - \
                1 else filled_image[y, x2 - 1]

            # Set the pixel at the selection as the average of the left and right pixels
            filled_image[y, x] = (left_pixel + right_pixel) // 2

    return filled_image


# Load an image (replace 'image.jpg' with your image file)
image = cv2.imread('image.jpg')

# Define the selection coordinates (x1, y1, x2, y2)
# These coordinates define the rectangle to remove and fill
x1, y1 = 100, 50   # Top-left corner
x2, y2 = 200, 150  # Bottom-right corner

# Create a copy of the image and "remove" the selection by setting it to black
image_with_removed_selection = image.copy()
# Removing the selection (setting it to black)
image_with_removed_selection[y1:y2, x1:x2] = 0

# Fill the removed selection with averaged neighboring pixels
filled_image = fill_selection_with_average(
    image_with_removed_selection, x1, y1, x2, y2)

# Display the results
cv2.imshow("Original Image", image)
cv2.imshow("Image with Removed Selection", image_with_removed_selection)
cv2.imshow("Filled Image", filled_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
