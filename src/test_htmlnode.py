import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_html_node(self):
        node1 = HTMLNode("h1", "Title", props={"class": "chapter"})
        self.assertEqual(node1.props_to_html(), ' class="chapter"')

        node2 = HTMLNode("p", "Hello world!")
        self.assertEqual(node2.props_to_html(), '')

        node3 = HTMLNode("div", props={"class": "content"})
        self.assertEqual(node3.props_to_html(), ' class="content"')
        node4 = HTMLNode("a", "testlink", props={"href": "https://www.google.com", "target": "blank"})
        self.assertEqual(node4.props_to_html(), ' href="https://www.google.com" target="blank"')

if __name__ == "__main__":
    unittest.main()
