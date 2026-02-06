import os 
from markdown_to_html_node import markdown_to_html_node 
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path):
    print(f"Beep Boop ...Generating Page from {from_path} to {dest_path} using {template_path}")

    from_file = open(from_path, "r")
    markdown = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    markdown_html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", markdown_html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    
    to_file = open(dest_path, "w")
    to_file.write(template)
    to_file.close()