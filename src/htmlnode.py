class HTMLNode:
    def __init__(tag: str = None,
                 value: str = None,
                 children: list[HTMLNode] = None,
                 props: dict[str,str] = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        prop_str: str = ""
        for prop, value in self.props:
            prop_str += f' {prop}="{value}"'
        return(prop_str)

    def __repr__(self) -> str:
        return(f"{self.tag}, {self.value}, {self.children}, {self.props}")
