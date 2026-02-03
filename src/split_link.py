from textnode import TextType, TextNode
from extract_markdown import extract_markdown_links

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes: 
        if node.text_type is not TextType.TEXT: 
            new_nodes.append(node)
            continue
        extracted_links = extract_markdown_links(node.text)

        if extracted_links == []:
            new_nodes.append(node)
            continue
        original_text = node.text

        for alt, url in extracted_links:
            link_md = f"[{alt}]({url})"
            sections = original_text.split(link_md, 1)

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(alt, TextType.LINK,url))
            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes