import markdown, subprocess, pathlib

css = pathlib.Path('style.css').read_text(encoding='utf-8')
md_text = pathlib.Path('figure-demo.md').read_text(encoding='utf-8')
html_body = markdown.markdown(md_text, extensions=['tables', 'fenced_code', 'extra'])
full_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
{css}
</style>
</head>
<body>
{html_body}
</body>
</html>"""

pathlib.Path('test.html').write_text(full_html, encoding='utf-8')
edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
html_url = pathlib.Path('test.html').resolve().as_uri()
pdf_path = pathlib.Path('test.pdf').resolve()
cmd = [edge, "--headless", "--disable-gpu", f"--print-to-pdf={pdf_path}", "--no-pdf-header-footer", html_url]
subprocess.run(cmd, check=True)
print("PDF generated successfully:", pdf_path.stat().st_size, "bytes")
