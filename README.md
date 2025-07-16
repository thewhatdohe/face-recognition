This project is a real-time face recognition system that uses a webcam to detect and recognize known faces from a predefined folder of images. When a face is recognized, the system displays the name on the video feed and announces it aloud using text-to-speech. If no known face is detected, it will notify verbally that no faces were recognized.

# Features
Uses DeepFace with Facenet512 model for facial verification.

Supports multiple known faces.

Announces recognized faces by voice.

Runs on a webcam feed with real-time processing every two seconds.

# How to Use
Prepare Known Faces: Create a folder named known_faces in the project directory. Add clear images of people you want the system to recognize. Each image filename should correspond to the person’s name (e.g., JohnDoe.jpg).

# Install Dependencies:
Ensure Python 3.8 or newer is installed. Then install required packages:

pip install opencv-python deepface pyttsx3 numpy tensorflow==2.12.0

# Run the Script:
Execute the main Python script (recognize_and_speak.py). Your webcam will start, and the system will analyze frames every two seconds.

# Usage:
The system displays the webcam feed with recognized names overlaid. When a face is recognized, it will speak the person’s name. If no faces are detected, it will announce accordingly.

# Exit:
Press q to quit the program and release the webcam.

# Notes
Ensure good lighting and clear images in the known_faces folder for optimal recognition accuracy.

The system processes recognition every two seconds to balance performance and responsiveness.
