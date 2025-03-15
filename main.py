from fastapi import FastAPI
from picamera import PiCamera
from io import BytesIO
import base64

app = FastAPI()

@app.get("/capture")
def capture_image():
    try:
        camera = PiCamera()
        stream = BytesIO()
        camera.capture(stream, format='jpeg')
        stream.seek(0)
        image_base64 = base64.b64encode(stream.read()).decode('utf-8')
        camera.close()
        return {"image": image_base64}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
