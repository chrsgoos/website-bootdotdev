from textnode import TextType, TextNode


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        if node.text.count(delimiter) % 2 != 0:
            raise Exception(f"{delimiter} was not closed")

        text_split: list = node.text.split(delimiter)
        new_nodes.append(TextNode(text_split[0], TextType.TEXT))

        match delimiter:
            case "**":
                new_nodes.append(TextNode(text_split[1], TextType.BOLD))
            case "_":
                new_nodes.append(TextNode(text_split[1], TextType.ITALIC))
            case "`":
                new_nodes.append(TextNode(text_split[1], TextType.CODE))

    return new_nodes
