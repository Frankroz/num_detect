from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
import onnxruntime as ort
import numpy as np
import base64
from io import BytesIO
from PIL import Image
from utils import preprocess_image

app = FastAPI()

try:
    session = ort.InferenceSession("./models/mnist_model.onnx")
    input_name = session.get_inputs()[0].name
except Exception as e:
    print(f"Error loading ONNX model: {e}")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"status": "online", "model": "onnx"}

@app.post("/predict")
async def predict_digit(data: str = Body(embed=True)):
    try:
        # 1. Decode base64 string
        header, encoded = data.split(",", 1)
        image_data = base64.b64decode(encoded)
        
        # 2. Open image and Preprocess
        img = preprocess_image(Image.open(BytesIO(image_data)))
        
        # 3. Convert to Numpy array and normalize
        img_array = np.array(img).astype(np.float32) / 255.0
        img_array = img_array.reshape(1, 28, 28, 1)
        
        # 4. Run Inference with ONNX
        outputs = session.run(None, {input_name: img_array})
        prediction = outputs[0]
        digit = np.argmax(prediction)
        
        return {"prediction": int(digit)}
    
    except Exception as e:
        return {"error": str(e)}

# For local testing
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)