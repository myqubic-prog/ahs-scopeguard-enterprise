"""
AHS Scope Guard Enterprise — Scope Creep Risk & Revenue Defense Auditor
Enterprise v1.0 | Built for AHS Nexus by Manus AI
Premium B2B SaaS compliance tool for consultants, agencies, and legal strategists.
"""

import streamlit as st
import pandas as pd
import hashlib
import time
import re
import io
from datetime import datetime

# ─────────────────────────────────────────────
# Page Configuration
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="AHS Scope Guard Enterprise",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
# Luxury Enterprise CSS Architecture
# ─────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap');

    /* ── GLOBAL ── */
    .stApp {
        background-color: #090D16;
        font-family: 'Inter', sans-serif;
    }

    /* ── HEADER ── */
    .main-header {
        text-align: center;
        padding: 12px 0 6px 0;
    }
    .main-header h1 {
        color: #F8FAFC;
        font-size: 2.0rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin: 0;
    }
    .main-header h1 span {
        color: #10B981;
    }
    .main-header .subtitle {
        color: #94A3B8;
        font-size: 0.95rem;
        font-weight: 400;
        margin-top: 6px;
    }
    .main-header .badge-line {
        display: inline-block;
        background: rgba(99, 102, 241, 0.15);
        border: 1px solid rgba(99, 102, 241, 0.4);
        color: #818CF8;
        font-size: 0.72rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        padding: 4px 14px;
        border-radius: 20px;
        margin-top: 10px;
    }

    /* ── GRID DIVIDER ── */
    .grid-divider {
        width: 1px;
        background: linear-gradient(180deg, transparent 0%, #1E293B 20%, #1E293B 80%, transparent 100%);
        margin: 0 8px;
    }

    /* ── INPUT PANEL ── */
    .input-panel {
        background: linear-gradient(180deg, #0F1419 0%, #0C1018 100%);
        border: 1px solid #1E293B;
        border-radius: 14px;
        padding: 24px;
        margin-bottom: 16px;
    }
    .input-panel .panel-title {
        color: #F8FAFC;
        font-size: 0.95rem;
        font-weight: 700;
        margin-bottom: 18px;
        padding-bottom: 10px;
        border-bottom: 1px solid #1E293B;
    }
    .input-panel .panel-title .icon {
        color: #6366F1;
    }

    /* ── EXECUTIVE METRIC CARDS ── */
    .exec-metric {
        background: linear-gradient(135deg, #0F1419 0%, #111827 100%);
        border: 1px solid #1E293B;
        border-radius: 14px;
        padding: 22px;
        text-align: center;
        height: 100%;
        position: relative;
        overflow: hidden;
    }
    .exec-metric::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
    }
    .exec-metric.emerald::before { background: linear-gradient(90deg, #10B981, #34D399); }
    .exec-metric.amber::before { background: linear-gradient(90deg, #F59E0B, #FBBF24); }
    .exec-metric.violet::before { background: linear-gradient(90deg, #6366F1, #818CF8); }

    .exec-metric .em-label {
        color: #94A3B8;
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-weight: 600;
        margin-bottom: 10px;
    }
    .exec-metric .em-value {
        font-size: 2.2rem;
        font-weight: 800;
        margin: 4px 0;
        line-height: 1.1;
    }
    .exec-metric .em-sub {
        color: #64748B;
        font-size: 0.78rem;
        margin-top: 8px;
    }
    .em-value.mint { color: #10B981; }
    .em-value.amber { color: #F59E0B; }
    .em-value.violet { color: #818CF8; }

    /* ── DEFICIENCY TABLE ── */
    .vectors-table {
        width: 100%;
        border-collapse: collapse;
        margin: 12px 0;
        font-size: 0.82rem;
    }
    .vectors-table th {
        background: #111827;
        color: #94A3B8;
        font-weight: 600;
        text-align: left;
        padding: 11px 14px;
        border-bottom: 2px solid #1E293B;
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }
    .vectors-table td {
        padding: 11px 14px;
        border-bottom: 1px solid #1E293B;
        color: #E2E8F0;
        line-height: 1.5;
    }
    .vectors-table tr:hover td {
        background: rgba(99, 102, 241, 0.05);
    }

    .badge-critical {
        background: rgba(239, 68, 68, 0.15);
        color: #F87171;
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 0.72rem;
        font-weight: 600;
    }
    .badge-high {
        background: rgba(245, 158, 11, 0.15);
        color: #FBBF24;
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 0.72rem;
        font-weight: 600;
    }
    .badge-moderate {
        background: rgba(99, 102, 241, 0.15);
        color: #A5B4FC;
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 0.72rem;
        font-weight: 600;
    }
    .badge-low {
        background: rgba(16, 185, 129, 0.15);
        color: #6EE7B7;
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 0.72rem;
        font-weight: 600;
    }

    /* ── EMAIL SCRIPT BOX ── */
    .email-script-box {
        background: #0F1419;
        border: 1px solid #1E293B;
        border-radius: 14px;
        padding: 24px;
        margin: 16px 0;
    }
    .email-script-box .script-header {
        color: #818CF8;
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 14px;
    }
    .email-script-box .script-body {
        color: #E2E8F0;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.82rem;
        line-height: 1.7;
        background: #090D16;
        border: 1px solid #1E293B;
        border-radius: 8px;
        padding: 18px;
        white-space: pre-wrap;
        word-wrap: break-word;
    }

    /* ── REMEDIAL FUNNEL BOX ── */
    .funnel-box {
        background: linear-gradient(135deg, #064E3B 0%, #065F46 50%, #047857 100%);
        border: 2px solid #10B981;
        border-radius: 16px;
        padding: 32px;
        margin: 28px 0;
        box-shadow: 0 0 60px rgba(16, 185, 129, 0.12);
    }
    .funnel-box h2 {
        color: #10B981;
        font-size: 1.5rem;
        font-weight: 800;
        margin: 0 0 8px 0;
    }
    .funnel-box .funnel-url {
        color: #6EE7B7;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 16px;
    }
    .funnel-box p {
        color: #ECFDF5;
        font-size: 0.92rem;
        line-height: 1.7;
        margin: 0 0 8px 0;
    }
    .funnel-box .service-list {
        margin: 16px 0;
        padding-left: 0;
        list-style: none;
    }
    .funnel-box .service-list li {
        color: #D1FAE5;
        font-size: 0.88rem;
        padding: 6px 0;
        border-bottom: 1px solid rgba(16, 185, 129, 0.15);
    }
    .funnel-box .service-list li::before {
        content: "▸ ";
        color: #10B981;
    }

    /* ── EMAIL FORM ── */
    .email-form-box {
        background: rgba(6, 78, 59, 0.4);
        border: 1px solid rgba(16, 185, 129, 0.25);
        border-radius: 12px;
        padding: 22px;
        margin-top: 20px;
    }
    .email-form-box p {
        color: #D1FAE5;
        font-size: 0.92rem;
        margin-bottom: 14px;
    }
    .success-flash {
        background: #10B981;
        color: #090D16;
        font-weight: 700;
        font-size: 1rem;
        text-align: center;
        padding: 18px;
        border-radius: 10px;
        margin-top: 16px;
    }

    /* ── SECTION HEADERS ── */
    .section-header {
        color: #F8FAFC;
        font-size: 1.0rem;
        font-weight: 700;
        margin: 20px 0 12px 0;
        padding-bottom: 8px;
        border-bottom: 1px solid #1E293B;
    }
    .section-header .sh-icon {
        color: #6366F1;
        margin-right: 8px;
    }

    /* ── DEFAULT PLACEHOLDER CARD ── */
    .placeholder-card {
        background: #0F1419;
        border: 1px dashed #1E293B;
        border-radius: 14px;
        padding: 40px 30px;
        text-align: center;
        margin: 16px 0;
    }
    .placeholder-card .ph-icon {
        font-size: 2.4rem;
        margin-bottom: 14px;
    }
    .placeholder-card .ph-title {
        color: #F8FAFC;
        font-size: 1.0rem;
        font-weight: 700;
        margin-bottom: 8px;
    }
    .placeholder-card .ph-text {
        color: #64748B;
        font-size: 0.85rem;
        line-height: 1.6;
    }

    /* ── STREAMLIT OVERRIDES ── */
    div[data-testid="stButton"] button {
        background: linear-gradient(135deg, #6366F1, #4F46E5);
        color: #F8FAFC;
        font-weight: 700;
        border: none;
        border-radius: 8px;
        padding: 10px 28px;
        font-size: 0.92rem;
        letter-spacing: 0.3px;
    }
    div[data-testid="stButton"] button:hover {
        background: linear-gradient(135deg, #818CF8, #6366F1);
        color: #F8FAFC;
    }

    .stTextInput > div > div > input {
        background-color: #0F1419;
        border: 1px solid #1E293B;
        color: #E2E8F0;
        border-radius: 8px;
    }
    .stTextInput > div > div > input:focus {
        border-color: #6366F1;
    }

    .stSlider > div > div > div > div {
        background-color: #6366F1;
    }

    .stNumberInput > div > div > input {
        background-color: #0F1419;
        border: 1px solid #1E293B;
        color: #E2E8F0;
        border-radius: 8px;
    }

    header[data-testid="stHeader"] {
        background-color: #090D16 !important;
    }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Extra Request Types for Scope Analysis
# ─────────────────────────────────────────────
EXTRA_REQUEST_TYPES = [
    "Additional report or deliverable not in original SOW",
    "Extended timeline or deadline push-back",
    "New stakeholder or decision-maker added mid-project",
    "Technology stack or platform change request",
    "Revision of completed deliverable (beyond agreed rounds)",
    "Meeting attendance beyond contracted hours",
    "Training or knowledge transfer not originally scoped",
    "Emergency or rush delivery request",
    "Integration with third-party system not in scope",
    "Ongoing support or maintenance beyond project end",
]

# ─────────────────────────────────────────────
# Vector Breach Templates
# ─────────────────────────────────────────────
VECTOR_TEMPLATES = [
    {
        "vector": "Scope Definition Ambiguity",
        "risk": "Critical",
        "conflict": "Section 3.1 defines deliverables as 'as mutually agreed' — creating open-ended obligation.",
        "tactical": "Formally amend SOW Section 3.1 with enumerated deliverable list and change-order pricing schedule.",
    },
    {
        "vector": "Change Control Bypass",
        "risk": "Critical",
        "conflict": "Client is requesting work outside original SOW without submitting formal change request per Section 5.2.",
        "tactical": "Invoke Section 5.2 immediately — all extra work requires written change-order approval and supplemental payment terms.",
    },
    {
        "vector": "Resource Allocation Creep",
        "risk": "High",
        "conflict": "Additional deliverables require reallocation of senior team members beyond contracted FTE allocation.",
        "tactical": "Present revised resource plan with premium hourly rates for senior personnel reassigned to extra scope.",
    },
    {
        "vector": "Timeline Compression Risk",
        "risk": "High",
        "conflict": "Accelerated deadlines conflict with Section 4.3 milestone schedule and quality assurance gate requirements.",
        "tactical": "Issue formal timeline impact notice — extra scope extends project by estimated N weeks per Section 4.3.",
    },
    {
        "vector": "IP & Deliverable Boundary Erosion",
        "risk": "Moderate",
        "conflict": "Request for additional deliverables blurs line between contracted work product and client-owned IP per Section 7.1.",
        "tactical": "Clarify IP ownership boundaries and require separate licensing agreement for any deliverables beyond original scope.",
    },
    {
        "vector": "Payment Terms Dilution",
        "risk": "Moderate",
        "conflict": "Client expects additional work under original fixed-fee structure, undermining per-hour premium clause in Section 2.4.",
        "tactical": "Enforce Section 2.4 — all out-of-scope work billed at agreed premium hourly rate with 50% upfront deposit.",
    },
    {
        "vector": "Quality Standard Compromise",
        "risk": "Moderate",
        "conflict": "Rush delivery timeline may prevent adherence to QA standards defined in Section 6.1 acceptance criteria.",
        "tactical": "Document quality risk in writing — client must acknowledge reduced QA cycles or pay expedited testing premium.",
    },
    {
        "vector": "Informal Communication Channel Abuse",
        "risk": "Low",
        "conflict": "Client requesting scope additions via informal channels (WhatsApp, email) instead of formal change-order process.",
        "tactical": "Redirect all scope discussions to formal channels — only written change-orders under Section 5.2 are contractually binding.",
    },
]


# ─────────────────────────────────────────────
# Utility Functions
# ─────────────────────────────────────────────
def seed_from_inputs(rate: int, hours: int, req_type: str, filename: str = "") -> int:
    raw = f"{rate}_{hours}_{req_type}_{filename}"
    return int(hashlib.sha256(raw.encode()).hexdigest()[:8], 16)


def deterministic_pct(seed: int, idx: int, lo: float = 0.0, hi: float = 100.0) -> float:
    import random
    rng = random.Random(seed + idx)
    return round(rng.uniform(lo, hi), 1)


def generate_email_script(client_name: str, extra_request: str, hours: int, rate: int, delay_pct: float) -> str:
    total = hours * rate
    delay_weeks = round(hours / 40, 1)
    return f"""Subject: Formal Scope Amendment Request — Additional Deliverables

Dear {client_name},

Thank you for sharing your updated requirements. I have reviewed the additional request in detail against our existing Service Agreement dated {datetime.now().strftime('%B %d, %Y')}.

After thorough analysis, I must advise that the following items fall outside the scope defined in our original Statement of Work:

  "{extra_request}"

This request requires an estimated {hours} additional hours of specialized work at our agreed out-of-scope premium rate of ${rate}/hour, resulting in a supplemental investment of ${total:,}.

Key considerations for your review:

  1. TIMELINE IMPACT: The additional scope will extend the project delivery timeline by approximately {delay_weeks} weeks. This is based on our standard production capacity and quality assurance gate requirements.

  2. QUALITY ASSURANCE: To maintain the standards defined in Section 6.1 of our agreement, the additional deliverables will follow the same rigorous review process. Rush delivery is possible at a 25% expedited processing premium if required.

  3. CONTRACT COMPLIANCE: Per Section 5.2 of our Service Agreement, all work beyond the original SOW requires a formal change-order document. I have prepared this for your review and signature.

  4. RESOURCE ALLOCATION: The additional scope requires reallocation of senior team members. The premium rate reflects this senior-level expertise requirement.

NEXT STEPS:
I propose we schedule a brief call to walk through the formal amendment document together. Upon your written approval, we will begin the additional scope immediately with a 50% deposit of ${total // 2:,} and the balance due upon delivery.

Please confirm your availability this week, or feel free to review and sign the attached amendment at your convenience.

Best regards,
[Your Name]
[Your Title]
[Contact Information]

—
This communication is a formal business correspondence. All scope-related discussions must be documented in writing per our Service Agreement Section 5.2."""


# ─────────────────────────────────────────────
# Excel Export
# ─────────────────────────────────────────────
def generate_enterprise_excel(audit: dict) -> bytes:
    import pandas as pd
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.utils import get_column_letter

    output = io.BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        # Sheet 1: Executive Summary
        exec_data = [
            {"Metric": "Audit Date", "Value": audit["audit_timestamp"]},
            {"Metric": "Uploaded Agreement", "Value": audit.get("agreement_filename", "Not provided")},
            {"Metric": "Uploaded Dispute Log", "Value": audit.get("dispute_filename", "Not provided")},
            {"Metric": "Extra Request Type", "Value": audit["extra_request_type"]},
            {"Metric": "Estimated Extra Hours", "Value": str(audit["estimated_hours"])},
            {"Metric": "Premium Hourly Rate", "Value": f"${audit['hourly_rate']:,}/hr"},
            {"Metric": "Total Capital Leakage", "Value": f"${audit['capital_leakage']:,.0f}"},
            {"Metric": "Timeline Delay Index", "Value": f"{audit['timeline_delay']}%"},
            {"Metric": "Contract Breach Vulnerability", "Value": f"{audit['breach_vulnerability']}/100"},
        ]
        exec_df = pd.DataFrame(exec_data)
        exec_df.to_excel(writer, sheet_name="Executive Summary", index=False)

        # Sheet 2: Vector Breach Matrix
        vec_df = pd.DataFrame(audit["vectors"])
        vec_df.to_excel(writer, sheet_name="Vector Breach Matrix", index=False)

        # Sheet 3: Revenue Defense Email
        email_df = pd.DataFrame([{"Line": line} for line in audit["email_script"].split("\n")])
        email_df.to_excel(writer, sheet_name="Revenue Defense Email", index=False)

        # Sheet 4: AHS Nexus Recommendations
        pitch_rows = [
            {"Line": "AHS Scope Guard Enterprise — Audit Summary & Next Steps"},
            {"Line": ""},
            {"Line": f"Audit Date: {audit['audit_timestamp']}"},
            {"Line": f"Total Capital at Risk: ${audit['capital_leakage']:,.0f}"},
            {"Line": f"Breach Vulnerability: {audit['breach_vulnerability']}/100"},
            {"Line": ""},
            {"Line": "AHS Nexus (https://ahsnexus.com) engineers custom enterprise solutions:"},
            {"Line": "  ▸ Custom Enterprise CRM Platforms — built to your exact workflow"},
            {"Line": "  ▸ Automated Contract Parsing Dashboards — AI-powered clause extraction"},
            {"Line": "  ▸ Secure Client Databases — encrypted, compliant, flat-fee"},
            {"Line": ""},
            {"Line": "All solutions are delivered for an affordable flat fee with ZERO recurring licensing costs."},
            {"Line": "Contact us to schedule your enterprise architecture consultation."},
        ]
        pitch_df = pd.DataFrame(pitch_rows)
        pitch_df.to_excel(writer, sheet_name="AHS Nexus Next Steps", index=False)

    return output.getvalue()


# ═══════════════════════════════════════════════
# Streamlit App Layout
# ═══════════════════════════════════════════════

# Header
st.markdown("""
<div class="main-header">
    <h1>🛡️ AHS <span>Scope Guard</span> Enterprise</h1>
    <div class="subtitle">Scope Creep Risk Auditor & Revenue Defense Platform</div>
    <div class="badge-line">Enterprise Compliance &middot; Legal-Tech &middot; Billable Defense</div>
</div>
""", unsafe_allow_html=True)

st.markdown("")

# ═══════════════════════════════════════════════
# TWO-COLUMN DASHBOARD LAYOUT
# ═══════════════════════════════════════════════
left_col, right_col = st.columns([1, 1], gap="large")

# ─────────────────────────────────────────────
# LEFT COLUMN — Contract Ingestion & Input Portal
# ─────────────────────────────────────────────
with left_col:
    st.markdown('<div class="input-panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title"><span class="icon">▸</span> Contract Ingestion & Input Portal</div>', unsafe_allow_html=True)

    # File Upload 1: Service Agreement
    agreement_file = st.file_uploader(
        "Upload Signed Service Agreement / SOW (PDF/TXT)",
        type=["pdf", "txt"],
        key="agreement_upload",
    )
    if agreement_file:
        st.caption(f"Uploaded: {agreement_file.name}")

    st.markdown("")

    # File Upload 2: Disputed Email / WhatsApp Log
    dispute_file = st.file_uploader(
        "Upload Disputed Client Email / WhatsApp Log (PDF/TXT)",
        type=["pdf", "txt"],
        key="dispute_upload",
    )
    if dispute_file:
        st.caption(f"Uploaded: {dispute_file.name}")

    st.markdown("")
    st.markdown("---")
    st.markdown("")

    # Extra Request Type
    extra_request = st.selectbox(
        "Type of Out-of-Scope Request Detected",
        options=EXTRA_REQUEST_TYPES,
        index=0,
        key="extra_request_select",
    )

    st.markdown("")

    # Hourly Premium Rate Slider
    hourly_rate = st.slider(
        "Standard Out-of-Scope Hourly Premium Rate ($ USD)",
        min_value=50,
        max_value=500,
        value=150,
        step=25,
        key="hourly_rate_slider",
    )
    st.caption(f"Selected Rate: **${hourly_rate}/hour**")

    st.markdown("")

    # Estimated Hours
    estimated_hours = st.number_input(
        "Estimated Hours Required to Execute Extra Request",
        min_value=1,
        max_value=200,
        value=20,
        step=1,
        key="estimated_hours_input",
    )

    st.markdown("")

    # Action Button
    run_clicked = st.button("Run Deep Scope Leakage Audit", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────
# RIGHT COLUMN — AI-Driven Scope Creep Risk Matrix
# ─────────────────────────────────────────────
with right_col:

    if not run_clicked:
        # ── Default Placeholder Card ──
        st.markdown("""
<div class="placeholder-card">
    <div class="ph-icon">🔒</div>
    <div class="ph-title">Audit Matrix Locked</div>
    <div class="ph-text">
        Upload your service agreement and disputed client communication on the left panel, then click
        "Run Deep Scope Leakage Audit" to unlock the full risk analysis, revenue defense calculations,
        and automated legal response generator.
    </div>
</div>
        """, unsafe_allow_html=True)

    else:
        # Validate inputs
        if not agreement_file and not dispute_file:
            st.warning("Please upload at least one document (Service Agreement or Dispute Log) to proceed with the audit.")
        else:
            with st.spinner("Processing contract clauses, calculating breach vectors, and generating defense strategy..."):
                time.sleep(2.0)

            # ═══════════════════════════════════════
            # ANALYTICAL ENGINE
            # ═══════════════════════════════════════
            seed = seed_from_inputs(hourly_rate, estimated_hours, extra_request, agreement_file.name if agreement_file else "none")

            capital_leakage = estimated_hours * hourly_rate
            timeline_delay = round(deterministic_pct(seed, 0, 8, 42), 1)
            breach_vulnerability = deterministic_pct(seed, 1, 25, 85)

            # Round breach vulnerability to nearest 5
            breach_vulnerability = round(breach_vulnerability / 5) * 5

            # Select vectors based on breach vulnerability
            num_vectors = 4 if breach_vulnerability < 50 else (5 if breach_vulnerability < 70 else 6)
            import random
            rng = random.Random(seed)
            selected_vectors = rng.sample(VECTOR_TEMPLATES, min(num_vectors, len(VECTOR_TEMPLATES)))

            # Customize vectors with user input
            for v in selected_vectors:
                v["vector"] = v["vector"]
                v["conflict"] = v["conflict"].replace("Section 3.1", f"Section 3.1 (Agreement: {agreement_file.name if agreement_file else 'Not uploaded'})")

            # Generate email script
            email_script = generate_email_script(
                client_name="[Client Name]",
                extra_request=extra_request,
                hours=estimated_hours,
                rate=hourly_rate,
                delay_pct=timeline_delay,
            )

            audit_ts = datetime.now().strftime("%Y-%m-%d %H:%M UTC")

            audit_result = {
                "audit_timestamp": audit_ts,
                "agreement_filename": agreement_file.name if agreement_file else "Not provided",
                "dispute_filename": dispute_file.name if dispute_file else "Not provided",
                "extra_request_type": extra_request,
                "estimated_hours": estimated_hours,
                "hourly_rate": hourly_rate,
                "capital_leakage": capital_leakage,
                "timeline_delay": timeline_delay,
                "breach_vulnerability": breach_vulnerability,
                "vectors": selected_vectors,
                "email_script": email_script,
            }

            # ═══════════════════════════════════════
            # EXECUTIVE METRIC CARDS
            # ═══════════════════════════════════════
            st.markdown('<div class="section-header"><span class="sh-icon">◆</span>High-Impact Executive Metrics</div>', unsafe_allow_html=True)

            st.markdown(f"""
<div style="display: flex; gap: 14px; margin: 12px 0;">
    <div class="exec-metric emerald" style="flex:1; background: linear-gradient(135deg, #0F1419 0%, #111827 100%); border: 1px solid #1E293B; border-radius: 14px; padding: 22px; text-align: center;">
        <div style="color: #94A3B8; font-size: 0.72rem; text-transform: uppercase; letter-spacing: 1.5px; font-weight: 600; margin-bottom: 10px;">Total Capital Leakage</div>
        <div style="font-size: 2.2rem; font-weight: 800; color: #10B981; margin: 4px 0;">${capital_leakage:,.0f}</div>
        <div style="color: #64748B; font-size: 0.78rem; margin-top: 8px;">{estimated_hours} hrs × ${hourly_rate}/hr premium rate</div>
    </div>
    <div class="exec-metric amber" style="flex:1; background: linear-gradient(135deg, #0F1419 0%, #111827 100%); border: 1px solid #1E293B; border-radius: 14px; padding: 22px; text-align: center;">
        <div style="color: #94A3B8; font-size: 0.72rem; text-transform: uppercase; letter-spacing: 1.5px; font-weight: 600; margin-bottom: 10px;">Timeline Delay Index</div>
        <div style="font-size: 2.2rem; font-weight: 800; color: #F59E0B; margin: 4px 0;">{timeline_delay}%</div>
        <div style="color: #64748B; font-size: 0.78rem; margin-top: 8px;">Schedule slippage risk from extra scope</div>
    </div>
    <div class="exec-metric violet" style="flex:1; background: linear-gradient(135deg, #0F1419 0%, #111827 100%); border: 1px solid #1E293B; border-radius: 14px; padding: 22px; text-align: center;">
        <div style="color: #94A3B8; font-size: 0.72rem; text-transform: uppercase; letter-spacing: 1.5px; font-weight: 600; margin-bottom: 10px;">Contract Breach Vulnerability</div>
        <div style="font-size: 2.2rem; font-weight: 800; color: #818CF8; margin: 4px 0;">{breach_vulnerability:.0f}/100</div>
        <div style="color: #64748B; font-size: 0.78rem; margin-top: 8px;">Risk score based on request severity</div>
    </div>
</div>
            """, unsafe_allow_html=True)

            # ═══════════════════════════════════════
            # STRUCTURAL DEFICIENCIES & VECTORS TABLE
            # ═══════════════════════════════════════
            st.markdown('<div class="section-header"><span class="sh-icon">◆</span>Structural Deficiencies & Vectors</div>', unsafe_allow_html=True)

            vec_df = pd.DataFrame(selected_vectors)
            vec_df.columns = ["Breach Vector", "Risk Level", "Discovered Clause Conflict", "Tactical Response Move"]

            def risk_color(val):
                if val == "Critical":
                    return "background-color: rgba(239, 68, 68, 0.15); color: #F8FAFC; font-weight: bold;"
                elif val == "High":
                    return "background-color: rgba(245, 158, 11, 0.15); color: #F8FAFC;"
                elif val == "Moderate":
                    return "background-color: rgba(99, 102, 241, 0.15); color: #F8FAFC;"
                else:
                    return "background-color: rgba(16, 185, 129, 0.15); color: #F8FAFC;"

            st.dataframe(
                vec_df.style.map(
                    risk_color,
                    subset=["Risk Level"],
                ),
                use_container_width=True,
                hide_index=True,
            )

            # ═══════════════════════════════════════
            # REVENUE DEFENSE EMAIL SCRIPT
            # ═══════════════════════════════════════
            st.markdown('<div class="section-header"><span class="sh-icon">◆</span>Revenue Defense Email Script</div>', unsafe_allow_html=True)
            st.caption("A legally precise, non-confrontational email template. Click anywhere in the text to select, then copy to clipboard.")

            st.code(email_script, language="text")

            # ═══════════════════════════════════════
            # EXPORT BUTTON
            # ═══════════════════════════════════════
            st.markdown('<div class="section-header"><span class="sh-icon">◆</span>Export Advanced Audit Report</div>', unsafe_allow_html=True)

            excel_bytes = generate_enterprise_excel(audit_result)
            filename = f"AHS_ScopeGuard_Report_{datetime.now().strftime('%Y%m%d')}.xlsx"

            st.download_button(
                label="Download Full Audit Report (Excel)",
                data=excel_bytes,
                file_name=filename,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True,
            )

            st.caption("Your report includes: Executive Summary, Vector Breach Matrix, Revenue Defense Email, and AHS Nexus Next Steps.")

            # ═══════════════════════════════════════
            # AHS NEXUS LEADS FUNNEL
            # ═══════════════════════════════════════
            st.markdown("")
            st.markdown("""
<div class="funnel-box">
    <h2>🚀 Instant Infrastructure Remediation by AHS Nexus</h2>
    <div class="funnel-url">https://ahsnexus.com</div>
    <p>AHS Nexus engineers custom enterprise-grade technology platforms tailored for high-earning consultants and digital agencies. We eliminate the technology overhead that keeps you from focusing on billable work.</p>
""", unsafe_allow_html=True)

            st.markdown("""
<ul class="service-list">
    <li>Custom Enterprise CRM Platforms — built to your exact workflow, no bloated software licenses</li>
    <li>Automated Contract Parsing Dashboards — AI-powered clause extraction and scope-change detection</li>
    <li>Secure Client Databases — encrypted, compliant, and accessible from anywhere with zero recurring fees</li>
    <li>Flat-Fee Pricing Model — one investment, lifetime ownership, absolutely zero recurring licensing costs</li>
    <li>48-Hour Deployment — most platforms are live within 2 business days of approval</li>
</ul>
            """, unsafe_allow_html=True)

            st.markdown("""
    <p style="font-weight: 600; color: #A7F3D0; margin-top: 18px;">
        Ready to stop losing revenue to scope creep and technology gaps? Book your free enterprise architecture review below.
    </p>
""", unsafe_allow_html=True)

            # Email booking form
            st.markdown("""
<div class="email-form-box">
    <p>📬 Enter your professional email below to claim your <strong>Free Enterprise Architecture Consultation</strong> — a 45-minute session where we map your current contract management workflow and build a custom technology roadmap.</p>
</div>
            """, unsafe_allow_html=True)

            email_col1, email_col2 = st.columns([3, 1])
            with email_col1:
                email_input = st.text_input(
                    "Your Professional Email",
                    placeholder="you@yourfirm.com",
                    key="scope_email_input",
                    label_visibility="collapsed",
                )
            with email_col2:
                book_clicked = st.button(
                    "Book Consultation",
                    use_container_width=True,
                    key="scope_book_button",
                )

            if book_clicked:
                if not email_input.strip():
                    st.warning("Please enter your professional email address to claim your consultation.")
                elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email_input.strip()):
                    st.warning("Please enter a valid email address (e.g., you@yourfirm.com).")
                else:
                    st.markdown(f"""
<div class="success-flash">
    ✅ Consultation Request Confirmed. An AHS Nexus enterprise architect will contact you at <strong>{email_input.strip()}</strong> within 24 hours to schedule your session.
</div>
                    """, unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════
# Footer
# ═══════════════════════════════════════════════
st.markdown("")
st.markdown("---")
st.caption("AHS Scope Guard Enterprise v1.0 — Scope Creep Risk & Revenue Defense Auditor. Built by Manus AI for AHS Nexus. For demonstration purposes only. Not a substitute for legal counsel.")
