# retrozero
restropie on a raspberry pi zero 2 w at full speed 

usefull links : https://files.retropie.org.uk/images/weekly/
use the leatest image file from this link 
# RetroZero – RetroPie Handheld on Pi Zero 2 W

Build a portable, landscape-style retro gaming handheld using a **Raspberry Pi Zero 2 W**, dual analog joysticks, physical buttons, a 3.5″ scalable HDMI display, and a virtual gamepad interface to run RetroPie.

## 🎮 Project Overview

- **Platform:** Raspberry Pi Zero 2 W  
- **Display:** 3.5″ HDMI, 480×320 (auto-scaled)  
- **Controls:**  
  - Dual analog joysticks (via ADS1115, quad-channel 16-bit)  
  - D-pad (Up, Down, Left, Right)  
  - ABXY buttons  
  - Start / Select  
  - Shoulder triggers (L1 / R1)  
- **Power:** ~3000 mAh Li-ion battery (charged via TP4056, boosted to 5V)  
- **Input Handling:** `retro_gamepad_legacy.py` reads buttons & sticks, publishes a Linux virtual gamepad via `uinput`.

---

## ✨ Features

- **Plug & Play Controls** – RetroPie sees your build as a real gamepad.  
- **High-Resolution Input** – Full analog range (scaled for stability).  
- **Auto-Start Service** – Device runs on boot (via systemd).  
- **Portable Power** – Battery-powered for mobile retro gaming.  
- **Clean Architecture** – Ready for 3D-printed or custom case integration.

---

## ⚡ Setup Instructions

### Install Dependencies
```bash
sudo apt update
sudo apt install python3-pip python3-uinput git
```

Install ADS1115 library:
```bash
pip3 install Adafruit-ADS1x15
```

Enable the `uinput` module:
```bash
sudo modprobe uinput
echo "uinput" | sudo tee -a /etc/modules
```

### Clone the Project
```bash
git clone https://github.com/rohanbala-100/retrozero.git
cd retrozero
```

Make script executable:
```bash
chmod +x retro_gamepad_legacy.py
```

### Enable Auto-Start Service
Create the service file:
```bash
sudo nano /etc/systemd/system/retro_gamepad.service
```
Paste:
```ini
[Unit]
Description=Retro Gamepad Service
After=multi-user.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/retrozero/retro_gamepad_legacy.py
WorkingDirectory=/home/pi/retrozero
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

Enable and start service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable retro_gamepad.service
sudo systemctl start retro_gamepad.service
```

---

## 🎛 Virtual Gamepad Mapping

| Physical Input   | Virtual Event          |
|------------------|------------------------|
| D-Pad            | BTN_DPAD_{UP/DOWN/...} |
| ABXY Buttons     | BTN_{A/B/X/Y}          |
| Start / Select   | BTN_START / BTN_SELECT |
| L1 / R1 Triggers | BTN_TL / BTN_TR        |
| Left Joystick    | ABS_X, ABS_Y           |
| Right Joystick   | ABS_RX, ABS_RY         |

Analog values scaled to a **0–32767 range** for stable input behavior with RetroPie.

---

## 🔋 Battery & Runtime

- **Estimated load**: ~800–1000 mA (Pi + display)  
- **Runtime**: ~3–3.5 hours on a 3000 mAh battery  
- Internal TP4056 charger ensures safe recharging.

---

## 🛠 Customization

- Design or 3D-print a **landscape case** with space for screen, controls, battery, and cooling.  
- Add a **battery level gauge** (such as INA219) for power monitoring.  
- Refine deadzone or input scaling in the Python driver as needed.

---

🚀 Built with love for retro gaming!

