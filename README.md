<div align="center">
  <img src="logo.png" alt="SIGMA fp L OG3.2K Logo" width="220" />

  <h1>SIGMA fp L — OG3.2K v2</h1>
  <h3>Full-Frame Open Gate 3:2 (3152 × 2110) · True Open Gate Live View (LCD + HDMI) · Glitch-Free In-Camera Playback</h3>

  <p>
    Independent firmware research and runtime memory modification (<code>AutoRun.txt</code>) for <b>SIGMA fp L Firmware Ver. 3.02</b>.<br />
    Tested on SIGMA fp L Ver. 3.02 only. <b>Memory addresses differ on other firmware versions or the standard SIGMA fp.</b>
  </p>

   <p>
<b>🌐 Website:</b> <a href="https://gueipul.com">gueipul.com</a> &nbsp;|&nbsp;
<b>📥 Download:</b> <a href="https://github.com/gueipul/sigma-fpl-og3.2k/blob/main/AutoRun.txt">AutoRun.txt (Ver. 3.02)</a> &nbsp;|&nbsp;
<b>☕ Support:</b> <a href="https://ko-fi.com/gueipul">ko-fi.com/gueipul</a>
</p>


</div>

---

## 🆕 What's New in v2

* ✅ **Full-frame open gate:** the whole sensor area (full width × full height, 3:2) is recorded. Nothing is cropped from the sides.
* ✅ **True open gate live view:** standby framing is identical to recording on the LCD (no top/bottom crop, no stretch).
* ✅ **HDMI shows open gate in standby:** no 16:9 black bars on an external monitor.
* ✅ **Live view works during recording:** clean display on LCD and HDMI while recording (no freeze, no glitch).
* ✅ **In-camera playback no longer glitches:** the magenta/red glitch from v1 is gone.
* ✅ **Real 24 / 25 / 29.97 fps, 10-bit and 12-bit:** sequential frames, no drops, to SSD and SD card.
* 🔁 **Camera setting changed:** v2 uses the **FHD** resolution slot (v1 used UHD). See *Required Camera Settings*.

The previous build is kept as release **v1.0**.

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

In the AI-assisted research era, bridging different experiments and understanding each other's notes has become much easier. Even when independent researchers investigate the same hardware, each path uncovers unique details—such as keeping live view running during 12-bit Open Gate recording and fixing internal playback decoding. Feel free to adapt these memory maps, test new angles, and share your own discoveries openly.

---

## 📊 Current Build Status

Build: **SIGMA fp L Ver. 3.02 — Full-Frame Open Gate 3.2K v2 (`3152 × 2110`)**

| Parameter | Status / Test Result | Notes |
| :--- | :--- | :--- |
| **Aspect Ratio** | ✅ Working (`3:2`) | Full-frame open gate: full sensor width and height |
| **Output Resolution** | ✅ `3152 × 2110` (Active) | `3168 × 2120` RAW raster (width is a multiple of 16) |
| **Recording Format** | ✅ CinemaDNG **12-bit & 10-bit** | 8-bit not tested. SD card: 10-bit recommended |
| **Frame Rates** | ✅ `24p`, `25p`, `29.97p` | Real sensor rate, sequential frames, no drops. ⚠️ Do **not** use `23.98p` |
| **LCD Live View (Standby)** | ✅ Full open gate (`3:2`) | Same framing as recording |
| **LCD Live View (During REC)** | ✅ Working (`3:2`, smooth) | No freeze during recording |
| **RAW DNG in DaVinci Resolve** | ✅ **Verified & Clean** | Single sequence, full open gate 3:2, audio in sync |
| **In-Camera Playback** | ✅ **No glitch** | ⚠️ Picture is shown inside a 16:9 box (slightly squashed). 3:2 display is work in progress |
| **HDMI Output (Standby)** | ✅ Open gate, no 16:9 bars | |
| **HDMI Output (During REC)** | ⚠️ 16:9 | Clean (no glitch); 3:2 during REC is work in progress |

---

## 🎥 Required Camera Settings (How to Use)

To ensure **Full-Frame Open Gate 3:2** activates properly and safely, configure your **SIGMA fp L (Ver. 3.02)** as follows:

1. **Verify Firmware Version:** Go to **System → Firmware Update** and confirm your camera is running **Ver. 3.02**.
2. **Mode Switch:** Set the top dial/switch to **CINE** mode.
3. **Resolution:** Must be set to **FHD** (*v2 remaps the FHD pipeline. Do not select UHD or DCI 4K*).
4. **Crop Zoom:** **OFF (`x1.00`)**.
5. **Frame Rate:** Select **24p**, **25p**, or **29.97p**.
   * ⚠️ Do **not** select `23.98p` (wrong sensor readout, zoomed image) or `48p / 50p / 59.94p` (not supported).
6. **Codec & Storage:** **CinemaDNG 12-bit or 10-bit**, recording to an **external SSD** (recommended) or SD card (10-bit recommended).
   * 12-bit data rate: ~244 MB/s (24p), ~254 MB/s (25p), ~305 MB/s (29.97p). 10-bit: ~203 MB/s (24p).
7. **Reviewing Footage:** In-camera playback works without glitches (shown in a 16:9 box for now). For full-quality review, import the **CinemaDNG (`.dng`)** sequence into **DaVinci Resolve**.

---

## 🛠️ Installation Guide

1. Download [`AutoRun.txt`](https://github.com/gueipul/sigma-fpl-og3.2k/blob/main/AutoRun.txt) from this repository.
2. Copy `AutoRun.txt` to the **root directory** of your SD card. The file name must be exactly `AutoRun.txt`.
3. Insert the SD card into your **SIGMA fp L (Ver. 3.02)**, connect your SSD, and power it on (startup execution takes a few seconds).
4. To return to stock: remove or rename `AutoRun.txt` and restart the camera.

> `generate_autorun.py` builds the **v1** file only. It is kept in `legacy-v1/` for reference.

---

## 🔬 Technical Summary (Firmware 3.02, v2)

1. **Sensor Mode 204 (3x3 binning, full sensor area):** FHD 23.98–29.97 picker entries are redirected to mode 204. Its timing (`0xC0B9113C/40`) is set to the stock FHD timings (24.000 / 25.000 / 29.97 fps). A small hook picks the timing from the active profile's engine frame rate.
2. **Recording Descriptor (hook after descriptor build, `0xC0439934`):** sensor window `3184 × 2124` → resizer ratio `1025` → RAW `3168 × 2120` (crop `3152 × 2110`). Preview uses the same stream (preview = RAW), the same way the stock FHD pipeline does. This keeps live view running during recording. A ratio of exactly `1024` (no resize) freezes live view, so `1025` is the highest working size.
3. **Playback (no glitch):** the RAW width is a multiple of 16, and the playback profiles plus the playback-class descriptor use the clip's real row size (`3168 × 2120`, visible `3152 × 2110`, 3:2, unity scale). This follows bei's playback finding for the SIGMA fp.
4. **LCD Display-Fit (`0xC030AF38`, `0xC030AF84`):** aspect-fit set to `3:2` for standby and recording.
5. **Standby live view:** the standby preview uses its full height (`1928 × 1276`, visible `1920 × 1266`, the firmware's own live view profile numbers) instead of a 16:9 center crop. The display templates (`1620 × 911 → 1620 × 1080`, `320 × 180 → 320 × 213`) are switched to 3:2 only in standby and restored to stock when recording starts, so LCD and HDMI show open gate in standby without breaking the recording display.

Method: values were read from the running camera (RAM dumps written to the SSD with the firmware's own `mem save` command) and compared with the stock UHD/FHD pipelines, instead of being guessed.

---

## 🙏 Credits, Tools, & References

Research and hardware testing conducted by **Gueipul**, inspired by the pioneering work of **bei** (creator of **[fpSup](https://github.com)**):
* **Initial Inspiration & Architecture:** Inspired by **bei (ijigen)**, the inventor of **[fpSup](https://github.com)**, whose `AutoRun` methodology and firmware research for the SIGMA fp series laid the foundation for this exploration (including the open gate canvas layout and the playback profile findings).
* **Reverse Engineering & Binary Analysis:** **Ghidra** (NSA Software Reverse Engineering Framework) and **Python** (`struct`, `capstone`).
* **AI Research & Documentation Assistance:** **Claude Code** and **Gemini** for assisting with memory structure mapping, offset verification, script generation, and technical documentation.

---

## ☕ Support Development

If you find this research useful or want to support ongoing development (such as 3:2 in-camera playback display, 3:2 HDMI during recording, and more frame rates), feel free to support via Ko-fi:

👉 **Support via Ko-fi:** <a href="https://ko-fi.com/gueipul">ko-fi.com/gueipul</a>

---

## 📄 License

* Source code (`generate_autorun.py`) is licensed under the **MIT License**.
* Research notes and documentation are licensed under **CC BY-NC-SA 4.0**.
