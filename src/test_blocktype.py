import unittest
from blocktype import block_to_block_type, BlockType


class TestBlockToBlockType(unittest.TestCase):
    def test_heading_block(self):
        markdown_block = "# This is a heading"
        self.assertEqual(block_to_block_type(markdown_block), BlockType.HEADING)

    def test_another_heading_block(self):
        markdown_block = "## This is another heading"
        self.assertEqual(block_to_block_type(markdown_block), BlockType.HEADING)

    def test_code(self):
        markdown_block = """``` 
        This is code
        This is some more code
        Boots wants his salmon
        Boots why is the server room on fire?
        if boots + salmon == Happybear:
        print("yay")
        ```"""
        self.assertEqual(block_to_block_type(markdown_block), BlockType.CODE)
    
    def test_Quote(self):
        markdown_block = "> This is Quote"
        self.assertEqual(block_to_block_type(markdown_block), BlockType.QUOTE)
    
    def test_unordered_list(self):
        markdown_block = "- This\n- is\n- an\n- unordered\n- list"
        self.assertEqual(block_to_block_type(markdown_block), BlockType.UNORDERED_LIST)
    
    def test_ordered_list(self):
        markdown_block = "1. This\n2. is \n3. an \n4. ordered \n5. list"
        self.assertEqual(block_to_block_type(markdown_block), BlockType.ORDERED_LIST)
    
    def test_paragraph_list(self):
        markdown_block = " This is a paragraph"
        self.assertEqual(block_to_block_type(markdown_block), BlockType.PARAGRAPH)