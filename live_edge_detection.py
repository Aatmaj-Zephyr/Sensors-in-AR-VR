import cv2

# Function to perform Canny edge detection
def canny_edge_detection(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Perform Canny edge detection
    edges = cv2.Canny(blurred, 150, 500)
    
    return edges

# Capture video from the first webcam
cap = cv2.VideoCapture(r"C:\Users\Administrator\Pictures\Camera Roll\WIN_20240718_17_06_32_Pro.mp4")
# cap = cv2.VideoCapture(0)


ret, frame = cap.read()
# cv2.imshow('Canny Edge Detection', frame)
    
while ret:
    # Read the frame from the webcam
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Perform Canny edge detection
    edges = canny_edge_detection(frame)
    
    # Display the resulting frame
    cv2.imshow('Canny Edge Detection', edges)
    
    # Exit the program if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
