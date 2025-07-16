import cv2
import os

KNOWN_FACES_DIR = "known_faces"

def save_face(name):
    if not os.path.exists(KNOWN_FACES_DIR):
        os.makedirs(KNOWN_FACES_DIR)
    
    cap = cv2.VideoCapture(0)
    print(f"Press SPACE to capture your face photo for '{name}'. Press ESC to exit.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        
        cv2.imshow("Capture Face", frame)
        
        key = cv2.waitKey(1)
        if key == 27:  # ESC key
            print("Escape hit, closing...")
            break
        elif key == 32:  # SPACE key
            filepath = os.path.join(KNOWN_FACES_DIR, f"{name}.jpg")
            cv2.imwrite(filepath, frame)
            print(f"Saved face photo to {filepath}")
            cv2.waitKey(500)  # small delay to prevent freeze
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    your_name = input("Enter your name to save your face photo: ").strip()
    save_face(your_name)
