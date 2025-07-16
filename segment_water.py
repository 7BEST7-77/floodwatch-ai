import cv2

def detect_water(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Image not found.")
        return

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_blue = (90, 50, 50)
    upper_blue = (130, 255, 255)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    result = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow("Original", image)
    cv2.imshow("Detected Water", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
