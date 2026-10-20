html_content = """<!DOCTYPE html>
<html lang="en" data-theme="light" data-view="wifi" data-size="4x6">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Karma House - Wi-Fi & Website Sign</title>
  <link rel="icon" type="image/webp" href="karma_logo.webp">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=JetBrains+Mono:wght@600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-body: #f1f5f9;
      --card-bg: #ffffff;
      --card-border: #cbd5e1;
      --card-glow: rgba(0, 0, 0, 0.08);
      --gold: #b8860b;
      --gold-light: #78350f;
      --text-main: #0f172a;
      --text-muted: #475569;
      --plaque-bg: #f8fafc;
      --plaque-border: #e2e8f0;
      --btn-bg: #ffffff;
      --btn-text: #0f172a;
      --btn-border: #cbd5e1;
    }

    html[data-theme="dark"] {
      --bg-body: #080d0a;
      --card-bg: #101a14;
      --card-border: #1f3326;
      --card-glow: rgba(212, 175, 55, 0.14);
      --gold: #d4af37;
      --gold-light: #fef08a;
      --text-main: #f8fafc;
      --text-muted: #8ca394;
      --plaque-bg: #0b140f;
      --plaque-border: #1d3124;
      --btn-bg: #15241b;
      --btn-text: #e2e8f0;
      --btn-border: #2a4433;
    }

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      min-height: 100vh;
      background: var(--bg-body);
      color: var(--text-main);
      font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 1.5rem 1rem;
      transition: background 0.25s ease, color 0.25s ease;
    }

    /* Minimal Top Floating Actions (Hidden on Print) */
    .top-actions {
      display: flex;
      align-items: center;
      gap: 0.65rem;
      margin-bottom: 1.25rem;
      z-index: 10;
      flex-wrap: wrap;
      justify-content: center;
    }

    /* Segmented Pill Group (Options & Common Sizes) */
    .option-pill-group {
      display: inline-flex;
      background: var(--btn-bg);
      border: 1.5px solid var(--btn-border);
      border-radius: 9999px;
      padding: 3px;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.08);
    }

    .pill-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 0.45rem 1rem;
      border-radius: 9999px;
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      transition: all 0.2s ease;
      white-space: nowrap;
    }

    .pill-btn.active {
      background: var(--gold);
      color: #ffffff;
      box-shadow: 0 2px 10px rgba(184, 134, 11, 0.35);
    }

    html[data-theme="dark"] .pill-btn.active {
      color: #0b0f19;
    }

    .action-btn {
      background: var(--btn-bg);
      color: var(--btn-text);
      border: 1px solid var(--btn-border);
      padding: 0.5rem 1rem;
      border-radius: 9999px;
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s ease;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }

    .action-btn:hover {
      transform: translateY(-1px);
      border-color: var(--gold);
      color: var(--gold);
    }

    .action-btn.primary {
      background: linear-gradient(135deg, #d4af37, #b8860b);
      color: #ffffff;
      border: none;
      box-shadow: 0 4px 16px rgba(184, 134, 11, 0.35);
    }

    .action-btn.primary:hover {
      background: linear-gradient(135deg, #fef08a, #d4af37);
      color: #0b0f19;
      transform: translateY(-1px);
    }

    /* The Main Sign Card */
    .wifi-card {
      width: 100%;
      background: var(--card-bg);
      border: 2px solid var(--card-border);
      border-radius: 26px;
      padding: 2.25rem 2rem;
      text-align: center;
      box-shadow: 0 20px 45px -10px rgba(0, 0, 0, 0.12), 0 0 25px var(--card-glow);
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
      transition: all 0.25s ease;
    }

    /* Screen Sizing Rules */
    html[data-size="4x6"] .wifi-card {
      max-width: 440px;
    }
    html[data-size="4x6"] .qr-container {
      width: 320px;
      height: 320px;
    }

    html[data-size="5x7"] .wifi-card {
      max-width: 490px;
    }
    html[data-size="5x7"] .qr-container {
      width: 360px;
      height: 360px;
    }

    html[data-size="letter"] .wifi-card {
      max-width: 540px;
    }
    html[data-size="letter"] .qr-container {
      width: 400px;
      height: 400px;
    }

    /* Card Header */
    .brand-title {
      font-family: 'Cinzel', Georgia, serif;
      font-weight: 800;
      font-size: 1.6rem;
      letter-spacing: 0.12em;
      color: var(--text-main);
      text-transform: uppercase;
      line-height: 1.2;
      margin-bottom: 0.35rem;
    }

    .sub-title {
      font-family: 'Cinzel', Georgia, serif;
      font-size: 0.88rem;
      font-weight: 700;
      letter-spacing: 0.28em;
      color: var(--gold);
      text-transform: uppercase;
      margin-bottom: 1.35rem;
    }

    /* BIG QR CODE FRAME */
    .qr-container {
      max-width: 86vw;
      max-height: 86vw;
      background: #ffffff;
      border-radius: 22px;
      padding: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1px solid #cbd5e1;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
      margin-bottom: 0.85rem;
      position: relative;
      transition: all 0.2s ease;
    }

    .qr-container img {
      width: 100%;
      height: 100%;
      display: block;
      object-fit: contain;
    }

    .scan-prompt {
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--text-muted);
      margin-bottom: 1.15rem;
      display: flex;
      align-items: center;
      gap: 0.35rem;
    }

    .scan-prompt svg {
      color: var(--gold);
    }

    /* Credentials Plaque */
    .creds-plaque {
      width: 100%;
      background: var(--plaque-bg);
      border: 1.5px solid var(--plaque-border);
      border-radius: 14px;
      padding: 0.85rem 1.15rem;
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
      text-align: left;
    }

    .cred-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
    }

    .cred-meta {
      display: flex;
      align-items: baseline;
      gap: 0.75rem;
      overflow: hidden;
    }

    .cred-label {
      font-family: 'Cinzel', Georgia, serif;
      font-weight: 900;
      font-size: 0.78rem;
      letter-spacing: 0.1em;
      color: var(--gold);
      min-width: 50px;
      text-transform: uppercase;
    }

    .cred-val {
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      font-size: 1.12rem;
      color: var(--text-main);
      word-break: break-all;
    }

    .cred-val.password {
      color: var(--gold-light);
    }

    html[data-theme="dark"] .cred-val.password {
      color: #fef08a;
    }

    .cred-divider {
      height: 1px;
      background: var(--plaque-border);
      width: 100%;
    }

    .copy-btn {
      background: #e2e8f0;
      border: 1px solid #cbd5e1;
      color: #334155;
      border-radius: 6px;
      padding: 0.25rem 0.55rem;
      font-size: 0.72rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
      transition: all 0.15s ease;
      flex-shrink: 0;
      text-decoration: none;
    }

    html[data-theme="dark"] .copy-btn {
      background: rgba(255, 255, 255, 0.08);
      border-color: rgba(255, 255, 255, 0.15);
      color: var(--text-muted);
    }

    .copy-btn:hover {
      background: var(--gold);
      color: #ffffff;
      border-color: var(--gold);
    }

    /* View Specific Displays */
    .view-wifi-only {
      display: block;
    }
    .view-web-only,
    .view-review-only {
      display: none;
    }

    html[data-view="wifi"] .view-wifi-only { display: block; }
    html[data-view="wifi"] .view-web-only,
    html[data-view="wifi"] .view-review-only { display: none; }

    html[data-view="web"] .view-wifi-only,
    html[data-view="web"] .view-review-only { display: none; }
    html[data-view="web"] .view-web-only { display: block; }

    html[data-view="review"] .view-wifi-only,
    html[data-view="review"] .view-web-only { display: none; }
    html[data-view="review"] .view-review-only { display: block; }

    /* Toast */
    .toast {
      position: fixed;
      bottom: 2rem;
      background: #10b981;
      color: #ffffff;
      padding: 0.5rem 1.25rem;
      border-radius: 9999px;
      font-size: 0.82rem;
      font-weight: 700;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
      opacity: 0;
      transform: translateY(20px);
      transition: all 0.2s ease;
      pointer-events: none;
      z-index: 100;
    }

    .toast.show {
      opacity: 1;
      transform: translateY(0);
    }

    /* Discreet In-Card Developer Credit */
    .card-credit {
      margin-top: 1.15rem;
      font-size: 0.7rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--text-muted);
      opacity: 0.8;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.35rem;
      flex-wrap: wrap;
    }

    .card-credit a {
      color: inherit;
      text-decoration: none;
      border-bottom: 1px dotted var(--card-border);
      transition: color 0.2s, border-color 0.2s;
    }

    .card-credit a:hover {
      color: var(--gold);
      border-color: var(--gold);
    }

    /* Screen-Only App Footer */
    .app-footer {
      margin-top: 1.5rem;
      text-align: center;
      font-size: 0.78rem;
      color: var(--text-muted);
      line-height: 1.6;
      z-index: 10;
    }

    .app-footer .dev-credits {
      font-size: 0.74rem;
      margin-top: 0.25rem;
      opacity: 0.85;
    }

    .app-footer a.dev-link {
      color: var(--gold);
      text-decoration: none;
      font-weight: 700;
      transition: color 0.2s ease;
    }

    .app-footer a.dev-link:hover {
      text-decoration: underline;
    }

    /* ==========================================================================
       PRINT STYLESHEET: OPTIMIZED FOR COMMON SIZES ON STANDARD OFFICE PAPER
       ========================================================================== */
    @media print {
      @page {
        size: letter portrait;
        margin: 0.3in;
      }

      body {
        background: #ffffff !important;
        color: #000000 !important;
        padding: 0 !important;
        margin: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
      }

      .top-actions, .copy-btn, .toast, .app-footer, .card-credit {
        display: none !important;
      }

      /* 1. Common 4" x 6" Photo / Table Frame */
      html[data-size="4x6"] .wifi-card {
        width: 4in !important;
        max-width: 4in !important;
        height: 6in !important;
        max-height: 6in !important;
        background: #ffffff !important;
        border: 1.5px dashed #64748b !important;
        border-radius: 0 !important;
        box-shadow: none !important;
        padding: 0.25in 0.2in !important;
        margin: 0 auto !important;
      }
      html[data-size="4x6"] .brand-title {
        color: #000000 !important;
        font-size: 1.25rem !important;
        margin-bottom: 0.15rem !important;
      }
      html[data-size="4x6"] .sub-title {
        color: #333333 !important;
        font-size: 0.72rem !important;
        margin-bottom: 0.55rem !important;
      }
      html[data-size="4x6"] .qr-container {
        width: 2.85in !important;
        height: 2.85in !important;
        border: 1px solid #e2e8f0 !important;
        box-shadow: none !important;
        padding: 8px !important;
        margin: 0.08in auto !important;
      }
      html[data-size="4x6"] .scan-prompt {
        color: #333333 !important;
        font-size: 0.68rem !important;
        margin-bottom: 0.45rem !important;
      }
      html[data-size="4x6"] .creds-plaque {
        background: #f8fafc !important;
        border: 1.5px solid #000000 !important;
        padding: 0.45rem 0.65rem !important;
        gap: 0.35rem !important;
      }
      html[data-size="4x6"] .cred-label {
        color: #000000 !important;
        font-size: 0.7rem !important;
      }
      html[data-size="4x6"] .cred-val,
      html[data-size="4x6"] .cred-val.password {
        color: #000000 !important;
        font-size: 0.98rem !important;
        font-weight: 800 !important;
      }

      /* 2. Common 5" x 7" Tabletop Frame */
      html[data-size="5x7"] .wifi-card {
        width: 5in !important;
        max-width: 5in !important;
        height: 7in !important;
        max-height: 7in !important;
        background: #ffffff !important;
        border: 1.5px dashed #64748b !important;
        border-radius: 0 !important;
        box-shadow: none !important;
        padding: 0.35in 0.3in !important;
        margin: 0 auto !important;
      }
      html[data-size="5x7"] .brand-title {
        color: #000000 !important;
        font-size: 1.5rem !important;
        margin-bottom: 0.2rem !important;
      }
      html[data-size="5x7"] .sub-title {
        color: #333333 !important;
        font-size: 0.82rem !important;
        margin-bottom: 0.75rem !important;
      }
      html[data-size="5x7"] .qr-container {
        width: 3.5in !important;
        height: 3.5in !important;
        border: 1px solid #e2e8f0 !important;
        box-shadow: none !important;
        padding: 12px !important;
        margin: 0.12in auto !important;
      }
      html[data-size="5x7"] .scan-prompt {
        color: #333333 !important;
        font-size: 0.75rem !important;
        margin-bottom: 0.65rem !important;
      }
      html[data-size="5x7"] .creds-plaque {
        background: #f8fafc !important;
        border: 1.5px solid #000000 !important;
        padding: 0.6rem 0.85rem !important;
      }
      html[data-size="5x7"] .cred-label {
        color: #000000 !important;
      }
      html[data-size="5x7"] .cred-val,
      html[data-size="5x7"] .cred-val.password {
        color: #000000 !important;
        font-size: 1.15rem !important;
        font-weight: 800 !important;
      }

      /* 3. Common 8.5" x 11" Full Sheet (Wall / Counter Easel) */
      html[data-size="letter"] .wifi-card {
        width: 6.8in !important;
        max-width: 6.8in !important;
        height: auto !important;
        background: #ffffff !important;
        border: 2px solid #000000 !important;
        border-radius: 16px !important;
        box-shadow: none !important;
        padding: 0.5in 0.4in !important;
        margin: 0 auto !important;
      }
      html[data-size="letter"] .brand-title {
        color: #000000 !important;
        font-size: 2rem !important;
        margin-bottom: 0.35rem !important;
      }
      html[data-size="letter"] .sub-title {
        color: #333333 !important;
        font-size: 1.1rem !important;
        margin-bottom: 1.25rem !important;
      }
      html[data-size="letter"] .qr-container {
        width: 4.8in !important;
        height: 4.8in !important;
        border: 1px solid #e2e8f0 !important;
        box-shadow: none !important;
        padding: 16px !important;
        margin: 0.2in auto !important;
      }
      html[data-size="letter"] .scan-prompt {
        color: #333333 !important;
        font-size: 0.9rem !important;
        margin-bottom: 0.85rem !important;
      }
      html[data-size="letter"] .creds-plaque {
        background: #f8fafc !important;
        border: 1.5px solid #000000 !important;
        padding: 0.85rem 1.25rem !important;
      }
      html[data-size="letter"] .cred-label {
        color: #000000 !important;
        font-size: 0.95rem !important;
      }
      html[data-size="letter"] .cred-val,
      html[data-size="letter"] .cred-val.password {
        color: #000000 !important;
        font-size: 1.45rem !important;
        font-weight: 800 !important;
      }
    }
  </style>
</head>
<body>

  <!-- Top Minimal Floating Buttons: Content, Common Sizes, Print, Theme -->
  <div class="top-actions">
    <!-- View Switcher -->
    <div class="option-pill-group">
      <button class="pill-btn active" id="btn-view-wifi" onclick="switchView('wifi')">
        📶 Wi-Fi
      </button>
      <button class="pill-btn" id="btn-view-web" onclick="switchView('web')">
        🌐 TheKarmaHouse.org
      </button>
      <button class="pill-btn" id="btn-view-review" onclick="switchView('review')">
        ⭐ Google Reviews
      </button>
    </div>

    <!-- Common Frame Sizes -->
    <div class="option-pill-group">
      <button class="pill-btn active" id="btn-size-4x6" onclick="setSize('4x6')" title="Standard 4x6 Dollar Store Frame">
        4"×6"
      </button>
      <button class="pill-btn" id="btn-size-5x7" onclick="setSize('5x7')" title="Medium 5x7 Tabletop Frame">
        5"×7"
      </button>
      <button class="pill-btn" id="btn-size-letter" onclick="setSize('letter')" title="Standard 8.5x11 Full Page">
        8.5"×11"
      </button>
    </div>

    <!-- Print & Theme Buttons -->
    <button class="action-btn primary" onclick="window.print()" title="Print Sign">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>
      Print
    </button>
    <button class="action-btn" onclick="toggleTheme()" title="Switch Dark/Light Theme">
      🌓 Theme
    </button>
  </div>

  <!-- Main Sign Card -->
  <div class="wifi-card">
    
    <!-- Title & Dynamic Subtitle -->
    <h1 class="brand-title">THE KARMA HOUSE</h1>
    <div class="sub-title" id="card-subtitle">GUEST WI-FI</div>

    <!-- BIG QR CODE (Direct Image Path for Instant Safari / iOS Rendering) -->
    <div class="qr-container">
      <img id="qr-image" src="karma_wifi_qr_branded.png" alt="KarmaHGuest Wi-Fi QR Code">
    </div>

    <div class="scan-prompt" id="scan-hint-text">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path><circle cx="12" cy="13" r="4"></circle></svg>
      <span>Scan with camera to connect automatically</span>
    </div>

    <!-- Credentials Plaque -->
    <div class="creds-plaque">
      
      <!-- Wi-Fi View Content -->
      <div class="view-wifi-only">
        <div class="cred-row">
          <div class="cred-meta">
            <span class="cred-label">WIFI:</span>
            <span class="cred-val">KarmaHGuest</span>
          </div>
          <button class="copy-btn" onclick="copyText('KarmaHGuest', 'Wi-Fi name copied!')">Copy</button>
        </div>

        <div class="cred-divider" style="margin: 0.65rem 0;"></div>

        <div class="cred-row">
          <div class="cred-meta">
            <span class="cred-label">PASS:</span>
            <span class="cred-val password">KarmaTea2026!</span>
          </div>
          <button class="copy-btn" onclick="copyText('KarmaTea2026!', 'Password copied!')">Copy</button>
        </div>
      </div>

      <!-- TheKarmaHouse.org View Content (Single Clean Row for Print) -->
      <div class="view-web-only">
        <div class="cred-row" style="justify-content: center;">
          <div class="cred-meta" style="justify-content: center;">
            <span class="cred-label" style="min-width: unset;">WEBSITE:</span>
            <span class="cred-val" style="font-size: 1.2rem; color: var(--gold-light);">TheKarmaHouse.org</span>
          </div>
        </div>
      </div>

      <!-- Google Reviews View Content -->
      <div class="view-review-only">
        <div class="cred-row" style="justify-content: space-between;">
          <div class="cred-meta">
            <span class="cred-label" style="min-width: unset;">REVIEWS:</span>
            <span class="cred-val" style="font-size: 1.05rem; color: var(--gold-light);">The Karma House</span>
          </div>
          <a href="https://www.google.com/search?q=the+karma+house&rlz=1C1GCEA_enUS1138US1138&oq=the+karma+house&gs_lcrp=EgZjaHJvbWUqCggAEAAY4wIYgAQyCggAEAAY4wIYgAQyEAgBEC4YrwEYxwEYgAQYjgUyBwgCEAAYgAQyBwgDEAAYgAQyBwgEEAAYgAQyBwgFEAAYgAQyBwgGEAAYgAQyCAgHEAAYFhgeMggICBAAGBYYHjIICAkQABgWGB7SAQg0NjI5ajBqNKgCAbACAfEF6pj0nNfCmanxBeqY9JzXwpmp&sourceid=chrome&source=chrome.ob&ie=UTF-8#lrd=0x876b8753cd9737f3:0x74b26ca762433549,3,,,," target="_blank" rel="noopener" class="copy-btn" style="text-decoration: none; padding: 0.35rem 0.75rem; background: var(--gold); color: #ffffff; border: none; font-weight: 700;">Open Review ⭐</a>
        </div>
      </div>

    </div>

  </div>

  <!-- Screen Page Footer -->
  <footer class="app-footer">
    <div style="display: flex; justify-content: center; gap: 0.65rem; margin-bottom: 0.85rem; flex-wrap: wrap;">
      <a href="https://www.google.com/search?q=the+karma+house&rlz=1C1GCEA_enUS1138US1138&oq=the+karma+house&gs_lcrp=EgZjaHJvbWUqCggAEAAY4wIYgAQyCggAEAAY4wIYgAQyEAgBEC4YrwEYxwEYgAQYjgUyBwgCEAAYgAQyBwgDEAAYgAQyBwgEEAAYgAQyBwgFEAAYgAQyBwgGEAAYgAQyCAgHEAAYFhgeMggICBAAGBYYHjIICAkQABgWGB7SAQg0NjI5ajBqNKgCAbACAfEF6pj0nNfCmanxBeqY9JzXwpmp&sourceid=chrome&source=chrome.ob&ie=UTF-8#lrd=0x876b8753cd9737f3:0x74b26ca762433549,3,,,," target="_blank" rel="noopener" class="action-btn" style="text-decoration: none; font-size: 0.78rem; padding: 0.45rem 1rem;">
        ⭐ Direct Google Reviews Link
      </a>
      <a href="https://thekarmahouse.org" target="_blank" rel="noopener" class="action-btn" style="text-decoration: none; font-size: 0.78rem; padding: 0.45rem 1rem;">
        🌐 TheKarmaHouse.org
      </a>
    </div>
    <p>&copy; 2026 <strong>The Karma House Kava &amp; Community Lounge</strong> &bull; All Rights Reserved</p>
    <p class="dev-credits">
      Custom Signage &amp; QR Infrastructure by 
      <a href="https://ramonrios.net" target="_blank" rel="noopener" class="dev-link">Ramon Rios Jr.</a> 
      | <a href="https://coqui.cloud" target="_blank" rel="noopener" class="dev-link">Coqui Cloud</a>
    </p>
  </footer>

  <div class="toast" id="toast-notify">Copied!</div>

  <script>
    const qrWifiSrc = "karma_wifi_qr_branded.png";
    const qrWebSrc = "karma_website_qr_branded.png";
    const qrReviewSrc = "karma_review_qr_branded.png";

    function switchView(viewName) {
      const html = document.documentElement;
      html.setAttribute('data-view', viewName);

      const btnWifi = document.getElementById('btn-view-wifi');
      const btnWeb = document.getElementById('btn-view-web');
      const btnReview = document.getElementById('btn-view-review');
      const subtitle = document.getElementById('card-subtitle');
      const qrImg = document.getElementById('qr-image');
      const scanHint = document.querySelector('#scan-hint-text span');

      btnWifi.classList.toggle('active', viewName === 'wifi');
      btnWeb.classList.toggle('active', viewName === 'web');
      btnReview.classList.toggle('active', viewName === 'review');

      if (viewName === 'wifi') {
        subtitle.textContent = 'GUEST WI-FI';
        qrImg.src = qrWifiSrc;
        qrImg.alt = 'KarmaHGuest Wi-Fi QR Code';
        scanHint.textContent = 'Scan with camera to connect automatically';
      } else if (viewName === 'web') {
        subtitle.textContent = 'THEKARMAHOUSE.ORG';
        qrImg.src = qrWebSrc;
        qrImg.alt = 'TheKarmaHouse.org QR Code';
        scanHint.textContent = 'Scan with camera to visit TheKarmaHouse.org';
      } else if (viewName === 'review') {
        subtitle.textContent = 'GOOGLE REVIEWS';
        qrImg.src = qrReviewSrc;
        qrImg.alt = 'Google Reviews QR Code';
        scanHint.textContent = 'Scan with camera to leave us a 5-star review';
      }
    }

    function setSize(sz) {
      const html = document.documentElement;
      html.setAttribute('data-size', sz);
      document.querySelectorAll('[id^="btn-size-"]').forEach(btn => btn.classList.remove('active'));
      const activeBtn = document.getElementById('btn-size-' + sz);
      if (activeBtn) activeBtn.classList.add('active');
    }

    function toggleTheme() {
      const html = document.documentElement;
      const current = html.getAttribute('data-theme') || 'light';
      html.setAttribute('data-theme', current === 'light' ? 'dark' : 'light');
    }

    function copyText(val, msg) {
      navigator.clipboard.writeText(val).then(() => {
        showToast(msg);
      }).catch(() => {
        const el = document.createElement('input');
        el.value = val;
        document.body.appendChild(el);
        el.select();
        document.execCommand('copy');
        document.body.removeChild(el);
        showToast(msg);
      });
    }

    function showToast(msg) {
      const toast = document.getElementById('toast-notify');
      toast.textContent = msg;
      toast.classList.add('show');
      setTimeout(() => toast.classList.remove('show'), 1600);
    }
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updated index.html to clean light theme with direct images successfully!")
