class HTMLNode:
    def __init__(self,
                 tag: str = None,
                 value: str = None,
                 children: list = None,
                 props: dict[str,str] = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        props_str: str = ""
        if self.props:
            for prop, value in self.props.items():
                props_str += f' {prop}="{value}"'
        return(props_str)

    def __repr__(self) -> str:
        return(f"{self.tag}, {self.value}, {self.children}, {self.props}")

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict[str,str] = None):
       super().__init__(tag, value, None, props) 

    def to_html(self):
        if not self.value:
            raise ValueError("no value provided")

        if not self.tag:
            return self.value

        return(f'<{self.tag}>{self.value}</{self.tag}>')

    def __repr__(self):
        return(f"{self.tag}, {self.value}, {self.props}")

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("tag is missing")

        if not self.children:
            raise ValueError("children is missing")

        html_string = ""

        for child in self.children:
            html_string += child.to_html()

        return(f"<{self.tag}>{html_string}</{self.tag}>")