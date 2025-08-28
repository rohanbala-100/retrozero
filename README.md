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
Reboot and check:

ls /dev/i2c-1
i2cdetect -y 1
# Should show 0x48 (ADS1115)

2. Install Dependencies
sudo apt update
sudo apt install -y python3-pip python3-uinput git i2c-tools
pip3 install -r requirements.txt


Enable uinput permanently:

echo "uinput" | sudo tee -a /etc/modules
sudo modprobe uinput

3. Clone Repository
git clone https://github.com/rohanbala-100/retrozero.git
cd retrozero
chmod +x retro_gamepad_legacy.py

4. Run Manually (Test)
sudo python3 retro_gamepad_legacy.py

5. Auto-Start with Systemd
sudo cp retro_gamepad.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable retro_gamepad.service
sudo systemctl start retro_gamepad.service


Check status:

systemctl status retro_gamepad.service
journalctl -u retro_gamepad.service -n 30 --no-pager

🎮 Controls Mapping
Physical Input	Virtual Event
D-Pad	BTN_DPAD_{UP/DOWN/...}
ABXY Buttons	BTN_{A/B/X/Y}
Start / Select	BTN_START / BTN_SELECT
L1 / R1 Triggers	BTN_TL / BTN_TR
Left Joystick	ABS_X, ABS_Y
Right Joystick	ABS_RX, ABS_RY

Analog inputs are scaled 0 → 32767 for RetroPie compatibility.

🔋 Battery & Runtime

Power use: ~800–1000 mA (Pi + Display)

Runtime: ~3–3.5 hours on 3000 mAh Li-ion

Safe charging: TP4056 + boost converter

🛠 Troubleshooting

Check logs:

journalctl -u retro_gamepad.service


Verify uinput:

lsmod | grep uinput


Test joystick:

jstest /dev/input/js0


🚀 Built with ❤️ for Retro Gaming


---

Do you want me to also make this README include a **pinout diagram (ASCII or Markdown table)** so users can see exactly which GPIO pins connect to which buttons?
