from copystatic import copy_static
from gencontent import generate_pages_recursive
import sys


def main():
    if len(sys.argv) == 1:
        basepath = "/"
    else:
        basepath = sys.argv[1]
    static_path = "static"
    public_path = "docs"
    copy_static(static_path, public_path)
    generate_pages_recursive("content", "template.html", public_path, basepath)

if __name__ == "__main__":
    main()

