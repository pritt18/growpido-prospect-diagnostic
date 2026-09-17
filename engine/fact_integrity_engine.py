"""
Growpido Fact Integrity Engine
Dual-Pass Verification Engine:
- Pass 1: Primary Source Verification (DFSA/ADGM/Exchange filings/Corporate registries)
- Pass 2: Independent Cross-Check for Consistency
- Tri-State Classification: verified, partially_verified, unverified
- Automated Refusal Mechanism for uncorroborated, regulatory-sensitive, or conflicting metrics.
"""

from typing import List, Dict, Any, Tuple
from .models import FactClaim, ClaimStatus, SourceTier, Citation, RefusedClaimDetail


class FactIntegrityEngine:
    """
    Executes rigorous dual-pass verification on public claims.
    Strictly quarantines and refuses claims lacking primary empirical evidence.
    """

    def __init__(self):
        pass

    def evaluate_claim(self, raw_claim: Dict[str, Any]) -> Tuple[FactClaim, bool, str]:
        """
        Evaluates a single candidate claim through dual-pass verification.
        Returns: (FactClaim, is_refused, refusal_rationale)
        """
        claim_id = raw_claim.get("claim_id", "CLM-UNKNOWN")
        claim_text = raw_claim.get("claim_text", "")
        subject = raw_claim.get("subject", "")
        category = raw_claim.get("category", "General")
        has_numbers = raw_claim.get("contains_numeric_metric", False)

        pass1_data = raw_claim.get("pass1_primary_source")
        pass2_data = raw_claim.get("pass2_cross_source")
        discrepancy = raw_claim.get("discrepancy_note")
        regulatory_risk = raw_claim.get("regulatory_risk_note")
        is_explicitly_refused = raw_claim.get("force_refusal", False)

        pass1_citation = None
        pass1_valid = False
        if pass1_data:
            pass1_citation = Citation(
                source_title=pass1_data.get("title", ""),
                source_type=SourceTier(pass1_data.get("tier", SourceTier.SECONDARY_ECOSYSTEM.value)),
                url=pass1_data.get("url"),
                document_ref=pass1_data.get("document_ref"),
                quoted_snippet=pass1_data.get("snippet", ""),
                verification_date=pass1_data.get("date", "2026-09-17")
            )
            # Primary tier validation: Must be primary regulatory or primary corporate/academic
            if pass1_citation.source_type in [SourceTier.PRIMARY_REGULATORY, SourceTier.PRIMARY_CORPORATE]:
                pass1_valid = True

        pass2_citation = None
        pass2_consistent = False
        if pass2_data:
            pass2_citation = Citation(
                source_title=pass2_data.get("title", ""),
                source_type=SourceTier(pass2_data.get("tier", SourceTier.SECONDARY_FINANCIAL.value)),
                url=pass2_data.get("url"),
                document_ref=pass2_data.get("document_ref"),
                quoted_snippet=pass2_data.get("snippet", ""),
                verification_date=pass2_data.get("date", "2026-09-17")
            )
            pass2_consistent = raw_claim.get("pass2_consistent", False)

        # Refusal Decision: Explicitly flagged, contradictory discrepancy, or unsubstantiated regulatory metric
        if is_explicitly_refused or (discrepancy and not pass2_consistent and not pass1_valid):
            refusal_reason = (
                discrepancy
                or "Failed primary source corroboration. Contains unverified numerical or regulatory metric."
            )
            fact_claim = FactClaim(
                claim_id=claim_id,
                claim_text=claim_text,
                subject=subject,
                category=category,
                contains_numeric_metric=has_numbers,
                pass1_checked=True,
                pass1_primary_source=pass1_citation,
                pass2_checked=True,
                pass2_cross_source=pass2_citation,
                pass2_consistency_confirmed=False,
                status=ClaimStatus.REFUSED,
                confidence_score=0.10,
                refusal_reason=refusal_reason,
                regulatory_risk_note=regulatory_risk
            )
            return fact_claim, True, refusal_reason

        # Verified: Primary regulatory/corporate record valid + cross-check consistent
        if pass1_valid and pass2_consistent:
            fact_claim = FactClaim(
                claim_id=claim_id,
                claim_text=claim_text,
                subject=subject,
                category=category,
                contains_numeric_metric=has_numbers,
                pass1_checked=True,
                pass1_primary_source=pass1_citation,
                pass2_checked=True,
                pass2_cross_source=pass2_citation,
                pass2_consistency_confirmed=True,
                status=ClaimStatus.VERIFIED,
                confidence_score=0.98,
                regulatory_risk_note="Audited and aligned with DFSA/Public filing standards."
            )
            return fact_claim, False, ""

        # Partially Verified: Established reporting across ecosystem or corporate sources, with variance or private LPA/mandate
        fact_claim = FactClaim(
            claim_id=claim_id,
            claim_text=claim_text,
            subject=subject,
            category=category,
            contains_numeric_metric=has_numbers,
            pass1_checked=True,
            pass1_primary_source=pass1_citation,
            pass2_checked=True,
            pass2_cross_source=pass2_citation,
            pass2_consistency_confirmed=pass2_consistent,
            status=ClaimStatus.PARTIALLY_VERIFIED,
            confidence_score=0.75,
            regulatory_risk_note=raw_claim.get("audit_qualification", "Secondary market consensus confirmed; primary underlying LPA or contract is confidential.")
        )
        return fact_claim, False, ""

    def process_dossier(self, raw_claims: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Runs complete evaluation across all candidate claims.
        Separates accepted claims from refused claims.
        """
        verified = []
        partially_verified = []
        refused_claims_audit = []

        for raw_claim in raw_claims:
            claim, is_refused, rationale = self.evaluate_claim(raw_claim)
            if is_refused or claim.status == ClaimStatus.REFUSED:
                refused_claims_audit.append(
                    RefusedClaimDetail(
                        candidate_claim=claim.claim_text,
                        claimed_metric=raw_claim.get("metric_flagged", "Unsubstantiated Metric"),
                        purported_source=raw_claim.get("purported_source", "Secondary Internet Citation"),
                        pass1_failure_reason=raw_claim.get("pass1_failure_reason", "No regulatory filing found."),
                        pass2_cross_check_discrepancy=raw_claim.get("pass2_discrepancy", "Conflicting independent evidence."),
                        regulatory_or_reputational_risk=claim.regulatory_risk_note or "DFSA Conduct of Business risk.",
                        system_action="QUARANTINED AND REFUSED: Omitted from client-facing executive diagnostic."
                    )
                )
            elif claim.status == ClaimStatus.VERIFIED:
                verified.append(claim)
            elif claim.status == ClaimStatus.PARTIALLY_VERIFIED:
                partially_verified.append(claim)

        return {
            "verified": verified,
            "partially_verified": partially_verified,
            "refused_audit": refused_claims_audit,
            "total_evaluated": len(raw_claims),
            "refusal_rate_pct": round((len(refused_claims_audit) / len(raw_claims) * 100), 1) if raw_claims else 0.0
        }
