#!/usr/bin/env python3
"""
SIGMA fp L (Firmware 3.02) - Open Gate 3:2 (3.2K: 3168x2112) AutoRun Generator
Author: Gueipul
Inspired by: bei (fpSup)
"""

import argparse
import os
import struct
import sys

BASE_ADDR = 0xC0000000
STEP = 0x3024


def read_u32(data: bytes, addr: int) -> int:
    offset = addr - BASE_ADDR
    if offset < 0 or offset + 4 > len(data):
        raise ValueError(f"Address {hex(addr)} out of firmware bounds.")
    return struct.unpack("<I", data[offset : offset + 4])[0]


def build_patches(data: bytes) -> list[tuple[int, int, int]]:
    patches = []

    # 1. Display-fit LCD 3:2 & Aspect Branch
    display_patches = [
        (0xC030AF38, 0xE3A00003, 0xE3A00002),
        (0xC030AF84, 0xE3A00003, 0xE3A00002),
        (0xC030B074, None, 0xEA000049),
    ]
    for addr, exp_old, new_val in display_patches:
        actual = read_u32(data, addr)
        if exp_old is not None and actual != exp_old:
            raise ValueError(f"Mismatch at {hex(addr)}: expected {hex(exp_old)}, got {hex(actual)}")
        patches.append((addr, actual, new_val))

    # 2. Modify 4 UHD Binned Sensor Modes (155=29.97p, 156=25p, 157=24p, 158=23.98p) -> 3184x2126
    sensor_modes = (0xC0B92268, 0xC0B922CC, 0xC0B92330, 0xC0B92394)
    dim_updates = [
        (0x04, 4784, 3184),
        (0x08, 2700, 2126),
        (0x14, 4784, 3184),
        (0x18, 2700, 2126),
        (0x24, 4784, 3184),
        (0x28, 2700, 2126),
    ]
    for sm_base in sensor_modes:
        for off, exp, newv in dim_updates:
            patches.append((sm_base + off, exp, newv))

    # 3. Route UHD selectors (25p->0x9C, 24p->0x9D, 23.98p->0x9E)
    selector_updates = [
        # LV Standby
        (0xC0CBE814, 159, 0x9C), (0xC0CBE824, 160, 0x9D), (0xC0CBE834, 161, 0x9E),
        # UHD 8-bit
        (0xC0CBEA04, 159, 0x9C), (0xC0CBEA14, 160, 0x9D), (0xC0CBEA24, 161, 0x9E),
        # UHD 10-bit
        (0xC0CBEAD4, 159, 0x9C), (0xC0CBEAE4, 160, 0x9D), (0xC0CBEAF4, 161, 0x9E),
    ]
    for base_sel, old_sm, new_sm in selector_updates:
        patches.append((base_sel + 8, old_sm, new_sm))

    # 4. Master Profile Movie UHD -> 3.2K Open Gate (3168x2112 active, 3184x2122 RAW)
    movie_rows = [
        2736, 2755, 2774, 2793,  # CLV UHD
        1784, 1803, 1822, 1841,  # UHD 8-bit
        2095, 2114, 2133, 2152,  # UHD 10-bit
        2406, 2425, 2444, 2463,  # UHD 12-bit
    ]
    for row in movie_rows:
        w_addr = 0xC0CABEEC + row * 4
        profile_edits = [
            (-34, 0x40400000),  # Scale H (3.0)
            (-33, 0x40400000),  # Scale V (3.0)
            (-30, 0x3FF),       # Prev RWZM H
            (-29, 0x3FF),       # Prev RWZM V
            (-24, 1584),        # Prev Active W (0x630)
            (-23, 1056),        # Prev Active H (0x420)
            (-21, 1600),        # Prev Raster W (0x640)
            (-20, 1066),        # Prev Raster H (0x42A)
            (-19, 3184),        # Sensor W (0xC70)
            (-18, 2126),        # Sensor H (0x84E)
            (-4, 0x3FF),        # RAW RWZM H
            (-3, 0x3FF),        # RAW RWZM V
            (0, 3168),          # RAW Active W (0xC60)
            (1, 2112),          # RAW Active H (0x840)
            (2, 3184),          # RAW Raster 1 W (0xC70)
            (3, 2122),          # RAW Raster 1 H (0x84A)
            (4, 3184),          # RAW Raster 2 W (0xC70)
            (5, 2122),          # RAW Raster 2 H (0x84A)
        ]
        for mult, new_val in profile_edits:
            target = w_addr + (mult * STEP)
            patches.append((target, read_u32(data, target), new_val))

    # 5. Live View Standby UHD (29.97p, 25p, 24p, 23.98p)
    for row in (72, 91, 110, 129):
        w_lv = 0xC0CABEEC + row * 4
        lv_edits = [
            (-34, 0x40400000),
            (-33, 0x40400000),
            (-30, 0x3FF),
            (-29, 0x3FF),
            (-24, 1584),
            (-23, 1056),
            (-21, 1600),
            (-20, 1066),
            (-19, 3184),
            (-18, 2126),
        ]
        for mult, new_val in lv_edits:
            target = w_lv + (mult * STEP)
            patches.append((target, read_u32(data, target), new_val))

    return patches


def main():
    parser = argparse.ArgumentParser(
        description="Generate AutoRun.txt for SIGMA fp L Open Gate 3:2 (3.2K: 3168x2112)."
    )
    parser.add_argument(
        "-f", "--firmware",
        default="fpl_302_unpacked_c0000000.bin",
        help="Path to unpacked SIGMA fp L v3.02 firmware binary (base 0xC0000000)."
    )
    parser.add_argument(
        "-o", "--output",
        default="AutoRun.txt",
        help="Output filename (default: AutoRun.txt)."
    )
    args = parser.parse_args()

    if not os.path.isfile(args.firmware):
        print(f"Error: Firmware file '{args.firmware}' not found.", file=sys.stderr)
        sys.exit(1)

    with open(args.firmware, "rb") as f:
        fw_data = f.read()

    patches = build_patches(fw_data)

    lines = ["display monitor 0 1"]
    for addr, exp_old, new_val in patches:
        actual = read_u32(fw_data, addr)
        if actual != exp_old:
            raise ValueError(
                f"Firmware mismatch at {hex(addr)}: expected {hex(exp_old)}, got {hex(actual)}"
            )
        lines.append(f"mem set 0x{addr:08X} 0x{new_val:08X}")
    lines.append("echo")

    with open(args.output, "wb") as out:
        out.write(("\r\n".join(lines) + "\r\n").encode("ascii"))

    print(f"Success: Generated '{args.output}' with {len(patches)} verified 3.2K patches.")


if __name__ == "__main__":
    main()
