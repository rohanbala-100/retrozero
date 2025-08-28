
# 🎮 RetroZero – Raspberry Pi Zero 2W RetroPie Handheld

**RetroZero** turns a **Raspberry Pi Zero 2 W** into a **portable retro gaming handheld** with dual analog joysticks, arcade-style buttons, and a 3.5″ HDMI display.  
All controls are read through GPIO (buttons) and an ADS1115 ADC (joysticks), then exposed to RetroPie as a **virtual gamepad** via `uinput`.

---

## 📦 Hardware

- Raspberry Pi Zero 2 W  
- 3.5″ HDMI Display (480×320, scalable)  
- Dual analog joysticks (ADS1115, 16-bit, I²C)  
- D-Pad (Up, Down, Left, Right)  
- ABXY buttons  
- Start + Select  
- L1 / R1 shoulder triggers  
- 3000 mAh Li-ion battery (with TP4056 charger + boost module)  

---

## ⚡ Software Setup

### 1. Enable I²C
```bash
sudo raspi-config
# Interfacing Options → I2C → Enable
````

Reboot and check:

```bash
ls /dev/i2c-1
i2cdetect -y 1
# Should show 0x48 (ADS1115)
```

### 2. Install Dependencies

```bash
sudo apt update
sudo apt install -y python3-pip python3-uinput git i2c-tools
pip3 install -r requirements.txt
```

Enable `uinput` permanently:

```bash
echo "uinput" | sudo tee -a /etc/modules
sudo modprobe uinput
```

### 3. Clone Repository

```bash
git clone https://github.com/rohanbala-100/retrozero.git
cd retrozero
chmod +x retro_gamepad_legacy.py
```

### 4. Run Manually (Test)

```bash
sudo python3 retro_gamepad_legacy.py
```

### 5. Auto-Start with Systemd

```bash
sudo cp retro_gamepad.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable retro_gamepad.service
sudo systemctl start retro_gamepad.service
```

Check status:

```bash
systemctl status retro_gamepad.service
journalctl -u retro_gamepad.service -n 30 --no-pager
```

---

## 🎮 Controls Mapping

| Physical Input   | Virtual Event    | Pi GPIO (BCM) |
| ---------------- | ---------------- | ------------- |
| D-Pad Up         | BTN\_DPAD\_UP    | GPIO17        |
| D-Pad Down       | BTN\_DPAD\_DOWN  | GPIO27        |
| D-Pad Left       | BTN\_DPAD\_LEFT  | GPIO22        |
| D-Pad Right      | BTN\_DPAD\_RIGHT | GPIO23        |
| Button A         | BTN\_A           | GPIO24        |
| Button B         | BTN\_B           | GPIO25        |
| Button X         | BTN\_X           | GPIO5         |
| Button Y         | BTN\_Y           | GPIO6         |
| Start            | BTN\_START       | GPIO12        |
| Select           | BTN\_SELECT      | GPIO13        |
| L1 Trigger       | BTN\_TL          | GPIO19        |
| R1 Trigger       | BTN\_TR          | GPIO26        |
| Left Joystick X  | ABS\_X           | ADS1115 A0    |
| Left Joystick Y  | ABS\_Y           | ADS1115 A1    |
| Right Joystick X | ABS\_RX          | ADS1115 A2    |
| Right Joystick Y | ABS\_RY          | ADS1115 A3    |

👉 Analog inputs are scaled **0 → 32767** for RetroPie compatibility.

---

## 🔋 Battery & Runtime

* Power use: \~800–1000 mA (Pi + Display)
* Runtime: \~3–3.5 hours on 3000 mAh Li-ion
* Safe charging: TP4056 + boost converter

---

## 🛠 Troubleshooting

Check logs:

```bash
journalctl -u retro_gamepad.service
```

Verify `uinput`:

```bash
lsmod | grep uinput
```

Test joystick:

```bash
jstest /dev/input/js0
```

---

🚀 Built with ❤️ for Retro Gaming

```

---

✅ This is clean, GitHub-ready, and has a **GPIO pinout mapping table**.  

Do you also want me to generate a **PNG wiring diagram** for the repo (Pi Zero 2W pins + ADS1115 + buttons/joysticks) so users can see it visually?
```
