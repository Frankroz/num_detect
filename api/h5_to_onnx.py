import tensorflow as tf
import tf2onnx
import os
import shutil

# 1. Load your model
model = tf.keras.models.load_model("./models/mnist_model.h5")

# 2. Save as a temporary SavedModel (Standard format)
temp_model_path = "temp_saved_model"
model.export(temp_model_path) # or model.save(temp_model_path) in older TF

# 3. Convert from the SavedModel folder to ONNX
# This is much more robust than converting the Keras object directly
os.system(f"python -m tf2onnx.convert --saved-model {temp_model_path} --output model.onnx --opset 13")

# 4. Clean up the temporary folder
if os.path.exists(temp_model_path):
    shutil.rmtree(temp_model_path)

print("✅ Success! model.onnx has been created.")