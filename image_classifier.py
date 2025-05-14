import os
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

def classify_image(img_path):
    try:
        # Check if image exists
        if not os.path.exists(img_path):
            print(f"Error: Image file '{img_path}' not found!")
            return

        print(f"\nProcessing image: {img_path}...")

        # Load and preprocess image
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        # Load model and predict
        print("Loading MobileNetV2 model...")
        model = MobileNetV2(weights="imagenet")
        
        print("Classifying image...")
        predictions = model.predict(img_array)
        decoded_predictions = decode_predictions(predictions, top=3)[0]

        # Display results
        print("\nTop Predictions:")
        for i, (_, label, prob) in enumerate(decoded_predictions):
            print(f"{i+1}. {label}: {prob*100:.2f}%")

    except Exception as e:
        print(f"\nError occurred: {str(e)}")

if __name__ == "__main__":
    # Use 'dog.jpg' from the same folder
    image_file = "dog.jpg"
    classify_image(image_file)
    input("\nPress Enter to exit...")  # Keeps window open