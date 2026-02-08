from copystatic import copy_static
from generate_page import generate_page

def main():
    static_path = "static"
    public_path = "public"
    copy_static(static_path, public_path)
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()

