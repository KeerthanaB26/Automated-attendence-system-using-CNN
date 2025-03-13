import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

DATASET_PATH = "dataset"
IMG_SIZE = (100, 100)

# Load images for training
datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_generator = datagen.flow_from_directory(
    DATASET_PATH, target_size=IMG_SIZE, batch_size=32, class_mode="categorical", subset="training"
)

val_generator = datagen.flow_from_directory(
    DATASET_PATH, target_size=IMG_SIZE, batch_size=32, class_mode="categorical", subset="validation"
)

# Define CNN model
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=(100, 100, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(len(train_generator.class_indices), activation="softmax")
])

# Compile model
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# Train model
model.fit(train_generator, validation_data=val_generator, epochs=10)

# Save model
model.save("models/trained_model.h5")

print("✅ Model training completed and saved.")
