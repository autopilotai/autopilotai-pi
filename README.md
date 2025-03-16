# autopilotai-pi

## Installation on Raspberry Pi Zero 2

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

python app/main.py
```