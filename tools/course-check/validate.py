"""Structural checks for the financial-education course (EN/PL parity, links, tables, disclaimers).

Usage: python3 validate.py <repo-root>
"""
import glob
import os
import re
import sys

from anchors import slugs

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
PAIRS = [("en/practical-macro-economy", "pl/praktyczna-makroekonomia")]
DISC = {"en": "not financial advice", "pl": "nie doradztwo finansowe"}
SEP = re.compile(r"^\s*\|[\s:|-]+\|\s*$")
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def cols(line):
    line = re.sub(r"\\\|", "", line.strip())
    line = re.sub(r"`[^`]*`", lambda m: m.group(0).replace("|", ""), line)
    return line.strip("|").count("|") + 1


def scan(path):
    text = open(path, encoding="utf-8").read()
    lines, errs = text.split("\n"), []
    heads, in_code, block = [0] * 7, False, None
    for i, line in enumerate(lines, 1):
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r"(#{1,6}) ", line)
        if m:
            heads[len(m.group(1))] += 1
        if line.lstrip().startswith("|"):
            if block is None:
                block = (i, cols(line))
                if i < len(lines) and not SEP.match(lines[i]):
                    errs.append(f"{path}:{i} table without header separator")
            elif cols(line) != block[1]:
                errs.append(f"{path}:{i} table has {cols(line)} columns, header has {block[1]}")
        else:
            block = None
    if in_code:
        errs.append(f"{path}: unclosed code fence")
    for m in LINK.finditer(text):
        url = m.group(1)
        if re.match(r"(https?:|mailto:)", url):
            continue
        target = os.path.normpath(os.path.join(os.path.dirname(path), url.split("#")[0])) if url.split("#")[0] else path
        if not os.path.exists(target):
            errs.append(f"{path}: broken link {url}")
        elif "#" in url and target.endswith(".md") and url.split("#", 1)[1] not in slugs(open(target, encoding="utf-8").read()):
            errs.append(f"{path}: broken anchor {url}")
    stats = {
        "headings": tuple(heads[1:4]),
        "mermaid": text.count("```mermaid"),
        "details": text.count("<details>"),
        "tables": sum(1 for i, l in enumerate(lines) if SEP.match(l)),
    }
    return text, errs, stats


def main():
    errors, words = [], {}
    for md in glob.glob(os.path.join(ROOT, "*.md")) + glob.glob(os.path.join(ROOT, "tools/**/*.md"), recursive=True):
        errors += scan(md)[1]
    for en_dir, pl_dir in PAIRS:
        en = sorted(glob.glob(os.path.join(ROOT, en_dir, "*.md")))
        pl = sorted(glob.glob(os.path.join(ROOT, pl_dir, "*.md")))
        if len(en) != len(pl):
            errors.append(f"file count differs: {en_dir}={len(en)} {pl_dir}={len(pl)}")
        for lang, files in (("en", en), ("pl", pl)):
            words[lang] = 0
            for f in files:
                text, errs, _ = scan(f)
                errors += errs
                words[lang] += len(text.split())
                base = os.path.basename(f)
                if base[:2].isdigit() and base[:2] not in ("00", "16") and DISC[lang] not in text.lower():
                    errors.append(f"{f}: missing disclaimer")
        num = lambda fs: {os.path.basename(f)[:2]: f for f in fs if os.path.basename(f)[:2].isdigit()}  # noqa: E731
        ne, npl = num(en), num(pl)
        for k in sorted(set(ne) | set(npl)):
            if k not in ne or k not in npl:
                errors.append(f"chapter {k} missing in one language")
                continue
            se, sp = scan(ne[k])[2], scan(npl[k])[2]
            for key in se:
                if se[key] != sp[key]:
                    errors.append(f"chapter {k}: {key} EN={se[key]} PL={sp[key]}")
    print(f"words EN={words.get('en')} PL={words.get('pl')}")
    print(f"{len(errors)} problem(s)")
    for e in errors:
        print(" -", e)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
