# Growpido Prospect to Diagnostic Engine (Track B)

**Advisory & Reputation Engine for DIFC Founders, Fund Managers, and Family Offices**  
Built for the Growpido LLC AI & Automation Engineer Build Task (September 2026).

---

## 1. Executive Summary

This repository implements **Track B: Prospect to Diagnostic**, an intelligence and verification pipeline designed specifically for Growpido's reputation practice in and around the Dubai International Financial Centre (DIFC).

Starting from a public LinkedIn profile, the engine:
1. Researches the executive prospect across public domain records, statutory registries, and financial databases.
2. Executes a **Dual-Pass Fact Verification Pipeline**:
   - **Pass 1 (Primary Statutory Source)**: Corroborates claims against primary sources (DFSA Public Register, ADGM, NASDAQ Dubai, DED Commercial Register, official university registries).
   - **Pass 2 (Independent Cross-Check)**: Verifies consistency across secondary financial databases (Bloomberg, Reuters, TechCrunch, SEC, Tracxn) to catch discrepancies, numerical inflation, or temporal drift.
3. Classifies every claim into **Verified**, **Partially Verified**, or **Refused / Quarantined**.
4. Enforces Growpido House Rules programmatically:
   - **Zero Em Dashes** (`—`)
   - **Zero Hashtags** (`#`)
   - **Zero AI Filler Vocabulary** (blacklisting over 50 banned buzzwords like *delve*, *tapestry*, *pinnacle*, *game-changer*, *unwavering*)
   - **Zero Unsourced Numbers** (every statistic, date, currency amount, and percentage is anchored to a primary citation)
5. Identifies the **Three Biggest Strategic Narrative Gaps** in how the subject currently shows up publicly, benchmarked against tier-1 global VC and sovereign capital allocator standards.
6. Integrates a **Human Review Gate** that requires explicit advisory sign-off before any diagnostic is compiled for client release.
7. Generates an executive-grade **One-Page Diagnostic** and a **Refused Claims Compliance Audit**.

---

## 2. Subject Selection: Noor Sweid (Managing Partner, Global Ventures)

We selected **Noor Sweid**, Founder and Managing Partner of **Global Ventures**, based in the Dubai International Financial Centre (DIFC).

### Why This Subject Tests the Engine:
- **DIFC ICP Alignment**: Global Ventures is regulated by the Dubai Financial Services Authority (DFSA Reference: `F004381`).
- **High-Stakes Regulatory Context**: As noted in Growpido's brief: *"A fabricated statistic in a fund manager's post is not a typo. It is a regulatory problem and a client we lose."* DFSA Conduct of Business rules strictly regulate financial promotions, making unverified AUM or return metrics illegal.
- **Rich Public Record with Secondary Distortion**: The internet contains numerous conflicting claims regarding her track record (e.g., conflating Cedarbridge Capital with Fitness First, inflating fund AUM to $500M, or claiming unverified 10x net DPI multiples). This provided the ideal testing ground for the engine's refusal quarantine.

---

## 3. Architecture & Verification Pipeline

```
[ LinkedIn URL / Executive Target ]
                 │
                 ▼
     [ Research Harvester ]
   (Audited Statutory Dossier +
    Live Scrape / Web Fallback)
                 │
                 ▼
   [ Fact Integrity Engine ]
   ├── Pass 1: Primary Statutory Source (DFSA / NASDAQ / DED)
   └── Pass 2: Independent Dual Cross-Check (Financial Press / Bourses)
                 │
       ┌─────────┴─────────┐
       ▼                   ▼
[ Accepted Claims ]   [ Refused Claims Vault ]
- Verified (Dual OK)  - Quarantined
- Partially Verified  - Forensic Audit Logged
       │
       ▼
[ Strategic Narrative Gap Analyzer ]
(DIFC Institutional Benchmark Analysis)
       │
       ▼
[ Human Review Gate ]
(Advisor Oversight & Sign-off)
       │
       ▼
[ House Rules Linter Gate ]
(Regex validation: 0 em dashes, 0 hashtags, 0 AI filler, 100% sourced numbers)
       │
       ▼
[ Compiler & Deliverables ]
├── One-Page Executive Diagnostic (.md & .html)
└── Refused Claims Forensic Audit (.md)
```

---

## 4. How to Run

### Prerequisites
- Python 3.10+ (tested on Python 3.11.9)
- Dependencies installed via `pip install -r requirements.txt`

### Option A: Run All Automated Tests
```bash
python -m pytest tests/
```
*Executes 6 unit and integration tests verifying house rules linting, dual-pass verification, refusal mechanics, and document compliance.*

### Option B: Run via Command Line Interface (CLI)
```bash
python cli.py --subject "Noor Sweid" --url "https://www.linkedin.com/in/noorsweid"
```
*Harvests records, executes dual-pass verification, runs the linter, and outputs files to `/output`.*

### Option C: Launch the Interactive Streamlit Terminal
```bash
streamlit run app.py
```
*Launches the DIFC Advisory Terminal UI with interactive human review gate, live claim verification receipts, refusal vault, and one-click diagnostic downloads.*

### Option D: One-Click Windows Runner
Double-click `run.bat` to run tests, execute the CLI, and launch the dashboard in sequence.

---

## 5. Summary of Outputs

The engine generates three primary deliverables in the `output/` directory:

1. **`output/noor_sweid_one_page_diagnostic.md`**:  
   The clean, publication-grade executive diagnostic. Meets all house rules (0 em dashes, 0 hashtags, 0 AI filler words, 100% sourced metrics).
2. **`output/noor_sweid_one_page_diagnostic.html`**:  
   Print-ready HTML document styled with DIFC dark navy and gold palette.
3. **`output/refused_claims_forensic_audit.md`**:  
   Detailed breakdown of the claims the system refused to include, complete with failure reasons, cross-check discrepancies, and regulatory risk assessments.

---

## 6. The Refused Claim Example

In compliance with the Track B brief (*"plus one claim your system refused to include and why it refused"*):

### Refused Claim:
> *"Global Ventures currently manages over $500 million in cumulative assets under management (AUM) and has returned a net 10x realized cash distribution multiple to early fund investors."*

### Why the System Refused It:
1. **Pass 1 Failure (Primary Statutory Source)**:  
   The DFSA Public Register of Authorised Firms (Ref: `F004381`) verifies that Global Ventures Management Limited is licensed for collective investment fund management and advisory, but the DFSA does not publish private fund AUM or returns. No audited public statutory filing exists for a $500 million figure.
2. **Pass 2 Discrepancy (Dual Cross-Check)**:  
   Cross-checking against SEC Form D filings and verified venture reporting (TechCrunch) reveals:
   - Fund I target: $50 million (closed at ~$40 million)
   - Fund II target: $100 million
   - Fund III target: $150 million  
   The cumulative target across all three core funds is $300 million. The $500 million claim represents an unverified 66% inflation, and the 10x net DPI claim lacks any audited backing.
3. **Regulatory & Reputational Liability**:  
   Under Chapter 3 of the DFSA Conduct of Business (COB) Rulebook, financial promotions by authorised persons must be clear, fair, and not misleading. Publishing unverified AUM and return multiples exposes the firm to regulatory enforcement from the DFSA and damages credibility during institutional LP diligence.

---

## 7. Project Structure

```
growpido-prospect-diagnostic/
├── app.py                         # Interactive Streamlit terminal with Human Gate
├── cli.py                         # Command-line interface
├── run.bat                        # One-click Windows launcher
├── requirements.txt               # Dependencies
├── README.md                      # Project documentation
├── SUBMISSION.md                  # Complete submission reply for Growpido
├── data/
│   └── noor_sweid_dossier.json    # Audited primary dossier & candidate claims
├── engine/
│   ├── __init__.py
│   ├── models.py                  # Pydantic data schemas
│   ├── house_rules_linter.py      # House rules enforcer
│   ├── fact_integrity_engine.py   # Dual-pass verification & refusal engine
│   ├── research_harvester.py      # Data harvester with rate-limit fallback
│   ├── narrative_gap_analyzer.py  # DIFC-benchmarked narrative gap generator
│   └── compiler.py                # Executive diagnostic & HTML compiler
├── output/
│   ├── noor_sweid_one_page_diagnostic.md
│   ├── noor_sweid_one_page_diagnostic.html
│   └── refused_claims_forensic_audit.md
└── tests/
    ├── __init__.py
    └── test_engine.py             # 6 automated tests
```
