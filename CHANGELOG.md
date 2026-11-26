# Changelog

## v2.0 — Full-frame open gate, true open gate live view, glitch-free playback

**Camera setting: FHD resolution slot** (v1 used UHD).

### Added
- Full-frame open gate 3:2 recording: RAW `3168 × 2120`, active `3152 × 2110`, CinemaDNG 12-bit and 10-bit.
- Standby live view shows the full open gate frame (same framing as recording) on the LCD.
- HDMI shows open gate in standby (no 16:9 black bars).
- Clean live view during recording on LCD and HDMI (no freeze, no glitch).
- In-camera playback without the magenta/red glitch.
- Real sensor frame rates for 24p, 25p and 29.97p (sequential frames, no drops), SSD and SD card.

### Changed
- Pipeline moved from UHD to FHD.
- RAW width set to a multiple of 16 (needed for in-camera playback).
- Display templates switch to 3:2 only in standby and return to stock while recording.

### Known limitations
- HDMI during recording is 16:9.
- In-camera playback is shown inside a 16:9 box (slightly squashed).
- Do not use 23.98p, 48p, 50p or 59.94p. 8-bit not tested.
- `generate_autorun.py` only builds v1 (kept in `legacy-v1/`).

## v1.0 — OG3.2K (UHD slot)

- Open gate 3:2, `3168 × 2112` active / `3184 × 2122` RAW raster.
- Live view 3:2 in standby and recording.
- In-camera playback showed a magenta glitch.
