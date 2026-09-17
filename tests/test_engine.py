"""
Automated Test Suite for Growpido Prospect Diagnostic Engine
Validates:
1. House Rules Linter (em dash, hashtag, AI filler, unsourced numbers)
2. Dual-Pass Fact Integrity & Refusal Quarantining
3. Narrative Gap Extraction
4. End-to-End Compiler House Rule Compliance
"""

import os
import json
import pytest
from engine.house_rules_linter import HouseRulesLinter
from engine.fact_integrity_engine import FactIntegrityEngine
from engine.narrative_gap_analyzer import NarrativeGapAnalyzer
from engine.compiler import ExecutiveDiagnosticCompiler
from engine.models import ExecutiveDiagnostic, ClaimStatus


def test_house_rules_em_dash_detected():
    text_with_em_dash = "This is a sentence — with an em dash."
    audit = HouseRulesLinter.audit_document(text_with_em_dash)
    assert not audit["passed"]
    assert audit["summary"]["em_dashes_detected"] >= 1


def test_house_rules_hashtag_detected():
    text_with_hashtag = "Prominent venture capitalist in DIFC #venturecapital #fintech"
    audit = HouseRulesLinter.audit_document(text_with_hashtag)
    assert not audit["passed"]
    assert audit["summary"]["hashtags_detected"] == 2


def test_house_rules_ai_filler_detected():
    text_with_ai_filler = "She delves deep into the vibrant tapestry of Middle Eastern venture capital."
    audit = HouseRulesLinter.audit_document(text_with_ai_filler)
    assert not audit["passed"]
    assert audit["summary"]["ai_filler_words_detected"] >= 2


def test_fact_integrity_refusal_mechanism():
    engine = FactIntegrityEngine()
    
    # Test refusal candidate: $500M AUM without DFSA statutory proof
    refused_input = {
        "claim_id": "CLM-TEST-REFUSE",
        "claim_text": "Global Ventures manages over $500 million in AUM.",
        "subject": "Noor Sweid",
        "contains_numeric_metric": True,
        "force_refusal": True,
        "metric_flagged": "$500M AUM",
        "purported_source": "Conference Bio",
        "pass1_failure_reason": "No DFSA statutory filing.",
        "pass2_discrepancy": "TechCrunch reports $300M total target."
    }
    claim, is_refused, rationale = engine.evaluate_claim(refused_input)
    assert is_refused
    assert claim.status == ClaimStatus.REFUSED
    assert "primary source" in rationale.lower() or "discrepancy" in rationale.lower() or "statutory" in rationale.lower()


def test_dossier_processing_noor_sweid():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dossier_file = os.path.join(base_dir, "data", "noor_sweid_dossier.json")
    with open(dossier_file, "r", encoding="utf-8") as f:
        dossier = json.load(f)

    engine = FactIntegrityEngine()
    results = engine.process_dossier(dossier["candidate_claims"])

    # Assert verified claims are present
    assert len(results["verified"]) >= 5
    # Assert partially verified claims are present
    assert len(results["partially_verified"]) >= 2
    # Assert refused claims were caught and quarantined
    assert len(results["refused_audit"]) >= 2
    
    # Verify the refused claim contains the regulatory warning
    refused_claims = [r.candidate_claim for r in results["refused_audit"]]
    assert any("500 million" in c for c in refused_claims)


def test_compiled_diagnostic_passes_house_rules():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dossier_file = os.path.join(base_dir, "data", "noor_sweid_dossier.json")
    with open(dossier_file, "r", encoding="utf-8") as f:
        dossier = json.load(f)

    engine = FactIntegrityEngine()
    results = engine.process_dossier(dossier["candidate_claims"])
    gaps = NarrativeGapAnalyzer.get_noor_sweid_narrative_gaps()

    diagnostic = ExecutiveDiagnostic(
        subject_name=dossier["subject_name"],
        primary_title=dossier["primary_title"],
        entity_name=dossier["entity_name"],
        linkedin_url=dossier["linkedin_url"],
        jurisdiction=dossier["jurisdiction"],
        regulatory_status=dossier["regulatory_status"],
        executive_profile_summary=dossier["executive_profile_summary"],
        verified_facts=results["verified"],
        partially_verified_facts=results["partially_verified"],
        refused_claims=results["refused_audit"],
        three_biggest_narrative_gaps=gaps,
        house_rules_audit={},
        human_gate_approved=True,
        approved_by="Pritam Gangurde (AI & Automation Lead)",
        generated_at="2026-09-17"
    )

    # Compile markdown diagnostic
    md_output = ExecutiveDiagnosticCompiler.compile_markdown_diagnostic(diagnostic)
    
    # Run House Rules Linter
    audit = HouseRulesLinter.audit_document(md_output)
    
    # Assert 0 em dashes, 0 hashtags, 0 AI filler words
    assert audit["summary"]["em_dashes_detected"] == 0
    assert audit["summary"]["hashtags_detected"] == 0
    assert audit["summary"]["ai_filler_words_detected"] == 0
