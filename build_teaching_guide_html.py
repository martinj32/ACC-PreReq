"""
Regenerate docs/instructor/teaching-guide.html from teaching-guide.md.

Reuses the existing standalone-document CSS template (everything up to <body>)
and replaces the body with the freshly converted Markdown. Idempotent: the
<head>/<style> block is preserved across runs. Rerun whenever the .md changes.

    python build_teaching_guide_html.py
"""
import os
import markdown

HERE = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(HERE, "docs", "instructor", "teaching-guide.md")
HTML = os.path.join(HERE, "docs", "instructor", "teaching-guide.html")


def main():
    with open(MD, encoding="utf-8") as f:
        md_text = f.read()

    body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "sane_lists", "attr_list", "toc"],
    )

    # Preserve the existing <head>/<style> template: take everything up to <body>.
    with open(HTML, encoding="utf-8") as f:
        existing = f.read()

    marker = "<body>"
    idx = existing.find(marker)
    if idx == -1:
        raise SystemExit("Could not find <body> in existing teaching-guide.html template")
    head = existing[: idx + len(marker)]

    out = f"{head}\n\n{body}\n\n</body>\n</html>\n"

    with open(HTML, "w", encoding="utf-8") as f:
        f.write(out)

    print(f"Wrote {HTML}")
    print(f"Body length: {len(body)} chars")


if __name__ == "__main__":
    main()
