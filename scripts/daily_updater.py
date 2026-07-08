import os
import re
import sys
import subprocess
from datetime import datetime

# HTML template with beautiful styling
html_template = """<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        @page {{
            size: A4;
            margin: 20mm;
        }}
        
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            color: #2d3748;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #ffffff;
        }}
        
        .header {{
            border-bottom: 3px solid #7dc26f;
            padding-bottom: 15px;
            margin-bottom: 25px;
        }}
        
        .brand {{
            color: #1f3453;
            font-size: 14px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            margin-bottom: 5px;
        }}
        
        h1 {{
            color: #1f3453;
            font-size: 26px;
            font-weight: 700;
            margin-top: 0;
            margin-bottom: 10px;
        }}
        
        .meta {{
            font-size: 13px;
            color: #718096;
            display: flex;
            justify-content: space-between;
            margin-bottom: 15px;
        }}
        
        .badge {{
            background-color: #1f3453;
            color: #ffffff;
            padding: 3px 8px;
            border-radius: 4px;
            font-weight: 600;
            font-size: 11px;
        }}
        
        h2 {{
            color: #1f3453;
            font-size: 18px;
            font-weight: 600;
            border-left: 4px solid #7dc26f;
            padding-left: 10px;
            margin-top: 30px;
            margin-bottom: 15px;
        }}
        
        h3 {{
            color: #1f3453;
            font-size: 15px;
            font-weight: 600;
            margin-top: 20px;
            margin-bottom: 10px;
        }}
        
        p {{
            margin-top: 0;
            margin-bottom: 15px;
            font-size: 14px;
            text-align: justify;
        }}
        
        ul, ol {{
            margin-top: 0;
            margin-bottom: 15px;
            padding-left: 20px;
            font-size: 14px;
        }}
        
        li {{
            margin-bottom: 8px;
        }}
        
        .highlight-box {{
            background-color: #f7fafc;
            border: 1px solid #e2e8f0;
            border-left: 4px solid #1f3453;
            padding: 15px;
            border-radius: 4px;
            margin: 20px 0;
        }}
        
        .highlight-box p:last-child {{
            margin-bottom: 0;
        }}
        
        .comparison-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 13px;
        }}
        
        .comparison-table th, .comparison-table td {{
            border: 1px solid #e2e8f0;
            padding: 10px;
            text-align: left;
        }}
        
        .comparison-table th {{
            background-color: #1f3453;
            color: #ffffff;
            font-weight: 600;
        }}
        
        .comparison-table tr:nth-child(even) {{
            background-color: #f7fafc;
        }}
        
        .footer {{
            margin-top: 50px;
            border-top: 1px solid #e2e8f0;
            padding-top: 15px;
            font-size: 12px;
            color: #718096;
            text-align: center;
        }}
        
        .page-break {{
            page-break-before: always;
        }}
        
        .code {{
            font-family: 'Courier New', Courier, monospace;
            background-color: #edf2f7;
            padding: 2px 5px;
            border-radius: 3px;
            font-size: 13px;
        }}
    </style>
</head>
<body>
    <div class="header">
        <div class="brand">ClinApp PQC Study Series</div>
        <h1>{headline}</h1>
        <div class="meta">
            <div><strong>Day {day}</strong> | Category: {category}</div>
            <div>Date: {date} | <span class="badge">DAILY MONITORING</span></div>
        </div>
    </div>

    {content}

    <div class="footer">
        ClinApp Post-Quantum Cryptography Daily Study Guide • Created Autonomously for Paulo Cauca
    </div>
</body>
</html>
"""

def update_repo(day_str, date_str, topic_en, topic_pt, file_name_prefix, category_en, category_pt, content_en, content_pt, references_md=""):
    repo_dir = "/home/rycz/pqc"
    
    # Filenames
    pdf_en_name = f"{date_str}-{file_name_prefix}.pdf"
    pdf_pt_name = f"{date_str}-{file_name_prefix}.pdf"
    
    html_en_path = os.path.join(repo_dir, "en", f"{date_str}-{file_name_prefix}.html")
    html_pt_path = os.path.join(repo_dir, "pt-BR", f"{date_str}-{file_name_prefix}.html")
    
    pdf_en_path = os.path.join(repo_dir, "en", pdf_en_name)
    pdf_pt_path = os.path.join(repo_dir, "pt-BR", pdf_pt_name)
    
    # 1. Write HTML and Compile PDFs
    print("Writing HTML and compiling PDFs...")
    for lang, title, headline, category, content, html_path, pdf_path in [
        ("en", f"PQC Daily: {topic_en}", topic_en, category_en, content_en, html_en_path, pdf_en_path),
        ("pt-BR", f"CPQ Diário: {topic_pt}", topic_pt, category_pt, content_pt, html_pt_path, pdf_pt_path)
    ]:
        full_html = html_template.format(
            lang=lang,
            title=title,
            headline=headline,
            day=day_str,
            category=category,
            date=date_str,
            content=content
        )
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(full_html)
            
        # Chromium command to print to PDF
        cmd = [
            "/usr/bin/chromium",
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            f"--print-to-pdf={pdf_path}",
            "--no-pdf-header-footer",
            html_path
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            print(f"Compiled PDF successfully: {pdf_path}")
            os.remove(html_path)
        else:
            print(f"Failed compilation for {lang}: {res.stderr}")
            return False

    # 2. Update Timeline File
    print("Updating timeline...")
    timeline_path = os.path.join(repo_dir, "timeline")
    new_timeline_row = f"| **{day_str}** | {date_str} | {topic_en} / {topic_pt} | [PDF (EN)](en/{pdf_en_name}) | [PDF (PT-BR)](pt-BR/{pdf_pt_name}) | {category_en} | Completed |\n"
    
    with open(timeline_path, "r", encoding="utf-8") as f:
        timeline_content = f.read()
        
    # Append row
    if not timeline_content.endswith("\n"):
        timeline_content += "\n"
    timeline_content += new_timeline_row
    
    with open(timeline_path, "w", encoding="utf-8") as f:
        f.write(timeline_content)

    # 3. Update README.md
    print("Updating README.md...")
    readme_path = os.path.join(repo_dir, "README.md")
    with open(readme_path, "r", encoding="utf-8") as f:
        readme_content = f.read()
        
    # Replace Latest Study Material links
    en_link_pattern = r"- \*\*English \(EN\):\*\* \[Day \d+ - .*?\]\(en/.*?.pdf\)"
    pt_link_pattern = r"- \*\*Português \(PT-BR\):\*\* \[Dia \d+ - .*?\]\(pt-BR/.*?.pdf\)"
    
    new_en_link = f"- **English (EN):** [Day {day_str} - {topic_en} ({date_str})](en/{pdf_en_name})"
    new_pt_link = f"- **Português (PT-BR):** [Dia {day_str} - {topic_pt} ({date_str})](pt-BR/{pdf_pt_name})"
    
    readme_content = re.sub(en_link_pattern, new_en_link, readme_content)
    readme_content = re.sub(pt_link_pattern, new_pt_link, readme_content)
    
    # Append references if provided to Credits & Original Material section
    if references_md:
        credits_marker = "### NIST PQC Project Links"
        if credits_marker in readme_content:
            new_credits = f"### Daily Tracking News & Resources ({date_str})\n{references_md}\n\n### NIST PQC Project Links"
            readme_content = readme_content.replace(credits_marker, new_credits)
            
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)

    # 4. Push to Git
    print("Pushing to GitHub...")
    # Get GITHUB_TOKEN
    env_path = "/home/rycz/.hermes/.env"
    token = ""
    if os.path.exists(env_path):
        with open(env_path, "r") as f:
            content = f.read()
            m = re.search(r"GITHUB_TOKEN=(\S+)", content)
            if m:
                token = m.group(1)
                
    if token:
        # Secure git authentication using token
        repo_url = f"https://x-access-token:{token}@github.com/paulocauca/pqc.git"
        # Run git config, add, commit, push
        subprocess.run(["git", "-C", repo_dir, "config", "user.name", "Paulo Cauca"])
        subprocess.run(["git", "-C", repo_dir, "config", "user.email", "paulocauca@gmail.com"])
        subprocess.run(["git", "-C", repo_dir, "add", "."])
        subprocess.run(["git", "-C", repo_dir, "commit", "-m", f"docs: add Day {day_str} study material ({date_str})"])
        
        # Capture push output safely
        res = subprocess.run(["git", "-C", repo_dir, "push", "origin", "main"], capture_output=True, text=True)
        if res.returncode == 0:
            print("Successfully pushed to GitHub!")
            return True
        else:
            print("Git push failed!")
            print(res.stderr.replace(token, "REDACTED"))
            return False
    else:
        print("GITHUB_TOKEN not found in .env, cannot push!")
        return False

if __name__ == "__main__":
    # If run directly as a script (for testing or debugging)
    pass
