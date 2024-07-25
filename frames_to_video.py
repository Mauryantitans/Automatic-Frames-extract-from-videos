import cv2
import os
from pathlib import Path

# Folder containing the frames
frames_folder = r"C:\Users\moury\OneDrive\Desktop\frames"
output_video = r"C:\Users\moury\OneDrive\Desktop\output_video.mp4"

# Get all frame filenames and sort them numerically
frames = sorted(Path(frames_folder).glob("*.png"), key=lambda x: int(x.stem))

# Check if there are any frames
if not frames:
    print("No frames found in the specified folder.")
    exit()

# Read the first frame to get the width and height
first_frame = cv2.imread(str(frames[0]))
height, width, layers = first_frame.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'mp4v' for .mp4 file
video = cv2.VideoWriter(output_video, fourcc, 30, (width, height))

# Write frames to video
for frame_path in frames:
    frame = cv2.imread(str(frame_path))
    video.write(frame)

# Release the VideoWriter object
video.release()

print(f"Video created successfully at {output_video}")
