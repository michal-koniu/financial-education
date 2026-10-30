# course check

Structural checks for the courses in this repository:

- every relative link and `#anchor` resolves (GitHub heading slugs);
- tables have a header separator and equal column counts; code fences are closed;
- every chapter carries the "not financial advice" disclaimer;
- English and Polish chapters match: same number of headings (H1–H3), tables, mermaid diagrams and `<details>` blocks.

```bash
python3 tools/course-check/validate.py .
```

Standard library only. Exit code 0 means no problems.
