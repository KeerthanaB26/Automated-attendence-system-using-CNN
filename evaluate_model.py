import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

DATASET_PATH = "dataset"
MODEL_PATH = "models/trained_model.h5"
IMG_SIZE = (100, 100)
BATCH_SIZE = 32

# Check if model exists
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("Trained model not found! Please run train_model.py first.")

# Check if dataset exists
if not os.path.exists(DATASET_PATH) or not os.listdir(DATASET_PATH):
    raise ValueError("Dataset is empty! Please run create_dataset.py first.")

# Load trained model
model = tf.keras.models.load_model(MODEL_PATH)

# Data Preprocessing
datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

val_generator = datagen.flow_from_directory(
    DATASET_PATH, target_size=IMG_SIZE, batch_size=BATCH_SIZE, class_mode="categorical", subset="validation"
)

# Evaluate model
loss, accuracy = model.evaluate(val_generator)
print(f"\n✅ Model Validation Accuracy: {accuracy * 100:.2f}%")

