import os
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
import onnxruntime as ort
import numpy as np
import base64
from io import BytesIO
from PIL import Image
from utils import preprocess_image
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "..", "models", "mnist_model.onnx")

try:
    session = ort.InferenceSession(model_path)
    input_name = session.get_inputs()[0].name
except Exception as e:
    print(f"CRITICAL: Model load failed: {e}")
    # Don't let it crash here, or CORS will never be sent
    session = None

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_URL")],
    allow_credentials=True,
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