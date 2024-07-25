import cv2

# Video file path
video_path = r"C:\Users\moury\Downloads\RecordIt-1719666814.mp4"

# Create a VideoCapture object
vidcap = cv2.VideoCapture(video_path)

# Check if video opened successfully
if not vidcap.isOpened():
    print("Error: Could not open video.")
else:
    count = 0
    while True:
        success, image = vidcap.read()
        if not success:
            break
        # Write the frame to the specified path
        cv2.imwrite(r"C:\Users\moury\OneDrive\Desktop\frames\%d.png" % count, image)
        count += 1

    vidcap.release()
    print(f"Extraction completed. {count} frames extracted.")
