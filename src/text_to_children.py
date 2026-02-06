from textnode import TextNode, TextType, text_node_to_html_node
from text_to_text import text_to_textnodes


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]

