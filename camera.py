import cv2

def capture_image():
    # Open the camera
    cap = cv2.VideoCapture(0)

    # Read a single frame
    ret, frame = cap.read()

    # Release the camera
    cap.release()

    if ret:
        return frame
    else:
        raise Exception("Failed to capture image from camera.")
