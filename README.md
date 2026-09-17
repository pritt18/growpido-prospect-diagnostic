# Growpido Executive Prospect Diagnostic Platform

**Advisory & Reputation Intelligence Engine for DIFC Founders, Fund Managers, and Family Offices**  
*A dual-pass fact verification, regulatory compliance gate, and narrative gap diagnostic system.*

---

## 1. Executive Summary

This platform implements an enterprise intelligence and verification pipeline designed specifically for executive advisory practices in and around the Dubai International Financial Centre (DIFC).

Starting from a public LinkedIn profile, the platform:
1. Researches the executive prospect across public domain records, statutory registries, and financial databases.
2. Executes a **Dual-Pass Fact Verification Pipeline**:
   - **Pass 1 (Primary Statutory Source)**: Corroborates claims against primary sources (DFSA Public Register, ADGM, NASDAQ Dubai, DED Commercial Register, official university registries).
   - **Pass 2 (Independent Cross-Check)**: Verifies consistency across secondary financial databases (Bloomberg, Reuters, TechCrunch, SEC, Tracxn) to catch discrepancies, numerical inflation, or temporal drift.
3. Classifies every claim into **Verified**, **Partially Verified**, or **Refused / Quarantined**.
4. Enforces Editorial House Rules programmatically:
   - **Zero Em Dashes** (`—`)
   - **Zero Hashtags** (`#`)
   - **Zero AI Filler Vocabulary** (blacklisting over 50 banned buzzwords like *delve*, *tapestry*, *pinnacle*, *game-changer*, *unwavering*)
   - **Zero Unsourced Numbers** (every statistic, date, currency amount, and percentage is anchored to an explicit primary citation)
5. Identifies the **Three Biggest Strategic Narrative Gaps** in how the subject currently shows up publicly, benchmarked against tier-1 global VC and sovereign capital allocator standards.
6. Integrates an interactive **Human Review Gate** requiring advisory sign-off before any diagnostic is compiled for client release.
7. Generates publication-grade executive deliverables: **One-Page Diagnostic** (Markdown and HTML) and a **Refused Claims Forensic Audit**.

---

## 2. Supported Executive Profiles

The system includes pre-indexed, audited statutory dossiers for top UAE figures alongside live custom profile ingestion:

- **Noor Sweid (Global Ventures / DIFC)**: Founding Managing Partner at Global Ventures, authorized under DFSA Firm Reference `F004381`. Demonstrates statutory verification against NASDAQ Dubai IPO filings and quarantine of unverified fund metrics.
- **Hosam Arab (Tabby / DIFC & Riyadh)**: Co-founder and CEO of Tabby, MENA's first fintech unicorn ($1.5B Series D valuation). Demonstrates cross-border sovereign narrative analysis and quarantine of unsubstantiated personal wealth claims.
- **Custom Profile Mode**: Ingests any public LinkedIn URL with strict unverified status flags and mandatory statutory verification gates.

---

## 3. Architecture & Verification Pipeline

```
[ Target LinkedIn URL / Public Profile ]
                   │
                   ▼
       [ Research Harvester ]
   (Audited Statutory Dossier +
     Graceful Web Scrape Fallback)
                   │
                   ▼
     [ Fact Integrity Engine ]
   ├── Pass 1: Primary Statutory Verification (DFSA / NASDAQ Dubai / DED)
   └── Pass 2: Independent Dual Cross-Check (TechCrunch / SEC / Bourses)
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
  [ Accepted Claims ]   [ Refused Claims Vault ]
  - Dual Verified       - Quarantined
  - Partially Verified  - Forensic Audit Logged
         │
         ▼
  [ Strategic Narrative Gap Analyzer ]
  (DIFC Institutional Benchmark Analysis)
         │
         ▼
  [ Human Review Gate ]
  (Advisory Oversight & Sign-off)
         │
         ▼
  [ House Rules Linter Gate ]
  (0 Em Dashes | 0 Hashtags | 0 AI Filler Words | 100% Sourced Numbers)
         │
         ▼
  [ Publication Outputs ]
  ├── 1. One-Page Executive Diagnostic (.md & .html)
  └── 2. Refused Claims Forensic Audit (.md)
```

---

## 4. How to Run in VS Code

### Quick Start (3 Steps)

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Launch the Interactive Web Dashboard:**
   ```bash
   streamlit run app.py
   ```
   *The application will open automatically in your browser at `http://localhost:8501`.*

3. **Or Run via Command Line (CLI):**
   ```bash
   python cli.py --subject "Noor Sweid" --url "https://www.linkedin.com/in/noor-sweid"
   ```

*(On Windows, you can also simply double-click `run.bat` to launch the platform).*

---

## 5. Summary of Deliverables

The engine generates publication outputs in the `output/` directory:

1. **`output/noor_sweid_one_page_diagnostic.md`**:  
   Clean, executive diagnostic strictly obeying house rules (0 em dashes, 0 hashtags, 0 AI filler words, 100% sourced metrics).
2. **`output/noor_sweid_one_page_diagnostic.html`**:  
   Print-ready HTML briefing document styled with DIFC dark navy and gold palette.
3. **`output/refused_claims_forensic_audit.md`**:  
   Compliance audit explaining why specific unverified metrics were quarantined.

---

## 6. Project Structure

```
growpido-prospect-diagnostic/
├── app.py                         # Interactive Streamlit terminal with Human Gate
├── cli.py                         # Standalone Command-Line Interface
├── run.bat                        # Windows one-click launcher
├── requirements.txt               # Runtime dependencies (Streamlit, Pydantic, Requests)
├── README.md                      # Platform documentation
├── data/
│   ├── noor_sweid_dossier.json    # Audited primary dossier for Noor Sweid
│   └── hosam_arab_dossier.json    # Audited primary dossier for Hosam Arab
├── engine/
│   ├── __init__.py
│   ├── models.py                  # Pydantic data schemas
│   ├── house_rules_linter.py      # Automated editorial house rules enforcer
│   ├── fact_integrity_engine.py   # Dual-pass verification & refusal engine
│   ├── research_harvester.py      # Data harvester with rate-limit fallback
│   ├── narrative_gap_analyzer.py  # DIFC-benchmarked narrative gap generator
│   └── compiler.py                # Executive diagnostic & HTML compiler
└── output/
    ├── noor_sweid_one_page_diagnostic.md
    ├── noor_sweid_one_page_diagnostic.html
    └── refused_claims_forensic_audit.md
```
