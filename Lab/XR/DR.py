import cv2
import numpy as np

# Function to fill the selected region based on left-right averaging


def fill_selection_with_average(image, x1, y1, x2, y2):
    # Create a copy of the image to avoid modifying the original
    filled_image = image.copy()
    Sum = 0
    # Loop over each row in the selected area
    for y in range(y1, y2):
        # For each column in the selected area, average left and right pixels
        for x in range(x1, x2):
           Sum =cv2.add(Sum, cv2.add( image[x1,x],image[y1,y])[0])[0]



    for y in range(y1, y2):
        # For each column in the selected area, average left and right pixels
        for x in range(x1, x2):
            
            # Set the pixel at the selection as the average of the left and right pixels
            filled_image[x, y] =Sum//((x1-x2)*(y1-y2) )

    return filled_image


# Load an image (replace 'image.jpg' with your image file)
image = cv2.imread(
    '/Users/aatmaj/Downloads/WhatsApp Image 2024-06-12 at 12.00.20 (1).jpeg')

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
    image.copy(), x1, y1, x2, y2)

# Display the results
cv2.imshow("Original Image", image)
cv2.imshow("Image with Removed Selection", image_with_removed_selection)
cv2.imshow("Filled Image", filled_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
