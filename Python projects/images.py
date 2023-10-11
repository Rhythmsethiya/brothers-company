import cv2

# Load the image from the current directory (adjust the path if needed)
source = cv2.imread('SourceImage.jpg', cv2.IMREAD_UNCHANGED)

# Display the image in a window titled "title"
cv2.imshow("title", source)

# Wait for a key press indefinitely
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
