from htmlnode import ParentNode
from text_to_children import text_to_children
from textnode import text_node_to_html_node, LeafNode

def paragraph_block_to_node(block):
    lines = block.split("\n")
    text = " ".join(line.strip() for line in lines)
    children_for_block = text_to_children(text)
    return ParentNode("p", children_for_block)

def heading_to_block_node(block):
    lines = block.split("\n")
    first = lines[0].lstrip()

    level = 0
    for ch in first:
        if ch == "#":
            level += 1
        else:
            break

    first_text = first[level:].lstrip()
    rest = [line.strip() for line in lines[1:]]
    all_text = " ".join([first_text] + rest)

    children_for_block = text_to_children(all_text)
    return ParentNode(f"h{level}", children_for_block)

def code_to_block_node(block):
    lines = block.split("\n")
    inner_lines = lines[1:-1]
    code_text = "\n".join(inner_lines) + "\n"

    code_node = LeafNode("code", code_text)
    return ParentNode("pre", [code_node])

def quote_to_block_node(block):
    lines = block.split("\n")
    cleaned_lines = []
    for line in lines:
        line = line.lstrip()
        if line.startswith("> "):
            line = line[2:]
        elif line.startswith(">"):
            line = line[1:]
        cleaned_lines.append(line.strip())
    text = " ".join(cleaned_lines)
    children_for_block = text_to_children(text)
    return ParentNode("blockquote", children_for_block)

def ordered_list_to_block_node(block):
    lines = block.split("\n")
    li_nodes = []
    expected = 1

    for line in lines:
        stripped = line.strip()
        prefix = f"{expected}. "
        if stripped.startswith(prefix):
            item_text = stripped[len(prefix):]
        else:
            item_text = stripped

        li_children = text_to_children(item_text)
        li_nodes.append(ParentNode("li", li_children))
        expected += 1

    return ParentNode("ol", li_nodes)

def unordered_list_to_block_node(block):
    lines = block.split("\n")
    li_nodes = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("- "):
            item_text = stripped[2:]
        else:
            item_text = stripped

        li_children = text_to_children(item_text)
        li_nodes.append(ParentNode("li", li_children))

    return ParentNode("ul", li_nodes)
