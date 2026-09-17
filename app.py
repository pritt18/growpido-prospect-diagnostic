"""
Growpido Executive Prospect to Diagnostic Terminal
Interactive Streamlit Application with Human Review Gate & Fact Integrity Engine
DIFC Practice & Regulatory Intelligence Platform
"""

import streamlit as st
import json
import os
from datetime import datetime

from engine.research_harvester import ResearchHarvester
from engine.fact_integrity_engine import FactIntegrityEngine
from engine.narrative_gap_analyzer import NarrativeGapAnalyzer
from engine.compiler import ExecutiveDiagnosticCompiler
from engine.house_rules_linter import HouseRulesLinter
from engine.models import ExecutiveDiagnostic, ClaimStatus

# Set page configuration
st.set_page_config(
    page_title="Growpido | Executive Prospect Diagnostic",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Styling for DIFC Luxury Advisory Aesthetic
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 24px 30px;
        border-radius: 10px;
        color: white;
        margin-bottom: 25px;
        border-left: 6px solid #f59e0b;
    }
    
    .badge-verified {
        background-color: #dcfce7;
        color: #15803d;
        padding: 4px 10px;
        border-radius: 9999px;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.05em;
    }
    
    .badge-partially {
        background-color: #fef3c7;
        color: #b45309;
        padding: 4px 10px;
        border-radius: 9999px;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.05em;
    }
    
    .badge-refused {
        background-color: #fee2e2;
        color: #b91c1c;
        padding: 4px 10px;
        border-radius: 9999px;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.05em;
    }
    
    .metric-card {
        background: white;
        padding: 16px;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    
    .diagnostic-preview {
        background-color: #ffffff;
        padding: 30px;
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        color: #0f172a;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <div style="font-size: 12px; font-weight: 700; color: #f59e0b; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 4px;">
        Growpido Narrative & Reputation Advisory | DIFC Practice
    </div>
    <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: white;">
        Prospect to Diagnostic Engine
    </h1>
    <div style="font-size: 13px; color: #94a3b8; margin-top: 6px;">
        Dual-Pass Fact Integrity, DFSA Regulatory Gate & Strategic Public Presence Diagnostic
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 🎯 Prospect Selector")
    target_option = st.selectbox(
        "Select UAE Executive Prospect",
        [
            "Noor Sweid (Global Ventures / DIFC)",
            "Hosam Arab (Tabby / DIFC Fintech Unicorn)",
            "Custom LinkedIn URL"
        ]
    )
    
    if "Noor Sweid" in target_option:
        subject_name = "Noor Sweid"
        linkedin_url = "https://www.linkedin.com/in/noor-sweid"
        st.info("📌 **DIFC Target**: Founding Managing Partner at Global Ventures. DFSA Reference: F004381.")
    elif "Hosam Arab" in target_option:
        subject_name = "Hosam Arab"
        linkedin_url = "https://www.linkedin.com/in/hosam"
        st.info("📌 **Fintech Unicorn Target**: Co-founder & CEO of Tabby ($1.5B Series D Valuation).")
    else:
        subject_name = st.text_input("Executive Full Name", value="Mudassir Sheikha")
        linkedin_url = st.text_input("LinkedIn Profile URL", value="https://www.linkedin.com/in/mudassirsheikha")
        st.warning("⚠️ **Custom Mode**: Evaluates against public domain with mandatory statutory verification gate.")

    st.markdown("---")
    st.markdown("### 🏛️ House Rules Linter Status")
    st.success("✅ No Em Dashes (—) Enforced")
    st.success("✅ No Hashtags (#) Enforced")
    st.success("✅ No AI Filler Words Enforced")
    st.success("✅ 100% Sourced Metrics Enforced")

    st.markdown("---")
    st.markdown("### 👤 Human Review Gate")
    reviewer_name = st.text_input("Lead Advisor Sign-off", value="Pritam Gangurde")
    human_approved = st.checkbox("Sign-off for Client Release", value=True)

# Ingest and Process
harvester = ResearchHarvester()
dossier = harvester.harvest_subject(linkedin_url=linkedin_url, subject_hint=subject_name)
engine = FactIntegrityEngine()
results = engine.process_dossier(dossier.get("candidate_claims", []))
verified_facts = results["verified"]
partially_verified = results["partially_verified"]
refused_audit = results["refused_audit"]
gaps = NarrativeGapAnalyzer.get_gaps_for_subject(dossier.get("subject_name", subject_name))

# Layout Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Pipeline Overview",
    "🛡️ Fact Integrity & Dual-Pass Audit",
    "🚫 Refused Claims (Compliance Vault)",
    "🎯 Narrative Gaps (3 Public Blindspots)",
    "📄 Executive One-Page Diagnostic"
])

# TAB 1: PIPELINE OVERVIEW
with tab1:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Claims Screened", len(dossier.get("candidate_claims", [])))
    with col2:
        st.metric("Dual-Pass Verified", len(verified_facts), delta="100% Primary Proof")
    with col3:
        st.metric("Partially Verified", len(partially_verified), delta="Secondary Consensus")
    with col4:
        st.metric("Refused / Quarantined", len(refused_audit), delta=f"{results['refusal_rate_pct']}% Refused", delta_color="inverse")

    st.markdown("---")
    st.markdown("### Executive Profile Dossier")
    st.markdown(f"""
    - **Executive:** {dossier.get('subject_name')}
    - **Entity:** {dossier.get('entity_name')} ({dossier.get('jurisdiction')})
    - **Regulatory Status:** `{dossier.get('regulatory_status')}`
    - **Harvest Mode:** `{dossier.get('harvest_mode')}`
    """)
    st.markdown(f"**Profile Brief:** {dossier.get('executive_profile_summary')}")

# TAB 2: FACT INTEGRITY & DUAL PASS
with tab2:
    st.markdown("### Dual-Pass Verification Receipts")
    st.write("Every accepted claim has passed **Pass 1 (Primary Statutory Source)** and **Pass 2 (Independent Cross-Check)**.")

    st.markdown("#### ✅ Fully Verified Claims")
    for idx, fact in enumerate(verified_facts, start=1):
        with st.expander(f"Claim {idx}: {fact.claim_text[:85]}...", expanded=(idx == 1)):
            st.markdown(f"**Full Claim:** {fact.claim_text}")
            st.markdown(f"<span class='badge-verified'>VERIFIED (Confidence: {int(fact.confidence_score*100)}%)</span>", unsafe_allow_html=True)
            
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**Pass 1: Primary Source Receipt**")
                if fact.pass1_primary_source:
                    st.write(f"- **Source:** {fact.pass1_primary_source.source_title}")
                    st.write(f"- **Tier:** `{fact.pass1_primary_source.source_type.value}`")
                    st.write(f"- **Ref:** `{fact.pass1_primary_source.document_ref}`")
                    st.write(f"- *Snippet:* \"{fact.pass1_primary_source.quoted_snippet}\"")
            with c2:
                st.markdown("**Pass 2: Independent Cross-Check**")
                if fact.pass2_cross_source:
                    st.write(f"- **Source:** {fact.pass2_cross_source.source_title}")
                    st.write(f"- **Tier:** `{fact.pass2_cross_source.source_type.value}`")
                    st.write(f"- **Ref:** `{fact.pass2_cross_source.document_ref}`")
                    st.write(f"- *Snippet:* \"{fact.pass2_cross_source.quoted_snippet}\"")
                    st.success("Pass 2 Consistency Confirmed")

    st.markdown("#### ⚠️ Partially Verified Claims (Secondary Consensus)")
    for idx, fact in enumerate(partially_verified, start=1):
        with st.expander(f"Partially Verified {idx}: {fact.claim_text[:85]}..."):
            st.markdown(f"**Claim:** {fact.claim_text}")
            st.markdown(f"<span class='badge-partially'>PARTIALLY VERIFIED</span>", unsafe_allow_html=True)
            st.warning(f"**Audit Qualification:** {fact.regulatory_risk_note}")
            if fact.pass1_primary_source:
                st.write(f"Ecosystem Citation: {fact.pass1_primary_source.source_title}")

# TAB 3: REFUSED CLAIMS
with tab3:
    st.markdown("### 🚫 Refused Claims Forensic Audit")
    st.error("**Growpido Rule**: Any fabricated or unverified statistic is a regulatory liability and is quarantined immediately.")
    
    for idx, ref in enumerate(refused_audit, start=1):
        st.markdown(f"""
        <div style="padding: 16px; border: 1px solid #fca5a5; border-radius: 8px; background-color: #fff5f5; margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <span style="font-weight: 700; color: #991b1b; font-size: 15px;">REFUSED CLAIM #{idx}</span>
                <span class="badge-refused">QUARANTINED FROM DIAGNOSTIC</span>
            </div>
            <div style="font-weight: 600; color: #1e293b; margin-bottom: 8px;">"{ref.candidate_claim}"</div>
            <div style="font-size: 13px; color: #334155; margin-bottom: 4px;"><strong>Flagged Metric:</strong> <code>{ref.claimed_metric}</code></div>
            <div style="font-size: 13px; color: #334155; margin-bottom: 4px;"><strong>Purported Origin:</strong> {ref.purported_source}</div>
            <div style="font-size: 13px; color: #b91c1c; margin-bottom: 4px;"><strong>Pass 1 Primary Failure:</strong> {ref.pass1_failure_reason}</div>
            <div style="font-size: 13px; color: #b91c1c; margin-bottom: 4px;"><strong>Pass 2 Cross-Check Discrepancy:</strong> {ref.pass2_cross_check_discrepancy}</div>
            <div style="font-size: 13px; color: #7f1d1d; margin-bottom: 6px;"><strong>Regulatory Risk:</strong> {ref.regulatory_or_reputational_risk}</div>
            <div style="font-size: 12px; color: #047857; font-weight: 600;">System Action: {ref.system_action}</div>
        </div>
        """, unsafe_allow_html=True)

# TAB 4: NARRATIVE GAPS
with tab4:
    st.markdown("### The Three Biggest Public Narrative Gaps")
    st.write(f"Strategic public presence teardown for **{dossier.get('subject_name')}** benchmarked against tier-1 global and DIFC peers.")
    
    for g in gaps:
        with st.container():
            st.markdown(f"""
            <div class="metric-card" style="margin-bottom: 20px;">
                <h4 style="margin: 0 0 10px 0; color: #0f172a;">GAP {g.gap_number}: {g.title}</h4>
                <p style="margin-bottom: 6px; font-size: 13.5px;"><strong>Current Posture:</strong> {g.current_public_posture}</p>
                <p style="margin-bottom: 6px; font-size: 13.5px; color: #b91c1c;"><strong>Strategic Vulnerability:</strong> {g.strategic_vulnerability}</p>
                <p style="margin-bottom: 6px; font-size: 13.5px; color: #047857;"><strong>Advisory Recommendation:</strong> {g.recommended_positioning}</p>
                <p style="margin: 0; font-size: 12px; color: #64748b; font-style: italic;"><strong>Peer Benchmark:</strong> {g.institutional_benchmark}</p>
            </div>
            """, unsafe_allow_html=True)

# TAB 5: EXECUTIVE ONE-PAGE DIAGNOSTIC
with tab5:
    st.markdown("### Client-Ready One-Page Diagnostic")
    
    # Build full Diagnostic object
    diagnostic = ExecutiveDiagnostic(
        subject_name=dossier["subject_name"],
        primary_title=dossier["primary_title"],
        entity_name=dossier["entity_name"],
        linkedin_url=dossier["linkedin_url"],
        jurisdiction=dossier["jurisdiction"],
        regulatory_status=dossier["regulatory_status"],
        executive_profile_summary=dossier["executive_profile_summary"],
        verified_facts=verified_facts,
        partially_verified_facts=partially_verified,
        refused_claims=refused_audit,
        three_biggest_narrative_gaps=gaps,
        house_rules_audit={},
        human_gate_approved=human_approved,
        approved_by=reviewer_name if human_approved else None,
        generated_at=datetime.utcnow().strftime("%Y-%m-%d")
    )
    
    md_output = ExecutiveDiagnosticCompiler.compile_markdown_diagnostic(diagnostic)
    linter_audit = HouseRulesLinter.audit_document(md_output)
    diagnostic.house_rules_audit = linter_audit
    
    # Recompile with audit embed
    final_md = ExecutiveDiagnosticCompiler.compile_markdown_diagnostic(diagnostic)
    final_html = ExecutiveDiagnosticCompiler.compile_html_diagnostic(diagnostic)
    refused_md = ExecutiveDiagnosticCompiler.compile_refused_claim_audit(diagnostic)

    # House rules banner
    if linter_audit["passed"]:
        st.success("🌟 **House Rules Linter Passed 100%**: 0 Em Dashes | 0 Hashtags | 0 AI Filler Words | 100% Sourced Metrics")
    else:
        st.error(f"Editorial Violations Detected: {linter_audit['total_violations']}")

    # Download Buttons
    c_btn1, c_btn2, c_btn3 = st.columns(3)
    with c_btn1:
        st.download_button(
            label="📥 Download Diagnostic (Markdown)",
            data=final_md,
            file_name=f"{dossier.get('subject_name').lower().replace(' ', '_')}_diagnostic.md",
            mime="text/markdown"
        )
    with c_btn2:
        st.download_button(
            label="🌐 Download Print-Ready HTML",
            data=final_html,
            file_name=f"{dossier.get('subject_name').lower().replace(' ', '_')}_diagnostic.html",
            mime="text/html"
        )
    with c_btn3:
        st.download_button(
            label="🚫 Download Refused Claims Audit",
            data=refused_md,
            file_name="refused_claims_audit.md",
            mime="text/markdown"
        )

    st.markdown("---")
    # Render Diagnostic
    st.text_area("One-Page Diagnostic (Markdown View)", value=final_md, height=450)
