import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
     def test_html_node(self):
        node1 = HTMLNode("h1", "Title", props={"class": "chapter"})
        self.assertEqual(node1.props_to_html(), ' class="chapter"')

        node2 = HTMLNode("p", "Hello world!")
        self.assertEqual(node2.props_to_html(), '')

        node3 = HTMLNode("div", props={"class": "content"})
        self.assertEqual(node3.props_to_html(), ' class="content"')
        node4 = HTMLNode("a", "testlink", props={"href": "https://www.google.com", "target": "blank"})

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_div(self):
        node = LeafNode("div", "Container Content", props={"class": "content"})
        self.assertEqual(node.to_html(), "<div>Container Content</div>")

    def test_leaf_repr(self):
        node = LeafNode("a", "testlink", props={"href": "https://www.google.com", "target": "blank"})
        self.assertEqual(node.__repr__(), "a, testlink, {'href': 'https://www.google.com', 'target': 'blank'}")

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>"
            )


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()
