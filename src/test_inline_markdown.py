import unittest
from textnode import TextNode, TextType
from mdnode import split_nodes_delimiter

nodes = [TextNode("`text` **bold** _italic_", TextType.TEXT),
            TextNode("**Hallo** _Welt_ und `code`", TextType.TEXT),
            TextNode("Normaler Text mit **fett**, _kursiv_ und `inline code`.", TextType.TEXT),
            TextNode("nur normaler Text", TextType.TEXT)
]
class TestMdNode(unittest.TestCase):
    def test_bold(self):
        self.assertEqual(split_nodes_delimiter(nodes, "**", TextType.BOLD), [
            TextNode("`text` ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" _italic_", TextType.TEXT),
            TextNode("Hallo", TextType.BOLD),
            TextNode(" _Welt_ und `code`", TextType.TEXT),
            TextNode("Normaler Text mit ", TextType.TEXT),
            TextNode("fett", TextType.BOLD),
            TextNode(", _kursiv_ und `inline code`.", TextType.TEXT),
            TextNode("nur normaler Text", TextType.TEXT)
        ])

    def test_italic(self):
        self.assertEqual(split_nodes_delimiter(nodes, "_", TextType.ITALIC), [
            TextNode("`text` **bold** ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode("**Hallo** ", TextType.TEXT),
            TextNode("Welt", TextType.ITALIC),
            TextNode(" und `code`", TextType.TEXT),
            TextNode("Normaler Text mit **fett**, ", TextType.TEXT),
            TextNode("kursiv", TextType.ITALIC),
            TextNode(" und `inline code`.", TextType.TEXT),
            TextNode("nur normaler Text", TextType.TEXT)
        ])

    def test_code(self):
        self.assertEqual(split_nodes_delimiter(nodes, "`", TextType.CODE), [
            TextNode("text", TextType.CODE),
            TextNode(" **bold** _italic_", TextType.TEXT),
            TextNode("**Hallo** _Welt_ und ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode("Normaler Text mit **fett**, _kursiv_ und ", TextType.TEXT),
            TextNode("inline code", TextType.CODE),
            TextNode(".", TextType.TEXT),
            TextNode("nur normaler Text", TextType.TEXT)
        ])