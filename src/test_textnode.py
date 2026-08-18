import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node3 = TextNode("This is another text node", TextType.ITALIC)
        node4 = TextNode("This is another text node", TextType.ITALIC)
        self.assertEqual(node3, node4)

    def test_noteq(self):
        node1 = TextNode("This is a test link", TextType.LINK, "http://google.com")
        node2 = TextNode("This is a test link", TextType.LINK, "http://gogle.com")
        self.assertNotEqual(node1,node2)
        
        node1 = TextNode("This is  test link", TextType.LINK, "http://google.com")
        node2 = TextNode("This is a test link", TextType.LINK, "http://gogle.com")
        self.assertNotEqual(node1,node2)

        node1 = TextNode("This is a test link", TextType.IMAGE, "http://google.com")
        node2 = TextNode("This is a test link", TextType.LINK, "http://gogle.com")
        self.assertNotEqual(node1,node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold message", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold message")

        
    def test_italic(self):
        node = TextNode("This is an italic message", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic message")


    def test_code(self):
        node = TextNode("This is codetext", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is codetext")


    def test_link(self):
        node = TextNode("It's a hyperlink", TextType.LINK, "https://google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "It's a hyperlink")
        self.assertEqual(html_node.props, {"href": "https://google.com"})
    
    def test_img(self):
        node = TextNode("image description", TextType.IMAGE, "http://example.com/test.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": "http://example.com/test.png", "alt": "image description"})
    

if __name__ == "__main__":
    unittest.main()
