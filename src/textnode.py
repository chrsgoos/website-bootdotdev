from enum import Enum

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