from inline_markdown import split_node_delimiter
from split_image import split_nodes_image
from split_link import split_nodes_link
from textnode import TextNode, TextType

def text_to_textnodes(text):
    starting_list = [] 
    text_node = TextNode(text, TextType.TEXT)
    starting_list.append(text_node)
    split_code = split_node_delimiter(starting_list,"`", TextType.CODE)
    split_bold = split_node_delimiter(split_code,"**", TextType.BOLD)
    split_italic = split_node_delimiter(split_bold,"_", TextType.ITALIC)
    split_image = split_nodes_image(split_italic)
    final_list = split_nodes_link(split_image)
    return final_list