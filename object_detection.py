import cv2

def detect_and_count_pills(processed_image):
    # Find contours
    contours, _ = cv2.findContours(processed_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Count the number of contours (each contour is assumed to be a pill)
    pill_count = len(contours)

    return pill_count
