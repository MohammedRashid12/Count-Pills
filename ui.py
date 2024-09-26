import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from camera import capture_image
from image_processing import preprocess_image
from object_detection import detect_and_count_pills

def show_image(image):
    window = tk.Tk()
    window.title("Pill Counter")

    img = Image.fromarray(image)
    img_tk = ImageTk.PhotoImage(image=img)

    label = tk.Label(window, image=img_tk)
    label.image = img_tk
    label.pack()

    window.mainloop()

def main():
    image = capture_image()
    preprocessed_image = preprocess_image(image)
    pill_count = detect_and_count_pills(preprocessed_image)
    print(f"Pills counted: {pill_count}")
    show_image(preprocessed_image)

if __name__ == "__main__":
    main()
