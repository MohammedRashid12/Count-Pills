from camera import capture_image
from image_processing import preprocess_image
from object_detection import detect_and_count_pills

def main():
    # Step 1: Capture image from camera
    image = capture_image()

    # Step 2: Preprocess the image
    preprocessed_image = preprocess_image(image)

    # Step 3: Detect and count pills
    pill_count = detect_and_count_pills(preprocessed_image)

    # Step 4: Display results
    print(f"Number of pills detected: {pill_count}")

if __name__ == "__main__":
    main()
