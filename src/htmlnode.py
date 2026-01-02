

class HTMLNode():
    def __init__(self, tag = None,value = None,children = None,props= None):
        self.tag = tag
        self.value = value 
        self.children = children 
        self.props = props 
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None or self.props == {}:
            return ""
        else: 
            prop_string = ""
            for prop in self.props:
                prop_string += f' {prop}="{self.props[prop]}"'
            return prop_string
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")

        if self.tag is None:
            return self.value

        props_str = self.props_to_html()
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        else: 
            props_str = self.props_to_html()
            string = f"<{self.tag}{props_str}>"
            for child in self.children:
                string += child.to_html()
            string += f"</{self.tag}>"
        return string