import cv2
import os

DATASET_PATH = "dataset"
STUDENT_NAME = input("Enter Student Name: ")

STUDENT_DIR = os.path.join(DATASET_PATH, STUDENT_NAME)

if not os.path.exists(STUDENT_DIR):
    os.makedirs(STUDENT_DIR)

cap = cv2.VideoCapture(0)

count = 0
while count < 10:
    ret, frame = cap.read()
    if not ret:
        break

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = frame[y:y + h, x:x + w]
        face_path = os.path.join(STUDENT_DIR, f"{count}.jpg")
        cv2.imwrite(face_path, face)
        count += 1

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Capturing Faces", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print(f"✅ Dataset for {STUDENT_NAME} captured successfully.")
