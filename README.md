# The Karma House - Wi-Fi & Website Signage System

High-contrast, brand-integrated, print-ready signage and interactive display cards for **The Karma House Kava & Community Lounge**.

---

## 📶 Network Credentials & Display Key

| Field | Visible Plaque Format | Value |
| :--- | :--- | :--- |
| **Network (SSID)** | `WIFI:` | **`KarmaHGuest`** |
| **Password (Key)** | `PASS:` | **`KarmaTea2026!`** |
| **Security** | WPA2 / WPA3-Personal | Case-sensitive |
| **Official Website** | `WEBSITE:` | **`TheKarmaHouse.org`** |

---

## 🚀 Live Display & Options

The application in `index.html` is completely self-contained (all vector QR codes and branded assets are embedded directly as base64 data):

1. **Option Switcher**:
   * **📶 Wi-Fi**: Displays the prominent Wi-Fi QR code with `KarmaHGuest` and `KarmaTea2026!` credentials.
   * **🌐 TheKarmaHouse.org**: Displays the dedicated website QR code for quick community, events, and menu access.

2. **Common Print & Frame Sizes**:
   * **4" × 6"**: Standard Dollar Tree / photo frame size. Outputs with a dashed scissor cut outline on standard 8.5" × 11" paper.
   * **5" × 7"**: Tabletop portrait frame size with cut outline.
   * **8.5" × 11"**: Full-sheet sign for counter easel or wall display.

---

## 🖨️ Printing Instructions

1. Open `index.html` in any browser.
2. Select your desired sign: **Wi-Fi** or **TheKarmaHouse.org**.
3. Select your frame size: **4" × 6"**, **5" × 7"**, or **8.5" × 11"**.
4. Click **Print** (or press `Ctrl + P`).
5. In print settings, ensure paper is set to **Letter** and scale is **100% (Actual size)**.
6. Cut along the dashed border with scissors and slide directly into your frame!

---

## ☁️ Cloudflare Pages Deployment

To host this live on Cloudflare Pages connected to your GitHub repo:

1. In the **Cloudflare Dashboard**, navigate to **Compute (Workers & Pages)** > **Pages**.
2. Click **Connect to Git** and select `RamonRiosJr/the_house_of_karma_wifi_qr`.
3. Set **Framework preset** to `None` (Static HTML).
4. Set **Build output directory** to `/` (leave blank or root).
5. Click **Save and Deploy**.
6. (Optional) Under **Custom Domains**, bind your desired domain (e.g. `wifi.thekarmahouse.org` or `wifi.coquicloud.com`).
