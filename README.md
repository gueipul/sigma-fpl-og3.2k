<div align="center">
  <img src="logo.png" alt="SIGMA fp L OG3.2K Logo" width="220" />

  <h1>SIGMA fp L — OG3.2K</h1>
  <h3>Open Gate 3:2 (3168 × 2112) Research & Runtime Patch</h3>

  <p>
    Independent firmware research and runtime memory modification (<code>AutoRun.txt</code>) for <b>SIGMA fp L Firmware Ver. 3.02</b>.<br />
    Tested on SIGMA fp L Ver. 3.02 only. <b>Memory addresses differ on other firmware versions or the standard SIGMA fp.</b>
  </p>

   <p>
<b>🌐 Website:</b> <a href="https://gueipul.com">gueipul.com</a> &nbsp;|&nbsp;
<b>📥 Download:</b> <a href="https://github.com">AutoRun.txt (Ver. 3.02)</a> &nbsp;|&nbsp;
<b>☕ Support:</b> <a href="https://ko-fi.com/gueipul">ko-fi.com/gueipul</a>
</p>


</div>

---

## 🧭 Development Guide & Disclaimer

> **⚠️ Warning**
> This repository contains experimental firmware research and unofficial runtime memory modifications. Some findings, memory offsets, or configurations may be incomplete, untested, or unstable. Using them may cause failed recordings, data loss, broken settings, or an unresponsive camera.
>
> * **SIGMA fp L Firmware Ver. 3.02 ONLY.** Do not run this on other firmware versions or on the standard SIGMA fp (non-L), as memory addresses differ and will cause the system to hang.
> * This repository **does not** distribute proprietary firmware binaries, source code, or copyrighted assets belonging to SIGMA Corporation.
> * All RAM modifications via `AutoRun.txt` are volatile and revert to stock behavior once the camera is powered off or the battery is removed.
> * **This project is not affiliated with, endorsed, or supported by SIGMA Corporation. Use at your own risk.**

---

## 🌱 Development & Open Collaboration

Everyone is welcome to explore, fork, and build upon these findings in whatever workflow feels most comfortable. You do not need to follow a rigid structure or work toward a single unified codebase to contribute.

In the AI-assisted research era, bridging different experiments and understanding each other's notes has become much easier. Even when independent researchers investigate the same hardware, each path uncovers unique details—such as stabilizing long-duration 12-bit Open Gate recording while still investigating internal playback decoding. Feel free to adapt these memory maps, test new angles, and share your own discoveries openly.

---

## 📊 Current Build Status

Build: **SIGMA fp L Ver. 3.02 — Open Gate 3.2K (`3168 × 2112`)**

| Parameter | Status / Test Result | Notes |
| :--- | :--- | :--- |
| **Aspect Ratio** | ✅ Working (`3:2`) | Utilizes full sensor height (Full-Frame Open Gate) |
| **Output Resolution** | ✅ `3168 × 2112` (Active) | `3184 × 2122` RAW Raster / `3184 × 2126` Sensor Readout |
| **Recording Format** | ✅ CinemaDNG (12-bit, 10-bit, 8-bit) | Stable for continuous, long-duration recording |
| **Frame Rates** | ✅ `23.98p`, `24p`, `25p`, `29.97p` | Preserves native hardware video timing (Modes 155–158) |
| **LCD Live View / REC** | ✅ Working (`3:2` Full-Fit) | Proportional full-height `3:2` display during standby & recording |
| **RAW DNG in DaVinci Resolve** | ✅ **Verified & Clean** | Original CinemaDNG files open normally with accurate color & geometry |
| **In-Camera Playback** | ⚠️ **Not Working Yet (WIP)** | **Audio plays normally, but the camera LCD displays a magenta color glitch during internal playback** |

---

## 🎥 Required Camera Settings (How to Use)

To ensure **Open Gate 3:2 (3.2K)** activates properly and safely, configure your **SIGMA fp L (Ver. 3.02)** as follows:

1. **Verify Firmware Version:** Go to **System → Firmware Update** and confirm your camera is running **Ver. 3.02**.
2. **Mode Switch:** Set the top dial/switch to **CINE** mode.
3. **Resolution:** Must be set to **UHD** (*do not select FHD or DCI 4K, as this patch specifically remaps the UHD pipeline*).
4. **Crop Zoom:** Must be set to **OFF (`x1.00` Full-Frame)** (*crop modes `x1.24` and `x1.53` are not enabled in this build*).
5. **Frame Rate:** Select **23.98p**, **24p**, **25p**, or **29.97p**.
6. **Codec & Storage:** Select **CinemaDNG** (12-bit, 10-bit, or 8-bit) recording to an external SSD or a high-speed SD card.
7. **Reviewing Footage:** **Do not rely on the camera's internal Playback button** to inspect visuals (internal playback decoding currently outputs a magenta color glitch on the LCD, though audio plays back normally). Connect your SSD/SD card to a computer and import the **CinemaDNG (`.dng`)** sequence directly into **DaVinci Resolve**—the recorded RAW files are completely clean and intact.

---

## 🛠️ Installation Guide

You can either download the pre-built `AutoRun.txt` directly from this repository or generate it locally from your own unpacked firmware dump using `generate_autorun.py`.

### Option A: Pre-Built `AutoRun.txt` (For Ver. 3.02 Only)
1. Download [`AutoRun.txt`](https://github.com) from this repository.
2. Copy `AutoRun.txt` to the root directory of your SD card (alongside the `DCIM` folder).
3. Insert the SD card into your **SIGMA fp L (Ver. 3.02)** and power it on (startup execution takes approximately 4–5 seconds).

### Option B: Generate Locally via Python (Recommended for Verification)
`generate_autorun.py` verifies original baseline values against your local unpacked firmware binary (`base 0xC0000000`) before writing `AutoRun.txt`:
```bash
python3 generate_autorun.py --firmware fpl_302_unpacked_c0000000.bin --output AutoRun.txt
```
Copy the generated `AutoRun.txt` to the root directory of your SD card.

---

## 🔬 Technical Summary (Firmware 3.02)

1. **Binned Sensor Modes (`0xC0B92268`–`0xC0B92394`):** Updates sensor readout dimensions for Mode 155 (`29.97p`), Mode 156 (`25p`), Mode 157 (`24p`), and Mode 158 (`23.98p`) to `3184 × 2126` while preserving native hardware video timing to prevent buffer stalls during long 12-bit CinemaDNG takes.
2. **UHD Selector Tables (`0xC0CBE814`–`0xC0CBEAFC`):** Synchronizes Live View Standby, CLV Movie, and UHD recording selectors to their corresponding binned sensor modes across frame rates.
3. **Master Profile & Preview Geometry (`0xC0CABEEC`):** Configures preview scaling (`3.0`), active dimensions (`3168 × 2112`), and RAW raster geometry (`3184 × 2122`) for UHD movie and live view profiles.
4. **LCD Display-Fit (`0xC030AF38`, `0xC030AF84`, `0xC030B074`):** Adjusts ARM aspect-fit instructions so the camera monitor renders the full `3:2` frame without vertical squishing during standby and recording.

---

## 🙏 Credits, Tools, & References

Research and hardware testing conducted by **Gueipul**, inspired by the pioneering work of **bei** (creator of **[fpSup](https://github.com)**):
* **Initial Inspiration & Architecture:** Inspired by **bei (ijigen)**, the inventor of **[fpSup](https://github.com)**, whose `AutoRun` methodology and firmware research for the SIGMA fp series laid the foundation for this exploration.
* **Reverse Engineering & Binary Analysis:** **Ghidra** (NSA Software Reverse Engineering Framework) and **Python** (`struct`, `capstone`).
* **AI Research & Documentation Assistance:** **Claude Code** and **Gemini** for assisting with memory structure mapping, offset verification, script generation, and technical documentation.

---

## ☕ Support Development

If you find this research useful or want to support ongoing development (such as fixing the internal playback decoder and testing additional modes), feel free to support via Ko-fi:

👉 **Support via Ko-fi:** <a href="https://ko-fi.com/gueipul">ko-fi.com/gueipul</a>

---

## 📄 License

* Source code (`generate_autorun.py`) is licensed under the **MIT License**.
* Research notes and documentation are licensed under **CC BY-NC-SA 4.0**.
