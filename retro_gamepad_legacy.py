#!/usr/bin/env python3
# retro_gamepad_legacy.py
# Virtual gamepad driver for RetroZero (Pi Zero 2W + ADS1115 + GPIO buttons)

import time
import Adafruit_ADS1x15  # Legacy ADS1x15 library
import RPi.GPIO as GPIO
import uinput

# --- Button Mapping (GPIO BCM → Virtual Gamepad Button) ---
buttons = {
    17: uinput.BTN_DPAD_UP,
    27: uinput.BTN_DPAD_DOWN,
    22: uinput.BTN_DPAD_LEFT,
    23: uinput.BTN_DPAD_RIGHT,
    24: uinput.BTN_A,
    25: uinput.BTN_B,
    5:  uinput.BTN_X,
    6:  uinput.BTN_Y,
    12: uinput.BTN_START,
    13: uinput.BTN_SELECT,
    19: uinput.BTN_TL,
    26: uinput.BTN_TR
}

# --- GPIO Setup ---
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for pin in buttons:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# --- ADS1115 Joystick Setup ---
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1  # Default gain

# --- Virtual Device Setup ---
device = uinput.Device([
    uinput.ABS_X + (0, 32767, 0, 0),
    uinput.ABS_Y + (0, 32767, 0, 0),
    uinput.ABS_RX + (0, 32767, 0, 0),
    uinput.ABS_RY + (0, 32767, 0, 0),
] + list(buttons.values()))

time.sleep(1)  # Give system time to register device

# Track button states
last_state = {pin: True for pin in buttons}

print("✅ Retro Gamepad started (press Ctrl+C to exit)")

try:
    while True:
        # --- Buttons ---
        for pin, btn in buttons.items():
            pressed = GPIO.input(pin) == GPIO.LOW
            if pressed != last_state[pin]:
                device.emit(btn, int(pressed))
                last_state[pin] = pressed

        # --- Joysticks ---
        x = adc.read_adc(0, gain=GAIN)
        y = adc.read_adc(1, gain=GAIN)
        rx = adc.read_adc(2, gain=GAIN)
        ry = adc.read_adc(3, gain=GAIN)

        # Scale raw ADS1115 (16-bit signed) to 0–32767
        def scale(val):
            return max(0, min(32767, int((val + 32768) / 65535 * 32767)))

        device.emit(uinput.ABS_X, scale(x))
        device.emit(uinput.ABS_Y, scale(y))
        device.emit(uinput.ABS_RX, scale(rx))
        device.emit(uinput.ABS_RY, scale(ry))

        time.sleep(0.01)  # Polling delay (10 ms)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\n👋 Exiting Retro Gamepad...")
