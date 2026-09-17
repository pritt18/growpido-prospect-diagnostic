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

    @staticmethod
    def get_hosam_arab_narrative_gaps() -> List[NarrativeGap]:
        return [
            NarrativeGap(
                gap_number=1,
                title="Consumer Lifestyle App Branding versus Institutional Financial Rail Positioning",
                current_public_posture="Public content and interviews skew heavily toward retail merchant additions, promotional shopping campaigns, and consumer convenience features.",
                strategic_vulnerability="Risks trapping the executive narrative in a retail shopping utility perception rather than positioning Tabby as a core sovereign financial payments infrastructure layer across the GCC.",
                recommended_positioning="Pivot public positioning toward institutional financial technology: proprietary credit scoring models, balance-sheet resilience, and banking system integration [Source: Growpido DIFC Practice Advisory Benchmark].",
                institutional_benchmark="Benchmarked against founders of Klarna and Adyen who transitioned their public voices from consumer checkout tools to systemic global banking infrastructure leaders."
            ),
            NarrativeGap(
                gap_number=2,
                title="Absence of Thought Leadership on Consumer Credit Quality and Macro Underwriting",
                current_public_posture="Maintains silence on macro debt cycles, delinquency management, and credit health during regional consumer spending shifts.",
                strategic_vulnerability="Leaves open questions among institutional debt providers and central bank regulators regarding risk mitigation in high-interest rate environments.",
                recommended_positioning="Publish transparent, data-backed insights on regional consumer repayment discipline and machine-learning risk modeling to establish regulatory gold standards.",
                institutional_benchmark="Benchmarked against tier-1 fintech executives who publish regular macro credit health indexes to build regulatory trust."
            ),
            NarrativeGap(
                gap_number=3,
                title="Undercommunicated UAE to Saudi Sovereign Bridge Narrative",
                current_public_posture="Mentions regional growth generically without unpacking the complex operational and regulatory nuances of scaling a dual-headquartered fintech between DIFC and Riyadh.",
                strategic_vulnerability="Misses the opportunity to be the definitive public case study on GCC cross-border regulatory passporting and dual-market dominance.",
                recommended_positioning="Author authoritative playbooks on navigating regulatory compliance between the UAE Central Bank and SAMA, positioning himself as the premier advisor on GCC cross-border enterprise scale.",
                institutional_benchmark="Benchmarked against prominent multinational financial executives who actively shape cross-border trade and regulatory corridor dialogues."
            )
        ]

    @classmethod
    def get_gaps_for_subject(cls, subject_name: str) -> List[NarrativeGap]:
        name_lower = subject_name.lower()
        if "hosam" in name_lower or "tabby" in name_lower:
            return cls.get_hosam_arab_narrative_gaps()
        elif "noor" in name_lower or "sweid" in name_lower or "global" in name_lower:
            return cls.get_noor_sweid_narrative_gaps()
        else:
            # High-level default institutional gaps
            return [
                NarrativeGap(
                    gap_number=1,
                    title="Promotional Surface Noise versus Sovereign LP Capital Alignment",
                    current_public_posture="General marketing announcements without rigorous capital allocation theses.",
                    strategic_vulnerability="Fails to engage institutional investors who seek underwriting discipline over social reach.",
                    recommended_positioning="Publish macroeconomic commentary on regional deployment and capital efficiency [Source: Growpido DIFC Advisory Benchmark].",
                    institutional_benchmark="Benchmarked against institutional partners at global alternative asset managers."
                ),
                NarrativeGap(
                    gap_number=2,
                    title="Absence of Realized Value Creation and Cash Flow Architecture",
                    current_public_posture="Discourse centers on top-line vanity metrics without addressing net cash returns.",
                    strategic_vulnerability="Creates skepticism among institutional allocators during macro tightening cycles.",
                    recommended_positioning="Frame executive voice around sustainable unit economics and proven liquidity mechanisms.",
                    institutional_benchmark="Benchmarked against tier-1 executive peers in mature financial hubs."
                ),
                NarrativeGap(
                    gap_number=3,
                    title="Underutilized Policy and Institutional Regulatory Authority",
                    current_public_posture="Passive compliance without active contribution to industry regulatory standards.",
                    strategic_vulnerability="Cedes high-value market framing to incumbent legacy operators.",
                    recommended_positioning="Lead public whitepaper discourse on regulatory evolution in the UAE and wider GCC.",
                    institutional_benchmark="Benchmarked against industry leaders actively consulted by financial authorities."
                )
            ]
