"""
Growpido Narrative Gap Analyzer
Identifies the three biggest strategic narrative vulnerabilities in an executive's public presence.
Benchmarked against tier-1 institutional standards for DIFC/GCC founders and fund managers.
"""

from typing import List
from .models import NarrativeGap


class NarrativeGapAnalyzer:
    """Analyzes executive public presence to isolate top 3 strategic narrative gaps."""

    @staticmethod
    def get_noor_sweid_narrative_gaps() -> List[NarrativeGap]:
        return [
            NarrativeGap(
                gap_number=1,
                title="The Founder Cheerleader Trap versus Institutional Capital Allocator Authority",
                current_public_posture="High volume of celebratory portfolio announcements (seed and Series A funding rounds, portfolio honours) and conference photo galleries across LinkedIn.",
                strategic_vulnerability="Speaks primarily to early-stage founders rather than institutional LPs, sovereign wealth funds, and regional family offices that allocate major eight-figure institutional commitments and demand disciplined underwriting theses.",
                recommended_positioning="Reallocate a significant share of public commentary toward rigorous institutional macro perspectives: GCC capital deployment discipline, valuation multiples across emerging markets, and cross-border syndication mechanics [Source: Growpido DIFC Practice Advisory Benchmark].",
                institutional_benchmark="Benchmarked against General Partners at Index Ventures and Bessemer who anchor their public presence in macroeconomic capital allocation rather than portfolio celebration."
            ),
            NarrativeGap(
                gap_number=2,
                title="Absence of Realized Exit Architecture and Secondary Liquidity Playbooks",
                current_public_posture="Public discourse concentrates entirely on capital deployment, portfolio scaling, and markups, with near total silence on DPI (Distributed to Paid-In capital) and exit execution.",
                strategic_vulnerability="In an era where regional LPs demand liquidity over paper valuations, avoiding the liquidity conversation invites unspoken skepticism regarding fund distribution capabilities.",
                recommended_positioning="Directly deploy her rare operational pedigree as the executive who executed the Depa IPO on NASDAQ Dubai to lead the public industry discourse on regional M&A, secondary sales, and local bourse listings on ADX and DFM.",
                institutional_benchmark="Benchmarked against tier-1 Silicon Valley and European venture firms that proactively publish liquidity frameworks and M&A teardowns during venture downturns."
            ),
            NarrativeGap(
                gap_number=3,
                title="Underleveraged DIFC and Sovereign Financial Policy Leadership",
                current_public_posture="Focuses predominantly on general entrepreneurship advocacy, without authoritative technical commentary on GCC regulatory evolution or cross-border fund passporting.",
                strategic_vulnerability="Failing to draw upon her dual standing as a DFSA-regulated fund manager and former Dubai Future Foundation CIO cedes high-value financial regulatory discourse to Big 4 consultancies.",
                recommended_positioning="Publish point-of-view policy teardowns on UAE-KSA regulatory harmonization, digital asset compliance, and cross-border fund passporting, establishing her as the primary private sector interlocutor for sovereign policymakers.",
                institutional_benchmark="Benchmarked against leading London and Singapore fund principals who actively author consultation whitepapers and position their firms at the nexus of regulation and capital."
            )
        ]
