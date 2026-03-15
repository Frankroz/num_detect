import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps

def test_single_image(image_path):
    # 1. Load the saved model
    model = tf.keras.models.load_model("mnist_model.h5")
    
    # 2. Load and Preprocess the image
    img = Image.open(image_path).convert('L') # Convert to grayscale
    
    # IMPORTANT: MNIST is white-on-black. 
    # If you drew black-on-white, we MUST invert it.
    img = ImageOps.invert(img) 
    
    img = img.resize((28, 28)) # Resize to model input
    
    # 3. Convert to numpy and normalize
    img_array = np.array(img) / 255.0
    img_array = img_array.reshape(1, 28, 28, 1) # Add batch dimension
    
    # 4. Predict
    predictions = model.predict(img_array)
    predicted_digit = np.argmax(predictions)
    confidence = np.max(predictions)
    
    print(f"Predicted Digit: {predicted_digit}")
    print(f"Confidence: {confidence * 100:.2f}%")

if __name__ == "__main__":
    test_single_image("test_digit.png")