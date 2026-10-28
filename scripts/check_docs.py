"""Consistency checks for the framework. Runs in CI on every push.

1. Every relative link in every Markdown file points to a file (and heading) that exists.
2. The AI register CSV parses, and its columns match the field names in the intake form.
3. Register values stick to the allowed vocabularies used in the framework.
4. No em dashes (house style).
5. The training log CSV has the agreed columns and values.
6. Every Danish template in templates/da has an English counterpart, and links to it from the Danish index.

Run locally:  python scripts/check_docs.py
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []

ALLOWED = {
    "our_role": {"deployer", "provider"},
    "personal_data": {"yes", "no"},
    "oversight_level": {"1", "2", "3", "4", "5"},
    "eu_ai_act_tier": {"prohibited", "high", "limited", "minimal", "out_of_scope"},
    "governance_intensity": {"light", "standard", "enhanced", "strict", "redesign", "stop"},
    "dpia_required": {"yes", "no"},
    "fria_required": {"yes", "no"},
    "status": {"idea", "intake", "assessment", "live", "retired"},
}


def slugify(heading: str) -> str:
    """GitHub-style anchor for a heading."""
    s = heading.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    return re.sub(r"\s", "-", s)


def anchors(md: Path) -> set[str]:
    text = md.read_text(encoding="utf-8")
    return {slugify(m.group(1)) for m in re.finditer(r"^#{1,6}\s+(.+)$", text, re.M)}


def check_links() -> None:
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        text = md.read_text(encoding="utf-8")
        text = re.sub(r"```.*?```", "", text, flags=re.S)  # ignore code blocks
        for target in re.findall(r"\]\(([^)\s]+)\)", text):
            if re.match(r"^(https?:|mailto:)", target):
                continue
            path, _, anchor = target.partition("#")
            dest = md if not path else (md.parent / path).resolve()
            rel = md.relative_to(ROOT)
            if not dest.exists():
                errors.append(f"{rel}: broken link -> {target}")
                continue
            if anchor and dest.suffix == ".md" and anchor not in anchors(dest):
                errors.append(f"{rel}: missing heading #{anchor} in {path or md.name}")


def check_register() -> None:
    reg = ROOT / "templates" / "ai-register.csv"
    with reg.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
        columns = list(rows[0].keys()) if rows else []

    intake = (ROOT / "templates" / "use-case-intake.md").read_text(encoding="utf-8")
    intake_fields = re.findall(r"^\|\s*\*\*([a-z_]+)\*\*\s*\|", intake, re.M)
    missing = [f for f in intake_fields if f not in columns]
    extra = [c for c in columns if c not in intake_fields]
    if missing:
        errors.append(f"ai-register.csv lacks intake fields: {missing}")
    if extra:
        errors.append(f"ai-register.csv has columns not in the intake form: {extra}")

    for i, row in enumerate(rows, start=2):
        if None in row:
            errors.append(f"ai-register.csv line {i}: too many values")
        for col, allowed in ALLOWED.items():
            value = (row.get(col) or "").strip()
            if value and value not in allowed:
                errors.append(f"ai-register.csv line {i}: {col}='{value}' not in {sorted(allowed)}")


def check_style() -> None:
    for f in list(ROOT.rglob("*.md")) + list(ROOT.rglob("*.csv")):
        if ".git" in f.parts:
            continue
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if "—" in line:
                errors.append(f"{f.relative_to(ROOT)}:{n}: em dash, use a hyphen or rewrite")


TRAINING_COLUMNS = ["entry_id", "learner_group", "audience", "people", "module", "use_case_id",
                    "delivered_on", "delivered_by", "format", "evidence", "next_refresh"]
LEARNER_GROUPS = {"all_staff", "frequent_user", "overseer", "management", "governance"}

# Danish template -> English counterpart
DANISH = {
    "ai-politik.md": "ai-policy.md",
    "brug-af-ai.md": "acceptable-use.md",
    "ai-raad-kommissorium.md": "ai-council-charter.md",
    "ai-anmodning.md": "use-case-intake.md",
    "beslutningsvej.md": "intake-decision.md",
    "ai-faerdighedsplan.md": "ai-literacy-plan.md",
}


def check_training_log() -> None:
    log = ROOT / "templates" / "training-log.csv"
    with log.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        rows = list(reader)
        if reader.fieldnames != TRAINING_COLUMNS:
            errors.append(f"training-log.csv columns {reader.fieldnames} != {TRAINING_COLUMNS}")
    for i, row in enumerate(rows, start=2):
        if None in row:
            errors.append(f"training-log.csv line {i}: too many values")
        group = (row.get("learner_group") or "").strip()
        if group not in LEARNER_GROUPS:
            errors.append(f"training-log.csv line {i}: learner_group='{group}' not in {sorted(LEARNER_GROUPS)}")
        for col in ("delivered_on", "next_refresh"):
            value = (row.get(col) or "").strip()
            if value and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
                errors.append(f"training-log.csv line {i}: {col}='{value}' is not YYYY-MM-DD")


def check_danish() -> None:
    da = ROOT / "templates" / "da"
    index = (da / "README.md").read_text(encoding="utf-8")
    for f in sorted(da.glob("*.md")):
        if f.name == "README.md":
            continue
        en = DANISH.get(f.name)
        if not en:
            errors.append(f"templates/da/{f.name}: no English counterpart listed in check_docs.DANISH")
        elif not (ROOT / "templates" / en).exists():
            errors.append(f"templates/da/{f.name}: English counterpart {en} is missing")
        if f"]({f.name})" not in index:
            errors.append(f"templates/da/README.md does not link {f.name}")
    for da_name in DANISH:
        if not (da / da_name).exists():
            errors.append(f"templates/da/{da_name} is listed but missing")


check_links()
check_register()
check_style()
check_training_log()
check_danish()

if errors:
    print("\n".join(errors))
    print(f"\n{len(errors)} problem(s) found")
    sys.exit(1)
print("All checks passed")
