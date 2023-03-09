import cv2

# Load the image
img = cv2.imread("face.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# Define the parameters for Canny edge detection
canny_low = 50
canny_high = 150

# Apply Canny edge detection
edges = cv2.Canny(gray, canny_low, canny_high)

# Define the parameters for Hough line detection
rho = 1
theta = cv2.PI/180
threshold = 15
minLineLength = 50
maxLineGap = 20

# Apply Hough line detection
lines = cv2.HoughLinesP(edges, rho, theta, threshold, minLineLength, maxLineGap)

# Draw the lines on the original image
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Display the image with the detected lines
cv2.imshow("Lines Detected", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
