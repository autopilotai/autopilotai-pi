# autopilotai-pi

## Installation on Raspberry Pi Zero 2

### Flash with latest Raspberry Pi OS image
- Raspberry Pi Zero 2 W
- Raspberry Pi OS Lite (64-bit)

### Upgrade Raspberry Pi OS with latest packages
```sh
sudo apt update
sudo apt upgrade

sudo apt install git
```
### Install Tailscale
https://tailscale.com/kb/1174/install-debian-bookworm

#### Setup Tailscale as a service
```sh
sudo systemctl enable tailscaled
sudo systemctl start tailscaled
```

### Install application packages
```sh
git clone https://github.com/autopilotai/autopilotai-pi.git

sudo apt install python3-fastapi python3-uvicorn python3-picamera2
```

### Run the application
```sh
python app/main.py
```

### Optional: Setup to run as a service
```sh
```

### Test the endpoint
- GET http://localhost:8000/capture