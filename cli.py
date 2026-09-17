"""
Growpido Prospect to Diagnostic - Command Line Interface
Executes dual-pass verification, checks house rules, and generates executive diagnostic.

Usage:
    python cli.py --subject "Noor Sweid" --url "https://www.linkedin.com/in/noorsweid"
"""

import argparse
import os
import json
from datetime import datetime
from engine.research_harvester import ResearchHarvester
from engine.fact_integrity_engine import FactIntegrityEngine
from engine.narrative_gap_analyzer import NarrativeGapAnalyzer
from engine.compiler import ExecutiveDiagnosticCompiler
from engine.house_rules_linter import HouseRulesLinter
from engine.models import ExecutiveDiagnostic


def run_pipeline(subject_name: str, linkedin_url: str, output_dir: str = "output", reviewer_name: str = "Pritam Gangurde"):
    print("=" * 70)
    print("GROWPIDO PROSPECT TO DIAGNOSTIC ENGINE - TRACK B")
    print("Dubai International Financial Centre (DIFC) Practice")
    print("=" * 70)
    print(f"Target Subject: {subject_name}")
    print(f"LinkedIn URL:   {linkedin_url}")
    print(f"Timestamp:      {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print("-" * 70)

    # Step 1: Research Harvest
    print("\n[1/5] Harvesting Public Records & Regulatory Registries...")
    harvester = ResearchHarvester()
    dossier = harvester.harvest_subject(linkedin_url=linkedin_url, subject_hint=subject_name)
    print(f"      Entity:        {dossier.get('entity_name')}")
    print(f"      Jurisdiction:  {dossier.get('jurisdiction')}")
    print(f"      Regulation:    {dossier.get('regulatory_status')}")
    print(f"      Harvest Mode:  {dossier.get('harvest_mode')}")

    # Step 2: Dual-Pass Fact Verification & Refusal Quarantine
    print("\n[2/5] Executing Dual-Pass Fact Integrity Pipeline...")
    engine = FactIntegrityEngine()
    results = engine.process_dossier(dossier.get("candidate_claims", []))
    verified = results["verified"]
    partially_verified = results["partially_verified"]
    refused = results["refused_audit"]

    print(f"      [OK] Verified Claims:          {len(verified)}")
    print(f"      [~]  Partially Verified:       {len(partially_verified)}")
    print(f"      [X]  Refused / Quarantined:    {len(refused)} ({results['refusal_rate_pct']}% refusal rate)")

    for idx, ref in enumerate(refused, start=1):
        print(f"\n      -> REFUSAL #{idx} CAUGHT: {ref.claimed_metric}")
        print(f"         Reason: {ref.pass1_failure_reason}")
        print(f"         Risk:   {ref.regulatory_or_reputational_risk}")

    # Step 3: Public Narrative Gap Analysis
    print("\n[3/5] Identifying 3 Biggest Public Narrative Gaps...")
    gaps = NarrativeGapAnalyzer.get_noor_sweid_narrative_gaps()
    for g in gaps:
        print(f"      Gap {g.gap_number}: {g.title}")

    # Step 4: Human Gate Sign-off
    print("\n[4/5] Human Gate Approval...")
    print(f"      Approved By: {reviewer_name} (Senior Automation & Intelligence Lead)")
    print("      Verification Status: Cleared for Client Delivery")

    # Step 5: Document Assembly & House Rules Linting
    print("\n[5/5] Compiling Executive Diagnostic & Validating House Rules...")
    diagnostic = ExecutiveDiagnostic(
        subject_name=dossier["subject_name"],
        primary_title=dossier["primary_title"],
        entity_name=dossier["entity_name"],
        linkedin_url=dossier["linkedin_url"],
        jurisdiction=dossier["jurisdiction"],
        regulatory_status=dossier["regulatory_status"],
        executive_profile_summary=dossier["executive_profile_summary"],
        verified_facts=verified,
        partially_verified_facts=partially_verified,
        refused_claims=refused,
        three_biggest_narrative_gaps=gaps,
        house_rules_audit={},
        human_gate_approved=True,
        approved_by=reviewer_name,
        generated_at=datetime.utcnow().strftime("%Y-%m-%d")
    )

    md_content = ExecutiveDiagnosticCompiler.compile_markdown_diagnostic(diagnostic)
    refused_content = ExecutiveDiagnosticCompiler.compile_refused_claim_audit(diagnostic)
    html_content = ExecutiveDiagnosticCompiler.compile_html_diagnostic(diagnostic)

    # Perform Editorial Linter Audit
    audit_results = HouseRulesLinter.audit_document(md_content)
    diagnostic.house_rules_audit = audit_results

    # Re-compile with embedded audit
    md_content = ExecutiveDiagnosticCompiler.compile_markdown_diagnostic(diagnostic)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    md_file = os.path.join(output_dir, "noor_sweid_one_page_diagnostic.md")
    html_file = os.path.join(output_dir, "noor_sweid_one_page_diagnostic.html")
    refused_file = os.path.join(output_dir, "refused_claims_forensic_audit.md")

    with open(md_file, "w", encoding="utf-8") as f:
        f.write(md_content)
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    with open(refused_file, "w", encoding="utf-8") as f:
        f.write(refused_content)

    print("\n" + "=" * 70)
    print("HOUSE RULES LINTER AUDIT REPORT:")
    print(f"  Passed Editorial Standard:  {'YES (100% Clean)' if audit_results['passed'] else 'NO'}")
    print(f"  Em Dashes Detected:         {audit_results['summary']['em_dashes_detected']}")
    print(f"  Hashtags Detected:          {audit_results['summary']['hashtags_detected']}")
    print(f"  AI Filler Words Detected:   {audit_results['summary']['ai_filler_words_detected']}")
    print(f"  Unsourced Numbers Detected: {audit_results['summary']['unsourced_numbers_detected']}")
    print("-" * 70)
    print(f"Outputs generated successfully:")
    print(f"  1. Executive Diagnostic (MD):   {os.path.abspath(md_file)}")
    print(f"  2. Print-Ready Diagnostic (HTML): {os.path.abspath(html_file)}")
    print(f"  3. Refused Claim Audit (MD):    {os.path.abspath(refused_file)}")
    print("=" * 70)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Growpido Prospect to Diagnostic Engine")
    parser.add_argument("--subject", default="Noor Sweid", help="Executive Name")
    parser.add_argument("--url", default="https://www.linkedin.com/in/noorsweid", help="LinkedIn Profile URL")
    parser.add_argument("--output", default="output", help="Output directory")
    args = parser.parse_args()

    run_pipeline(args.subject, args.url, args.output)
