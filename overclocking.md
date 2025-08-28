# RetroPie on Raspberry Pi Zero 2 W

This project sets up **RetroPie** on a **Raspberry Pi Zero 2 W** with overclocking to improve emulation performance. The Pi Zero 2 W provides a big jump in power compared to the original Zero, making it capable of handling classic consoles and even PlayStation 1.

---

## ⚡ Hardware Overview

* **Board**: Raspberry Pi Zero 2 W
* **CPU**: Quad-core Cortex-A53 @ 1 GHz (default)
* **RAM**: 512 MB
* **Performance boost**:

  * \~40% faster single-core
  * \~500% faster multi-core compared to original Zero

---

## 🎮 Supported Emulation

* ✅ NES, SNES, Game Boy / Color, Genesis – **full speed**
* ✅ PlayStation 1 – most games run well, especially with overclocking
* ⚠️ N64 – mixed results (*Super Mario 64* runs OK, but demanding titles like *GoldenEye 007* struggle)
* ❌ Beyond N64 – not practical

---

## 🔧 Installation

1. Download and flash RetroPie for **Pi 2/3/Zero 2 W** from the [RetroPie download page](https://retropie.org.uk/download/).
2. Insert microSD card and boot the Pi.
3. Configure controllers, Wi-Fi, and basic setup.

---

## 🚀 Overclocking (Optional, for Better Performance)

To enable higher performance:

1. Edit the config file:

   ```bash
   sudo nano /boot/config.txt
   ```
2. Add these lines at the bottom:

   ```ini
   # RetroPie Overclock for Pi Zero 2 W
   arm_freq=1400
   over_voltage=8
   sdram_freq=533
   over_voltage_sdram=1
   ```
3. Save & reboot:

   ```bash
   sudo reboot
   ```

---

## 🧊 Cooling & Stability

* Add a heatsink or small fan if possible.
* If crashes occur, lower `arm_freq` (e.g., 1300) or reduce `over_voltage`.
* Monitor temps with:

  ```bash
  vcgencmd measure_temp
  ```

---

## ⚙️ Emulator Tweaks

* Enable **VSync** or frame limiter if games run too fast.
* Adjust emulator-specific settings for best performance.

---

## ✅ Summary

* Great for **portable retro handheld builds**.
* Excellent for **8-bit and 16-bit consoles**, solid for PS1.
* Overclocking boosts performance significantly.
* Keep an eye on cooling and stability.

---

## 📚 References

* [Bytes N Bits Guide – Overclock Pi Zero 2 W for RetroPie](https://bytesnbits.co.uk/raspberry-pi-zero-2-w-retropie/)
* [RetroPie Official Downloads](https://retropie.org.uk/download/)
* [RetroPie Forums – Pi Zero 2 W Performance](https://retropie.org.uk/forum/)

---
