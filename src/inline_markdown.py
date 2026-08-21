import re
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

        for index in range(0, len(text_split)):
            if text_split[index] != "":
                if index % 2 != 0:
                    new_nodes.append(TextNode(text_split[index], text_type))
                else:
                    new_nodes.append(TextNode(text_split[index], TextType.TEXT))

    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        text = node.text
        images = extract_markdown_images(text)

        if images == []:
            new_nodes.append(node)
            continue

        new_nodes.extend(build_node_list(text, images, TextType.IMAGE))
        
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        text = node.text
        links = extract_markdown_links(text)

        if links == []:
            new_nodes.append(node)
            continue

        new_nodes.extend(build_node_list(text, links, TextType.LINK))
        
    return new_nodes

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    pattern = r"\!\[(.[^\[\]]+)\]\((\S+)\)"
    images = re.findall(pattern, text)
    return images

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    pattern = r"\[(.[^\[\]]+)\]\((\S+)\)"
    links = re.findall(pattern, text)
    return links

def build_node_list(text: str, pairs: list[tuple], type: TextType) -> list[TextNode]:
    nodes: list[TextNode] = []
    for pair in pairs:
        if type == TextType.IMAGE:
            sections = text.split(f"![{pair[0]}]({pair[1]})", 1)
        else:
            sections = text.split(f"[{pair[0]}]({pair[1]})", 1)
        
        if sections[0] != "":
            nodes.append(TextNode(sections[0], TextType.TEXT))

        nodes.append(TextNode(pair[0], type, pair[1]))
        text = sections[1]

    if text != "":
        nodes.append(TextNode(text, TextType.TEXT))

    return nodes

def text_to_textnodes(text: str) -> list[TextNode]:
    textnodes: list[TextNode] = [TextNode(text, TextType.TEXT)]
    textnodes = split_nodes_delimiter(textnodes, "**", TextType.BOLD)
    textnodes = split_nodes_delimiter(textnodes, "_", TextType.ITALIC)
    textnodes = split_nodes_delimiter(textnodes, "`", TextType.CODE)
    textnodes = split_nodes_image(textnodes)
    textnodes = split_nodes_link(textnodes)