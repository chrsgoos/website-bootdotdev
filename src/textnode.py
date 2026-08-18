from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):

    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, 
                 content: str, 
                 type: TextType, 
                 url: str | None = None) -> None:

        self.text = content
        self.text_type = type
        self.url = url

    def __eq__(self, other) -> bool:
        return(
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self) -> str:
        return(f"TextNode({self.text}, {self.text_type.value}, {self.url})")

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if not text_node.text_type:
        raise Exception("not a valid TextType")

    match text_node.text_type.value:
        case "text":
            return LeafNode(None, text_node.text)
        case "bold":
            return LeafNode("b", text_node.text)
        case "italic":
            return LeafNode("i", text_node.text)
        case "code":
            return LeafNode("code", text_node.text)
        case "link":
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case "image":
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})