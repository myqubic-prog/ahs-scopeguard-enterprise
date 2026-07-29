# AHS Scope Guard Enterprise v1.0

## Scope Creep Risk Auditor & Revenue Defense Platform

Enterprise-grade B2B SaaS compliance tool for consultants, digital agency owners, and legal strategists.

---

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the application
streamlit run app.py
```

The application opens at `http://localhost:8501` in your default browser.

---

## Features

### Left Column — Contract Ingestion & Input Portal
- **File Upload 1:** Signed Service Agreement / SOW (PDF/TXT)
- **File Upload 2:** Disputed Client Email / WhatsApp Log (PDF/TXT)
- **Hourly Premium Rate Slider:** $50 – $500 per hour
- **Estimated Hours Selector:** 1 – 200 hours
- **Out-of-Scope Request Type Dropdown:** 10 common scope creep scenarios

### Right Column — AI-Driven Scope Creep Risk Matrix
- **Default Placeholder:** Elegant locked card shown until audit runs
- **Three Executive Metric Cards:**
  - Total Capital Leakage (hours × rate)
  - Timeline Delay Index (schedule slippage %)
  - Contract Breach Vulnerability (risk score /100)
- **Vector Breach Matrix Table:** Color-coded rows by severity (Critical, High, Moderate, Low)
- **Revenue Defense Email Script:** Copy-paste-ready legal email template
- **Excel Export:** 4-sheet professional report with all data and AHS Nexus recommendations
- **AHS Nexus Leads Funnel:** Premium green callout box with services list and email booking form

---

## Technology Stack

| Component | Technology |
|---|---|
| Frontend | Python Streamlit |
| Data Processing | Pandas 2.1.0+ |
| Excel Export | Openpyxl |
| Styling | Custom CSS with Enterprise Dark Theme |
| Theme Colors | Deep Charcoal #090D16, Neon Mint #10B981, Amber Gold #F59E0B, Electric Violet #6366F1 |

---

## Deployment

### Streamlit Cloud
1. Push `app.py` and `requirements.txt` to a GitHub repository
2. Connect the repository at https://share.streamlit.io
3. Set the main file to `app.py` and click Deploy

### Local / On-Premises
```bash
streamlit run app.py --server.port 8080 --server.headless true
```

---

## Built for AHS Nexus
**https://ahsnexus.com**

For demonstration purposes only. Not a substitute for legal counsel.
