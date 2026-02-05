from enum import Enum 

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown):
    lines = markdown.split("\n")
    striped_lines = []
    for line in lines:
        striped_lines.append(line.strip())
    
    if len(striped_lines) > 1:
        if striped_lines[0].startswith("```") and striped_lines[-1].startswith("```"):
            return BlockType.CODE
    
    heading_checker = ["# ", "## ", "### ", "#### ", "##### ", "###### "]
    for heading in heading_checker:
        if striped_lines[0].startswith(heading):
            return BlockType.HEADING
    
    is_quote = True
    for line in striped_lines:
        if not line.startswith(">") and not line.startswith("> "):
            is_quote = False
            break
    if is_quote:
        return BlockType.QUOTE

    is_unordered_list = True
    for line in striped_lines:
        if not line.startswith("- "):
            is_unordered_list = False
            break
    if is_unordered_list:
        return BlockType.UNORDERED_LIST     
    
    is_ordered_list = True
    expected_num = 1 
    for line in striped_lines: 
        prefix = f"{expected_num}. "
        if not line.startswith(prefix):
            is_ordered_list = False
            break 
        expected_num += 1
    
    if is_ordered_list:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH
