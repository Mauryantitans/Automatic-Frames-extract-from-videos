import os
from pathlib import Path

def rename_frames(frames_folder, prefix, start_number):
    # Get all frame filenames and sort them numerically
    frames = sorted(Path(frames_folder).glob("*.png"), key=lambda x: int(x.stem))

    # Check if there are any frames
    if not frames:
        print("No frames found in the specified folder.")
        return

    # Renaming frames
    for i, frame_path in enumerate(frames, start=start_number):
        new_name = f"{prefix}{i}.png"
        new_path = frame_path.parent / new_name
        frame_path.rename(new_path)
        print(f"Renamed {frame_path.name} to {new_name}")

    print("Renaming completed.")

# Folder containing the frames
frames_folder = r"C:\Users\moury\OneDrive\Desktop\frames"

# Prompt for the prefix and starting number
prefix = input("Enter the prefix for the new filenames (e.g., 'frame'): ")
start_number = int(input("Enter the starting number: "))

rename_frames(frames_folder, prefix, start_number)
