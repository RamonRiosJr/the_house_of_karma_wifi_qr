"""
The House of Karma - Wi-Fi QR Code Generator
Generates high-resolution standard and branded QR codes for the guest Wi-Fi.

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
        from PIL import Image, ImageDraw
    except ImportError:
        print("[-] Missing required libraries. Run: pip install \"qrcode[pil]\" pillow")
        sys.exit(1)

    ssid = "KarmaHGuest"
    password = "KarmaTea2026!"
    auth_type = "WPA"

    # Standard Wi-Fi URI format
    wifi_payload = f"WIFI:T:{auth_type};S:{ssid};P:{password};;"
    print(f"[+] Wi-Fi QR Payload: {wifi_payload}")

    # 1. Standard High-Res PNG
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=4,
    )
    qr.add_data(wifi_payload)
    qr.make(fit=True)

    img = qr.make_image(fill_color="#111827", back_color="#ffffff")
    png_path = "karma_wifi_qr.png"
    img.save(png_path)
    print(f"[+] Saved Standard PNG: {os.path.abspath(png_path)}")

    # 2. Vector SVG
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

    # 3. Branded QR with Center Logo (if logo exists)
    logo_file = "karma_logo.png"
    if not os.path.exists(logo_file) and os.path.exists("The house of Karme Logos 10-25-23 (4).avif"):
        try:
            im = Image.open("The house of Karme Logos 10-25-23 (4).avif")
            im.save("karma_logo.png", "PNG")
            logo_file = "karma_logo.png"
        except Exception as e:
            print(f"[!] Warning converting AVIF: {e}")

    if os.path.exists(logo_file):
        qr_branded = qr.make_image(fill_color="#111827", back_color="#ffffff").convert("RGBA")
        logo = Image.open(logo_file).convert("RGBA")

        qr_w, qr_h = qr_branded.size
        logo_size = int(qr_w * 0.24)
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

        # Circular mask for logo
        mask = Image.new("L", (logo_size, logo_size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, logo_size, logo_size), fill=255)

        # White protective halo ring behind center logo to guarantee scan reliability
        pad = 8
        bg_size = logo_size + pad * 2
        bg_circle = Image.new("RGBA", (bg_size, bg_size), (255, 255, 255, 0))
        bg_draw = ImageDraw.Draw(bg_circle)
        bg_draw.ellipse((0, 0, bg_size, bg_size), fill=(255, 255, 255, 255))

        pos_x = (qr_w - bg_size) // 2
        pos_y = (qr_h - bg_size) // 2
        qr_branded.paste(bg_circle, (pos_x, pos_y), bg_circle)

        logo_pos_x = (qr_w - logo_size) // 2
        logo_pos_y = (qr_h - logo_size) // 2
        qr_branded.paste(logo, (logo_pos_x, logo_pos_y), mask)

        branded_path = "karma_wifi_qr_branded.png"
        qr_branded.save(branded_path)
        print(f"[+] Saved Branded QR with Center Logo: {os.path.abspath(branded_path)}")

if __name__ == "__main__":
    main()
