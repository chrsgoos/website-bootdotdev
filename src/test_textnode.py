import unittest
from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()