"""
Growpido Prospect Diagnostic Engine - Data Models
Strict data schemas for fact verification, house rule enforcement, and executive diagnostic generation.
"""

from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class ClaimStatus(str, Enum):
    VERIFIED = "verified"
    PARTIALLY_VERIFIED = "partially_verified"
    UNVERIFIED = "unverified"
    REFUSED = "refused"


class SourceTier(str, Enum):
    PRIMARY_REGULATORY = "primary_regulatory"       # DFSA, ADGM, NASDAQ Dubai, official stock filings, government registries
    PRIMARY_CORPORATE = "primary_corporate"         # Company audited reports, official press releases, university registries
    SECONDARY_FINANCIAL = "secondary_financial"     # Bloomberg, Reuters, Financial Times, Forbes Middle East
    SECONDARY_ECOSYSTEM = "secondary_ecosystem"     # Wamda, TechCrunch MENA, conference bios, Tracxn
    UNVERIFIED_WEB = "unverified_web"               # Unattributed blog posts, social media claims, hearsay


class Citation(BaseModel):
    source_title: str
    source_type: SourceTier
    url: Optional[str] = None
    document_ref: Optional[str] = None
    quoted_snippet: str
    verification_date: str


class FactClaim(BaseModel):
    claim_id: str
    claim_text: str
    subject: str
    category: str                                   # e.g., "M&A / IPO", "AUM / Fund Size", "Education", "Governance"
    contains_numeric_metric: bool = False
    
    # Pass 1: Primary Source Verification
    pass1_checked: bool = False
    pass1_primary_source: Optional[Citation] = None
    
    # Pass 2: Independent Cross-Check
    pass2_checked: bool = False
    pass2_cross_source: Optional[Citation] = None
    pass2_consistency_confirmed: bool = False
    
    # Verdict
    status: ClaimStatus
    confidence_score: float = Field(default=0.0, ge=0.0, le=1.0)
    
    # Refusal & Audit details
    refusal_reason: Optional[str] = None
    regulatory_risk_note: Optional[str] = None
    human_override: bool = False
    human_notes: Optional[str] = None


class NarrativeGap(BaseModel):
    gap_number: int
    title: str
    current_public_posture: str
    strategic_vulnerability: str
    recommended_positioning: str
    institutional_benchmark: str


class RefusedClaimDetail(BaseModel):
    candidate_claim: str
    claimed_metric: str
    purported_source: str
    pass1_failure_reason: str
    pass2_cross_check_discrepancy: str
    regulatory_or_reputational_risk: str
    system_action: str


class ExecutiveDiagnostic(BaseModel):
    subject_name: str
    primary_title: str
    entity_name: str
    linkedin_url: str
    jurisdiction: str                               # e.g., "DIFC, Dubai, UAE"
    regulatory_status: str                          # e.g., "DFSA Authorised Firm Reference: F004381"
    
    executive_profile_summary: str
    verified_facts: List[FactClaim]
    partially_verified_facts: List[FactClaim]
    refused_claims: List[RefusedClaimDetail]
    three_biggest_narrative_gaps: List[NarrativeGap]
    
    house_rules_audit: Dict[str, Any]
    human_gate_approved: bool = False
    approved_by: Optional[str] = None
    generated_at: str
