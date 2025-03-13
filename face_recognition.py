import cv2
import numpy as np
import tensorflow as tf
import os
from attendance_database import mark_attendance  # Import the fixed database script

# Load trained model
model = tf.keras.models.load_model("models/trained_model.h5")

# Load class labels (students' names)
CLASS_NAMES = sorted(os.listdir("dataset"))

# Load face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Start camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = frame[y:y + h, x:x + w]
        face_resized = cv2.resize(face, (100, 100))
        face_resized = np.expand_dims(face_resized, axis=0) / 255.0  # Normalize

        # Predict
        prediction = model.predict(face_resized)
        predicted_class = np.argmax(prediction)
        name = CLASS_NAMES[predicted_class]

        # Define the subject manually or dynamically (e.g., "Math", "Physics")
        subject = "Math"

        # Mark attendance **only once per subject per day**
        mark_attendance(name, subject)

        # Draw rectangle and label
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
