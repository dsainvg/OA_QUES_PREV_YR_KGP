import os
import glob
import re
import shutil

def on_config(config):
    # Root directory is the current directory where mkdocs command is run
    root_dir = os.getcwd()
    docs_dir = os.path.join(root_dir, 'docs')
    
    # Recreate docs directory to have a clean build
    if os.path.exists(docs_dir):
        try:
            shutil.rmtree(docs_dir)
        except Exception as e:
            print(f"Warning: Could not remove docs directory: {e}")
            
    os.makedirs(docs_dir, exist_ok=True)
    
    # Recreate docs/javascripts directory and copy assets
    js_dest_dir = os.path.join(docs_dir, 'javascripts')
    os.makedirs(js_dest_dir, exist_ok=True)
    js_src_file = os.path.join(root_dir, 'javascripts', 'mathjax.js')
    if os.path.exists(js_src_file):
        shutil.copy(js_src_file, os.path.join(js_dest_dir, 'mathjax.js'))
        
    # Recreate docs/stylesheets directory and copy assets
    css_dest_dir = os.path.join(docs_dir, 'stylesheets')
    os.makedirs(css_dest_dir, exist_ok=True)
    css_src_file = os.path.join(root_dir, 'stylesheets', 'custom.css')
    if os.path.exists(css_src_file):
        shutil.copy(css_src_file, os.path.join(css_dest_dir, 'custom.css'))
        
    # Find all markdown files in root_dir
    md_files = glob.glob(os.path.join(root_dir, '*.md'))
    companies = []
    
    for f in md_files:
        filename = os.path.basename(f)
        # Exclude index.md or README.md from the root directory so they don't override our index/homepage
        if filename.lower() in ('index.md', 'readme.md'):
            continue
            
        # Get company name from filename
        name = os.path.splitext(filename)[0]
        company_name = name.replace('-', ' ').replace('_', ' ').title()
        
        # Read the file to count questions and rewrite its main header
        num_questions = 0
        file_content_str = ""
        try:
            with open(f, 'r', encoding='utf-8') as file_content:
                file_content_str = file_content.read()
                
                # Count headers starting with '### Q'
                q_matches = re.findall(r'^###\s+Q\d+', file_content_str, re.MULTILINE)
                num_questions = len(q_matches)
                
                # If no matching headers, search for "Total questions: X"
                if num_questions == 0:
                    tq_match = re.search(r'Total questions:\s*(\d+)', file_content_str)
                    if tq_match:
                        num_questions = int(tq_match.group(1))
        except Exception as e:
            print(f"Error reading file {filename}: {e}")
            
        # Rename the generic H1 header (e.g. "# Interview Questions") in the copied file to "# <Company Name>"
        # This makes the navigation tab and page title automatically show the company name!
        modified_content, replacement_count = re.subn(r'^#\s+.*$', f"# {company_name}", file_content_str, count=1, flags=re.MULTILINE)
        if replacement_count == 0:
            modified_content = f"# {company_name}\n\n" + file_content_str
            
        # Remove the "Generated from: ..." line dynamically
        modified_content = re.sub(r'^\*Generated from:.*\n?', '', modified_content, flags=re.MULTILINE)
            
        # Write the modified markdown file to the docs/ directory
        dest_file_path = os.path.join(docs_dir, filename)
        try:
            with open(dest_file_path, 'w', encoding='utf-8') as dest_file:
                dest_file.write(modified_content)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
            
        companies.append({
            'name': company_name,
            'filename': filename,
            'questions': num_questions
        })
        
    companies.sort(key=lambda x: x['name'])
    
    # Generate content for docs/index.md
    md_content = []
    md_content.append("# DSA Prep: Company Online Assessments")
    md_content.append("Welcome to the DSA Prep Questions Archive. Explore previous Online Assessment (OA) coding questions and solutions for various top tech companies.\n")
    md_content.append("## Available Companies\n")
    md_content.append('<div class="grid cards" markdown>\n')
    
    for c in companies:
        name = c['name']
        filename = c['filename']
        q_count = c['questions']
        q_text = f"{q_count} question{'s' if q_count != 1 else ''}"
        
        md_content.append(f"-   :material-briefcase: **{name}**")
        md_content.append("    ---")
        md_content.append(f"    Contains {q_text}.")
        md_content.append(f"    [:octicons-arrow-right-24: View Questions]({filename})\n")
        
    md_content.append('</div>\n')
    md_content.append("\n---\n*This index is auto-generated and updated on every commit. Add new markdown files to the repository, and they will automatically appear here.*")
    
    # Write to docs/index.md
    index_path = os.path.join(docs_dir, 'index.md')
    with open(index_path, 'w', encoding='utf-8') as index_file:
        index_file.write('\n'.join(md_content))
        
    print(f"Successfully generated docs/index.md and copied {len(companies)} company files to docs/.")
    return config
