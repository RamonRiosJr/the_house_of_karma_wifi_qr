"""
The House of Karma - Wi-Fi QR Code Generator
Generates high-resolution PNG and SVG QR codes for the guest Wi-Fi.

Network Details:
- SSID: KarmaHGuest
- Password: KarmaTea2026!
- Security: WPA / WPA2 / WPA3
"""

import os
import sys

def main():
    try:
        import qrcode
        from qrcode.image.svg import SvgPathImage
    except ImportError:
        print("[-] Missing qrcode library. Please install with: pip install \"qrcode[pil]\"")
        sys.exit(1)

    ssid = "KarmaHGuest"
    password = "KarmaTea2026!"
    auth_type = "WPA"
    hidden = False

    # Standard Wi-Fi QR code syntax:
    # Special characters to escape in SSID and Password if present: \, ;, ,, :, "
    # Here neither string contains those characters.
    wifi_payload = f"WIFI:T:{auth_type};S:{ssid};P:{password};;"
    if hidden:
        wifi_payload = f"WIFI:T:{auth_type};S:{ssid};P:{password};H:true;;"

    print(f"[+] Wi-Fi QR Payload: {wifi_payload}")

    # 1. Generate High-Res PNG (1024x1024 approx)
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction allows logos/clarity
        box_size=20,
        border=4,
    )
    qr.add_data(wifi_payload)
    qr.make(fit=True)

    img = qr.make_image(fill_color="#1a1a1a", back_color="#ffffff")
    png_path = "karma_wifi_qr.png"
    img.save(png_path)
    print(f"[+] Saved High-Res PNG: {os.path.abspath(png_path)}")

    # 2. Generate SVG (infinite vector scaling for signage/printing)
    svg_qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=4,
        image_factory=SvgPathImage,
    )
    svg_qr.add_data(wifi_payload)
    svg_qr.make(fit=True)
    svg_img = svg_qr.make_image()
    svg_path = "karma_wifi_qr.svg"
    svg_img.save(svg_path)
    print(f"[+] Saved Vector SVG: {os.path.abspath(svg_path)}")

if __name__ == "__main__":
    main()
