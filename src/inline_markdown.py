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

def parse_text(text: str) -> tuple[str, str]:
    md_literals: set = ["!", "[", "]", "(", ")"]

    for literal in md_literals:
        text = text.replace(literal, " ")

    text_parts = text.split()

    return (text_parts[0], text_parts[1])

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    images = re.findall(r"\!\[(\w+)\]\((\w+)\)")
    images_list: list = []

    for image_string in images:
        image_tuple = parse_text(image_string)
        images_list.append(image_tuple)

    return images_list

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    links = re.findall(r"\[(\w+)\]\((\w+)\)")
