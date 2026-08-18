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
