"""GitHub-style heading slugs shared by validate.py and remap_anchors.py."""
import re


def headings(text):
    """Return [(level, title)] for Markdown ATX headings outside code fences."""
    out, in_code = [], False
    for line in text.split("\n"):
        if line.startswith("```"):
            in_code = not in_code
            continue
        if not in_code:
            m = re.match(r"(#{1,6}) +(.*?)\s*#*\s*$", line)
            if m:
                out.append((len(m.group(1)), m.group(2)))
    return out


def slug(title):
    t = re.sub(r"<[^>]+>", "", title)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)  # links -> text
    t = t.replace("`", "").replace("*", "").strip().lower()
    t = re.sub(r"[^\w\- ]", "", t)  # keep unicode letters, digits, _, -, space
    return t.replace(" ", "-")


def slugs(text):
    seen, out = {}, []
    for _, title in headings(text):
        s = slug(title)
        n = seen.get(s, 0)
        out.append(s if n == 0 else f"{s}-{n}")
        seen[s] = n + 1
    return out
