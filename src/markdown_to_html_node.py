from blocktype import block_to_block_type, BlockType
from split_blocks import markdown_to_blocks
from htmlnode import ParentNode
from block_to_node import paragraph_block_to_node, heading_to_block_node, code_to_block_node, ordered_list_to_block_node, unordered_list_to_block_node, quote_to_block_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH: 
            children.append(paragraph_block_to_node(block))

        elif block_type == BlockType.HEADING:
            children.append(heading_to_block_node(block))
        
        elif block_type == BlockType.CODE:
            children.append(code_to_block_node(block))

        elif block_type == BlockType.QUOTE:
            children.append(quote_to_block_node(block))

        elif block_type == BlockType.ORDERED_LIST:
            children.append(ordered_list_to_block_node(block))

        elif block_type == BlockType.UNORDERED_LIST: 
            children.append(unordered_list_to_block_node(block))

    return ParentNode("div", children)