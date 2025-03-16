# autopilotai-pi

## Installation on Raspberry Pi Zero 2

### Flash with latest Raspberry Pi OS image
- Raspberry Pi Zero 2 W
- Raspberry Pi OS Lite (64-bit)

### Upgrade Raspberry Pi OS with latest packages
```sh
sudo apt update
sudo apt upgrade
```

### Install application packages
```sh
sudo apt install python3-fastapi
sudo apt install python3-uvicorn
sudo apt install python3-picamera2
```

### Run the application
```sh
python app/main.py
```

### Test the endpoint
- GET http://localhost:8000/capture