import time
from fastapi import FastAPI
from picamera2 import Picamera2
import uvicorn
from io import BytesIO
import base64

camera = Picamera2()
config = camera.create_still_configuration()
camera.configure(config)

app = FastAPI()

@app.get("/capture")
def capture_image():
    try:
        camera.start()
        time.sleep(2)
        # np_array = camera.capture_array()
        camera.capture_file("image.jpg")
        time.sleep(2)
        camera.stop()

        # # Convert the numpy array to bytes
        # image_bytes = np_array.tobytes()
        # # Encode the bytes to base64
        # image_base64 = base64.b64encode(image_bytes).decode('utf-8')

        return {"image": "image_base64"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)