# The House of Karma - Guest Wi-Fi QR Code

Ready-to-use Wi-Fi QR code generator and printable display signage for **The House of Karma**.

---

## 📶 Network Credentials

| Field | Value |
| :--- | :--- |
| **SSID (Network)** | `KarmaHGuest` |
| **Password** | `KarmaTea2026!` |
| **Security Type** | `WPA` (WPA / WPA2 / WPA3-Personal) |
| **Hidden** | `false` |

---

## 🛠 Raw Wi-Fi QR Payload Format

Standard Wi-Fi QR protocol recognized by iOS and Android:

```text
WIFI:T:WPA;S:KarmaHGuest;P:KarmaTea2026!;;
```

### Protocol Breakdown:
* `WIFI:` - URI scheme that triggers native OS Wi-Fi scanner.
* `T:WPA;` - Authentication type (`WPA`, `WEP`, or `nopass`).
* `S:KarmaHGuest;` - Network SSID.
* `P:KarmaTea2026!;` - Network password.
* `;;` - End of Wi-Fi configuration block.

---

## 📁 Generated Files in this Repository

1. **`karma_wifi_qr.png`**: High-resolution 1024x1024 PNG image. Perfect for wallpapers, digital displays, or sending directly to someone.
2. **`karma_wifi_qr.svg`**: Infinite-resolution vector SVG. Best for physical printing, acrylic table stands, business cards, or laser engraving.
3. **`index.html`**: A formatted printable card template. Open in any browser and press **Print** (or `Ctrl + P`) to print a clean guest sign.
4. **`generate_qr.py`**: Python script to regenerate QR codes if the password or SSID changes in the future.

---

## 🚀 How to Regenerate or Update

To change the Wi-Fi credentials or regenerate files:

```bash
# Run using the local venv:
.\.venv\Scripts\python generate_qr.py
```
