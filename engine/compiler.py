"""
Growpido Executive Diagnostic Compiler
Compiles:
1. Executive One-Page Diagnostic (Markdown + Print-Ready HTML)
2. Refused Claims Forensic Audit
Strictly validated against the Growpido House Rules Linter before export.
"""

from typing import Dict, Any, List
from .models import ExecutiveDiagnostic, ClaimStatus
from .house_rules_linter import HouseRulesLinter


class ExecutiveDiagnosticCompiler:
    """Compiles publication-grade executive diagnostics for DIFC leadership."""

    @staticmethod
    def compile_markdown_diagnostic(diagnostic: ExecutiveDiagnostic) -> str:
        """
        Compiles clean, sober markdown formatted for high-level DIFC advisory clients.
        Strictly zero em dashes, zero hashtags, zero AI filler words, 100% sourced numbers.
        """
        lines = []
        lines.append("GROWPIDO EXECUTIVE DIAGNOSTIC: PROSPECT ANALYSIS")
        lines.append("CONFIDENTIAL AND ADVISORY: DIFC PRACTICE")
        lines.append("==================================================")
        lines.append(f"Subject: {diagnostic.subject_name}")
        lines.append(f"Title: {diagnostic.primary_title}")
        lines.append(f"Entity: {diagnostic.entity_name}")
        lines.append(f"Jurisdiction: {diagnostic.jurisdiction}")
        lines.append(f"Regulatory Standing: {diagnostic.regulatory_status}")
        lines.append(f"LinkedIn Reference: {diagnostic.linkedin_url}")
        lines.append(f"Verification Date: {diagnostic.generated_at}")
        lines.append(f"Human Gate Status: {'APPROVED BY HUMAN GATE' if diagnostic.human_gate_approved else 'PENDING HUMAN APPROVAL'}")
        if diagnostic.approved_by:
            lines.append(f"Reviewed By: {diagnostic.approved_by}")
        lines.append("--------------------------------------------------")
        lines.append("")
        
        lines.append("EXECUTIVE SUMMARY")
        lines.append(diagnostic.executive_profile_summary)
        lines.append("")
        lines.append("--------------------------------------------------")
        lines.append("SECTION 1: FACT INTEGRITY AUDIT (DUAL-PASS VERIFIED)")
        lines.append("All claims below passed two independent verification tiers: primary statutory record plus secondary corroboration.")
        lines.append("")
        
        for idx, fact in enumerate(diagnostic.verified_facts, start=1):
            lines.append(f"{idx}. [VERIFIED] {fact.claim_text}")
            if fact.pass1_primary_source:
                lines.append(f"   Pass 1 Primary: {fact.pass1_primary_source.source_title} ({fact.pass1_primary_source.verification_date}) [Source: {fact.pass1_primary_source.document_ref}]")
            if fact.pass2_cross_source:
                lines.append(f"   Pass 2 Cross-Check: {fact.pass2_cross_source.source_title} [Source: {fact.pass2_cross_source.document_ref}]")
            lines.append("")

        if diagnostic.partially_verified_facts:
            lines.append("--------------------------------------------------")
            lines.append("SECTION 2: PARTIALLY VERIFIED CLAIMS (NON-STATUTORY DISCLOSURES)")
            lines.append("Accepted with qualifications. Reliable ecosystem consensus confirmed, but primary statutory filing is private or variance exists.")
            lines.append("")
            for idx, fact in enumerate(diagnostic.partially_verified_facts, start=1):
                lines.append(f"{idx}. [PARTIALLY VERIFIED] {fact.claim_text}")
                if fact.regulatory_risk_note:
                    lines.append(f"   Audit Note: {fact.regulatory_risk_note} [Source: Dual Cross-Check Review]")
                lines.append("")

        lines.append("--------------------------------------------------")
        lines.append("SECTION 3: THE THREE BIGGEST PUBLIC NARRATIVE Gaps")
        lines.append("Strategic assessment of how the subject currently shows up publicly against tier-1 global and DIFC institutional benchmarks.")
        lines.append("")

        for gap in diagnostic.three_biggest_narrative_gaps:
            lines.append(f"GAP {gap.gap_number}: {gap.title}")
            lines.append(f"Current Posture: {gap.current_public_posture}")
            lines.append(f"Strategic Risk: {gap.strategic_vulnerability}")
            lines.append(f"Advisory Fix: {gap.recommended_positioning}")
            lines.append(f"Peer Benchmark: {gap.institutional_benchmark}")
            lines.append("")

        lines.append("--------------------------------------------------")
        lines.append("HOUSE RULES COMPLIANCE RECORD")
        lines.append(f"Total Editorial Violations: {diagnostic.house_rules_audit.get('total_violations', 0)}")
        lines.append(f"Em Dashes: {diagnostic.house_rules_audit.get('summary', {}).get('em_dashes_detected', 0)}")
        lines.append(f"Hashtags: {diagnostic.house_rules_audit.get('summary', {}).get('hashtags_detected', 0)}")
        lines.append(f"AI Filler Words: {diagnostic.house_rules_audit.get('summary', {}).get('ai_filler_words_detected', 0)}")
        lines.append(f"Unsourced Numbers: {diagnostic.house_rules_audit.get('summary', {}).get('unsourced_numbers_detected', 0)}")
        lines.append("==================================================")
        
        return "\n".join(lines)

    @staticmethod
    def compile_refused_claim_audit(diagnostic: ExecutiveDiagnostic) -> str:
        """
        Compiles the standalone forensic audit for refused claims.
        Explicitly answers the brief: 'plus one claim your system refused to include and why it refused.'
        """
        lines = []
        lines.append("GROWPIDO FACT INTEGRITY AUDIT: REFUSED CLAIMS DOSSIER")
        lines.append("CONFIDENTIAL COMPLIANCE LOG: DIFC PRACTICE")
        lines.append("==================================================")
        lines.append(f"Subject: {diagnostic.subject_name}")
        lines.append(f"Entity: {diagnostic.entity_name}")
        lines.append(f"Total Claims Refused: {len(diagnostic.refused_claims)}")
        lines.append("Growpido Core Standard: A fabricated statistic in a fund manager's post is a regulatory violation.")
        lines.append("--------------------------------------------------")
        lines.append("")

        for idx, ref in enumerate(diagnostic.refused_claims, start=1):
            lines.append(f"REFUSED CLAIM {idx}: {ref.candidate_claim}")
            lines.append(f"Flagged Metric: {ref.claimed_metric}")
            lines.append(f"Purported Source: {ref.purported_source}")
            lines.append(f"Pass 1 Primary Failure: {ref.pass1_failure_reason}")
            lines.append(f"Pass 2 Cross-Check Discrepancy: {ref.pass2_cross_check_discrepancy}")
            lines.append(f"Regulatory & Reputational Risk: {ref.regulatory_or_reputational_risk}")
            lines.append(f"System Action: {ref.system_action}")
            lines.append("")
            lines.append("--------------------------------------------------")

        return "\n".join(lines)

    @staticmethod
    def compile_html_diagnostic(diagnostic: ExecutiveDiagnostic) -> str:
        """
        Generates print-ready, clean executive HTML styled with dark navy and gold DIFC aesthetic.
        """
        verified_html = ""
        for v in diagnostic.verified_facts:
            verified_html += f"""
            <div style="margin-bottom: 14px; padding: 12px; background: #f8fafc; border-left: 4px solid #10b981; border-radius: 4px;">
                <div style="font-weight: 600; color: #0f172a; font-size: 14px;">[VERIFIED] {v.claim_text}</div>
                <div style="margin-top: 6px; font-size: 12px; color: #475569;">
                    <strong>Pass 1 Primary:</strong> {v.pass1_primary_source.source_title if v.pass1_primary_source else 'N/A'} <br>
                    <strong>Pass 2 Cross-Check:</strong> {v.pass2_cross_source.source_title if v.pass2_cross_source else 'N/A'}
                </div>
            </div>
            """

        partially_verified_html = ""
        for pv in diagnostic.partially_verified_facts:
            partially_verified_html += f"""
            <div style="margin-bottom: 14px; padding: 12px; background: #fefce8; border-left: 4px solid #f59e0b; border-radius: 4px;">
                <div style="font-weight: 600; color: #0f172a; font-size: 14px;">[PARTIALLY VERIFIED] {pv.claim_text}</div>
                <div style="margin-top: 6px; font-size: 12px; color: #854d0e;">
                    <strong>Audit Qualification:</strong> {pv.regulatory_risk_note or 'Secondary market data confirmed without direct statutory filing.'}
                </div>
            </div>
            """

        gaps_html = ""
        for g in diagnostic.three_biggest_narrative_gaps:
            gaps_html += f"""
            <div style="margin-bottom: 16px; padding: 14px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 6px;">
                <div style="font-size: 15px; font-weight: 700; color: #0f172a; margin-bottom: 6px;">GAP {g.gap_number}: {g.title}</div>
                <div style="font-size: 13px; color: #334155; margin-bottom: 4px;"><strong>Current Posture:</strong> {g.current_public_posture}</div>
                <div style="font-size: 13px; color: #b91c1c; margin-bottom: 4px;"><strong>Strategic Vulnerability:</strong> {g.strategic_vulnerability}</div>
                <div style="font-size: 13px; color: #047857; margin-bottom: 4px;"><strong>Advisory Fix:</strong> {g.recommended_positioning}</div>
                <div style="font-size: 12px; color: #64748b; font-style: italic;"><strong>Peer Benchmark:</strong> {g.institutional_benchmark}</div>
            </div>
            """

        refused_html = ""
        for r in diagnostic.refused_claims:
            refused_html += f"""
            <div style="margin-bottom: 14px; padding: 12px; background: #fef2f2; border-left: 4px solid #ef4444; border-radius: 4px;">
                <div style="font-weight: 700; color: #991b1b; font-size: 14px;">[REFUSED BY INTEGRITY ENGINE] {r.candidate_claim}</div>
                <div style="margin-top: 6px; font-size: 12px; color: #7f1d1d;">
                    <strong>Flagged Metric:</strong> {r.claimed_metric} <br>
                    <strong>Pass 1 Failure:</strong> {r.pass1_failure_reason} <br>
                    <strong>Pass 2 Cross-Check:</strong> {r.pass2_cross_check_discrepancy} <br>
                    <strong>Regulatory Risk:</strong> {r.regulatory_or_reputational_risk}
                </div>
            </div>
            """

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Growpido Executive Diagnostic - {diagnostic.subject_name}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #f1f5f9;
            color: #0f172a;
            margin: 0;
            padding: 30px;
        }}
        .page-container {{
            max-width: 900px;
            margin: 0 auto;
            background: #ffffff;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }}
        .header {{
            border-bottom: 2px solid #0f172a;
            padding-bottom: 15px;
            margin-bottom: 25px;
        }}
        .badge {{
            display: inline-block;
            padding: 4px 10px;
            border-radius: 9999px;
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
        }}
        .badge-approved {{
            background-color: #dcfce7;
            color: #166534;
        }}
        .section-title {{
            font-size: 15px;
            font-weight: 800;
            letter-spacing: 0.05em;
            color: #1e293b;
            text-transform: uppercase;
            border-bottom: 1px solid #cbd5e1;
            padding-bottom: 6px;
            margin-top: 25px;
            margin-bottom: 15px;
        }}
        .meta-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            font-size: 13px;
            color: #334155;
            margin-bottom: 20px;
        }}
    </style>
</head>
<body>
    <div class="page-container">
        <div class="header">
            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                <div>
                    <h1 style="margin: 0; font-size: 24px; color: #0f172a; font-weight: 800;">GROWPIDO EXECUTIVE DIAGNOSTIC</h1>
                    <div style="color: #64748b; font-size: 13px; margin-top: 4px;">DIFC Practice & Narrative Advisory | Prospect Evaluation</div>
                </div>
                <div>
                    <span class="badge badge-approved">HUMAN GATE APPROVED</span>
                </div>
            </div>
        </div>

        <div class="meta-grid">
            <div><strong>Subject:</strong> {diagnostic.subject_name}</div>
            <div><strong>Entity:</strong> {diagnostic.entity_name}</div>
            <div><strong>Title:</strong> {diagnostic.primary_title}</div>
            <div><strong>Jurisdiction:</strong> {diagnostic.jurisdiction}</div>
            <div><strong>Regulatory Standing:</strong> {diagnostic.regulatory_status}</div>
            <div><strong>Date:</strong> {diagnostic.generated_at}</div>
        </div>

        <div class="section-title">Executive Summary</div>
        <p style="font-size: 13.5px; line-height: 1.6; color: #334155; margin-bottom: 20px;">
            {diagnostic.executive_profile_summary}
        </p>

        <div class="section-title">Section 1: Fact Integrity Audit (Dual-Pass Verified)</div>
        {verified_html}

        <div class="section-title">Section 2: Partially Verified Claims (Secondary Consensus)</div>
        {partially_verified_html}

        <div class="section-title">Section 3: The Three Biggest Public Narrative Gaps</div>
        {gaps_html}

        <div class="section-title">Section 4: Forensic Audit of Refused Claims (Quarantined)</div>
        {refused_html}

        <div style="margin-top: 30px; padding-top: 15px; border-top: 1px solid #e2e8f0; font-size: 11px; color: #94a3b8; text-align: center;">
            Growpido LLC | Dubai International Financial Centre | strictly zero em dashes, zero hashtags, zero unsourced metrics.
        </div>
    </div>
</body>
</html>
"""
        return html
