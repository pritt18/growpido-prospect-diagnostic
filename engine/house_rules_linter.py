"""
Growpido House Rules Linter
Strict enforcement of Growpido editorial guidelines:
1. No em dashes (—, \u2014, \u2015, or parenthetical '--')
2. No hashtags (#)
3. No AI filler vocabulary
4. No number published without an explicit source citation
"""

import re
from typing import List, Dict, Any


# Comprehensive blacklist of AI filler vocabulary and cliches (with inflections)
BANNED_AI_WORDS = [
    r"\bdelv(?:e|es|ed|ing)\b",
    r"\btapestr(?:y|ies)\b",
    r"\bvibrant\b",
    r"\bbeacons?\b",
    r"\bpinnacles?\b",
    r"\bgame[- ]chang(?:er|ers|ing)\b",
    r"\btestaments?\b",
    r"\bunwavering(?:ly)?\b",
    r"\belevat(?:e|es|ed|ing)\b",
    r"\bleverag(?:e|es|ed|ing)\b",
    r"\bspearhead(?:s|ed|ing)?\b",
    r"\btrailblaz(?:er|ers|ing)\b",
    r"\bsynerg(?:y|ies)\b",
    r"\bfoster(?:s|ed|ing)?\b",
    r"\bseamless(?:ly)?\b",
    r"\bcornerstones?\b",
    r"\btransformational\b",
    r"\btransformative\b",
    r"\bpivotal\b",
    r"\bparamount\b",
    r"\bin conclusion\b",
    r"\bembark(?:s|ed|ing)?\b",
    r"\bdynamic landscape\b",
    r"\bever[- ]evolving\b",
    r"\bbustling\b",
    r"\bpowerhouse\b",
    r"\bparadigm shifts?\b",
    r"\bholistic(?:ally)?\b",
    r"\bbespoke\b",
    r"\bquintessential\b",
    r"\bcatalysts?\b",
    r"\brealms?\b",
    r"\bunlock(?:s|ed|ing)?\b",
    r"\bunleash(?:es|ed|ing)?\b",
    r"\bnavigating the complexities\b",
    r"\bstands as a\b",
    r"\bserve as a\b",
    r"\bpoised to\b",
    r"\bharness(?:es|ed|ing)?\b",
    r"\bresonate(?:s|d|ing)?\b",
    r"\bdeep dive\b",
]

# Matches em dashes or word-level double dashes, excluding standalone markdown HR lines
EM_DASH_PATTERN = re.compile(r"[\u2014\u2015]|(?<=\S)\s*--\s*(?=\S)")
HASHTAG_PATTERN = re.compile(r"(?<!\S)#[A-Za-z0-9_]+")
NUMERIC_PATTERN = re.compile(r"(?<![A-Za-z0-9])(?:[\$€£]\s*)?\d+(?:,\d{3})*(?:\.\d+)?%?(?:\s*(?:million|billion|M|B|k|x))?(?![A-Za-z0-9])", re.IGNORECASE)
SOURCE_TAG_PATTERN = re.compile(r"\[(?:Source|Ref|Citation|DFSA|NASDAQ|Registry|Pass 1|Pass 2):[^\]]+\]", re.IGNORECASE)


class HouseRulesLinter:
    """Programmatic enforcer of Growpido House Rules."""

    @staticmethod
    def is_structural_line(line: str) -> bool:
        """Determines if a line is pure markdown formatting (horizontal rules, headers, dividers)."""
        stripped = line.strip()
        if not stripped:
            return True
        if set(stripped) <= {"-", "=", "_", "*"}:
            return True
        return False

    @classmethod
    def check_em_dashes(cls, text: str) -> List[Dict[str, Any]]:
        violations = []
        for line_num, line in enumerate(text.splitlines(), start=1):
            if cls.is_structural_line(line):
                continue
            matches = list(EM_DASH_PATTERN.finditer(line))
            for m in matches:
                violations.append({
                    "rule": "NO_EM_DASH",
                    "line": line_num,
                    "matched": m.group(),
                    "context": line.strip()
                })
        return violations

    @classmethod
    def check_hashtags(cls, text: str) -> List[Dict[str, Any]]:
        violations = []
        for line_num, line in enumerate(text.splitlines(), start=1):
            if cls.is_structural_line(line):
                continue
            matches = list(HASHTAG_PATTERN.finditer(line))
            for m in matches:
                violations.append({
                    "rule": "NO_HASHTAGS",
                    "line": line_num,
                    "matched": m.group(),
                    "context": line.strip()
                })
        return violations

    @classmethod
    def check_ai_filler(cls, text: str) -> List[Dict[str, Any]]:
        violations = []
        for line_num, line in enumerate(text.splitlines(), start=1):
            if cls.is_structural_line(line):
                continue
            for pattern_str in BANNED_AI_WORDS:
                pattern = re.compile(pattern_str, re.IGNORECASE)
                matches = list(pattern.finditer(line))
                for m in matches:
                    violations.append({
                        "rule": "NO_AI_FILLER",
                        "line": line_num,
                        "matched": m.group(),
                        "context": line.strip()
                    })
        return violations

    @classmethod
    def check_sourced_numbers(cls, text: str) -> List[Dict[str, Any]]:
        violations = []
        for line_num, line in enumerate(text.splitlines(), start=1):
            if cls.is_structural_line(line):
                continue
            stripped = line.strip()
            
            # Exempt headings, metadata key-value rows that define status or date, or summary counts
            if (
                stripped.startswith("#")
                or stripped.startswith("Subject:")
                or stripped.startswith("Verification Date:")
                or stripped.startswith("Date:")
                or stripped.startswith("House Rules")
                or stripped.startswith("Total Editorial Violations:")
                or stripped.startswith("Em Dashes:")
                or stripped.startswith("Hashtags:")
                or stripped.startswith("AI Filler Words:")
                or stripped.startswith("Unsourced Numbers:")
                or stripped.startswith("Total Claims Refused:")
            ):
                continue

            content_without_list_prefix = re.sub(r"^(?:GAP\s+\d+:|\d+\.\s+|SECTION\s+\d+:)", "", stripped, flags=re.IGNORECASE)
            numbers = list(NUMERIC_PATTERN.finditer(content_without_list_prefix))
            meaningful_numbers = [n for n in numbers if not (len(n.group()) == 1 and n.group() in "123456789")]
            
            if meaningful_numbers:
                if not SOURCE_TAG_PATTERN.search(line):
                    violations.append({
                        "rule": "NO_UNSOURCED_NUMBERS",
                        "line": line_num,
                        "numbers_found": [n.group() for n in meaningful_numbers],
                        "context": stripped
                    })
        return violations

    @classmethod
    def audit_document(cls, text: str) -> Dict[str, Any]:
        """Runs the complete suite of Growpido House Rule audits."""
        em_dash_violations = cls.check_em_dashes(text)
        hashtag_violations = cls.check_hashtags(text)
        ai_filler_violations = cls.check_ai_filler(text)
        unsourced_number_violations = cls.check_sourced_numbers(text)

        total_violations = (
            len(em_dash_violations)
            + len(hashtag_violations)
            + len(ai_filler_violations)
            + len(unsourced_number_violations)
        )

        return {
            "passed": total_violations == 0,
            "total_violations": total_violations,
            "summary": {
                "em_dashes_detected": len(em_dash_violations),
                "hashtags_detected": len(hashtag_violations),
                "ai_filler_words_detected": len(ai_filler_violations),
                "unsourced_numbers_detected": len(unsourced_number_violations),
            },
            "violations": {
                "em_dash": em_dash_violations,
                "hashtag": hashtag_violations,
                "ai_filler": ai_filler_violations,
                "unsourced_numbers": unsourced_number_violations,
            }
        }
