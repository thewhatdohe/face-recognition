import cv2
import os
import numpy as np
import pyttsx3
from deepface import DeepFace
import time

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Folder with known faces
KNOWN_FACES_DIR = "known_faces"
print("Loading known faces...")

known_faces = []
known_names = []

for filename in os.listdir(KNOWN_FACES_DIR):
    if filename.lower().endswith((".jpg", ".png")):
        path = os.path.join(KNOWN_FACES_DIR, filename)
        known_faces.append(path)
        known_names.append(os.path.splitext(filename)[0])
        print(f"[INFO] Loaded: {filename}")

# Initialize webcam
print("Starting webcam... Press 'q' to quit.")
video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("[ERROR] Cannot access webcam")
    exit()

last_check_time = 0
previous_names = set()
no_faces_said = False  # track if "No faces recognized" was said last time

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("[ERROR] Failed to grab frame")
        break

    current_time = time.time()
    if current_time - last_check_time >= 2:
        last_check_time = current_time

        # Save current frame temporarily for DeepFace
        cv2.imwrite("current_frame.jpg", frame)

        recognized_names = []

        for i, face_path in enumerate(known_faces):
            try:
                result = DeepFace.verify(
                    img1_path=face_path,
                    img2_path="current_frame.jpg",
                    enforce_detection=False,
                    model_name="VGG-Face"  # ✅ switched from "Facenet512"
                )
                if result["verified"]:
                    recognized_names.append(known_names[i])
            except Exception as e:
                print(f"[ERROR] DeepFace verification failed for {known_names[i]}: {e}")

        unique_names = set(recognized_names)

        engine.stop()  # Clear previous speech queue

        if unique_names:
            # Find newly recognized names
            new_names = unique_names - previous_names

            if new_names:
                for name in new_names:
                    print(f"[INFO] Recognized: {name}")
                    engine.say(f"Recognized {name}")
                engine.runAndWait()
            no_faces_said = False
        else:
            if not no_faces_said:
                print("[INFO] No faces recognized.")
                engine.say("No faces recognized")
                engine.runAndWait()
                no_faces_said = True

        previous_names = unique_names

    # Display recognized names on the frame
    for i, name in enumerate(recognized_names):
        cv2.putText(frame, name, (50, 50 + i * 40), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()