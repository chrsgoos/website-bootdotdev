from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    
    for node in old_nodes:
        if not node.text_type.TEXT:
            new_nodes.extend(node)

        if 

    return new_nodes