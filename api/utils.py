from PIL import Image, ImageOps, ImageFilter

def preprocess_image(img):
    # 1. Convert to grayscale
    img = img.convert('L') 
    
    # 2. INVERT: If background is white (255), make it black (0)
    # Most canvases export black lines on transparent/white.
    img = ImageOps.invert(img) 
    
    # 3. Add Padding/Centering: MNIST digits are centered
    # This helps if the user draws right to the edge
    img = ImageOps.expand(img, border=4, fill=0)
    
    # 4. Resize and Blur slightly (removes "jagged" aliasing)
    img = img.resize((28, 28), Image.Resampling.LANCZOS)
    img = img.filter(ImageFilter.GaussianBlur(radius=0.5))
    
    return img