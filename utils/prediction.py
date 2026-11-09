import tensorflow as tf
import numpy as np
import json

MODEL_PATH = "model/leaf_guard_model.keras"
CLASS_PATH = "model/class_names.json"

model = tf.keras.models.load_model(MODEL_PATH)

with open(CLASS_PATH, "r") as file:
    class_names = json.load(file)


def predict_disease(image):

    image = image.resize((180, 180))
    image_array = np.array(image)
    image_array = np.expand_dims(image_array, axis=0)

    predictions = model.predict(image_array, verbose=0)[0]

    top_indices = np.argsort(predictions)[-3:][::-1]

    results = []

    for index in top_indices:
        results.append({
            "disease": class_names[index],
            "confidence": float(predictions[index] * 100)
        })

    return results