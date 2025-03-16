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
        camera.capture_file("image.jpeg")
        camera.stop()

        with open("image.jpeg", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())

        return {"image": encoded_string}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)