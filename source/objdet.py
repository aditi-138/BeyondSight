import cv2
import numpy as np
import torch
from ultralytics import YOLO
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from pydub.utils import which
import os

# Ensure ffmpeg is found
AudioSegment.converter = which("ffmpeg")
AudioSegment.ffmpeg = which("ffmpeg")
AudioSegment.ffprobe = which("ffprobe")

# Load YOLOv8 model
model = YOLO("yolov8n.pt")  # Make sure the model is in the same directory

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Width
cap.set(4, 720)   # Height

# Keep track of detected objects
detected_objects = set()

def speak(text):
    """Convert text to speech and play the audio."""
    tts = gTTS(text, lang="en")
    filename = "speech.mp3"
    tts.save(filename)
    audio = AudioSegment.from_file(filename, format="mp3")
    play(audio)
    os.remove(filename)  # Remove the file after playing

while True:
    success, frame = cap.read()
    if not success:
        print("Failed to capture frame")
        break

    # Run YOLO object detection
    results = model(frame)
    
    current_objects = set()
    
    for result in results:
        boxes = result.boxes
        for box in boxes:
            class_id = int(box.cls[0])  # Get class ID
            confidence = float(box.conf[0])  # Get confidence score
            label = model.names[class_id]  # Get class name

            # Get bounding box coordinates
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Draw bounding box and label
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} ({confidence:.2f})", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            
            # Add to current detected objects
            current_objects.add(label)

    # Find new objects that were not previously detected
    new_objects = current_objects - detected_objects

    # Speak only new objects
    if new_objects:
        object_names = ", ".join(new_objects)
        speak(f"I see {object_names}")

    # Update detected objects
    detected_objects = current_objects

    # Show output
    cv2.imshow("Object Detection", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
