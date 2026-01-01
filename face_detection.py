import cv2
import time

# Load Haar Cascade safely
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

if face_cascade.empty():
    print("❌ Haar Cascade not loaded")
    exit()

# Start webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# System states
system_locked = True
face_start_time = None
UNLOCK_AFTER = 2.5  # seconds face must stay visible

print("🔒 Face Detection System Started")
print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=4,
        minSize=(70, 70)
    )

    current_time = time.time()

    if len(faces) > 0:
        if face_start_time is None:
            face_start_time = current_time

        elapsed = current_time - face_start_time

        if elapsed >= UNLOCK_AFTER:
            system_locked = False
    else:
        face_start_time = None
        system_locked = True

    # Draw face boxes
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # UI Overlay
    if system_locked:
        status_text = "SYSTEM LOCKED - FACE REQUIRED"
        color = (0, 0, 255)  # Red
    else:
        status_text = "SYSTEM UNLOCKED"
        color = (0, 255, 0)  # Green

    cv2.putText(frame, status_text, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

    if face_start_time and system_locked:
        countdown = UNLOCK_AFTER - (current_time - face_start_time)
        cv2.putText(frame, f"Unlocking in {countdown:.1f}s",
                    (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    cv2.imshow("Face Detection & Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()