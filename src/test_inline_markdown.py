import unittest
from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
from textnode import TextType, TextNode

class TestLinkExtraction(unittest.TestCase):

    def test_image(self):
        sample: list[tuple] = [("image description", "http://localhost/images/picture.png")]
        test = "random text ![image description](http://localhost/images/picture.png) some other text"
        self.assertEqual(extract_markdown_images(test), sample)

        test = "random! tex[t ![image description](http://localhost/images/picture.png) (some o)ther t]ext"
        self.assertEqual(extract_markdown_images(test), sample)

    def test_link(self):
        sample: list[tuple] = [("link text", "http://google.com/content/index.html")]
        test = "random text [link text](http://google.com/content/index.html) some other text"
        self.assertEqual(extract_markdown_links(test), sample)

        test = "ra!ndom [text [link text](http://google.com/content/index.html) ]some ot(her )text"
        self.assertEqual(extract_markdown_links(test), sample)

    def test_images(self):
        sample: list[tuple] = [("image description", "http://localhost/images/picture.png"), ("second image description", "http://localhost/images/picture2.png")]
        test = "random text ![image description](http://localhost/images/picture.png) some other text random! tex[t ![second image description](http://localhost/images/picture2.png) (some o)ther t]ext"
        self.assertEqual(extract_markdown_images(test), sample)

    def test_links(self):
        sample: list[tuple] = [("link text", "http://google.com/content/index.html"), ("second link text", "http://google.com/content/index2.html")]
        test = "random text [link text](http://google.com/content/index.html) some other text ra!ndom [text [second link text](http://google.com/content/index2.html) ]some ot(her )text"
        self.assertEqual(extract_markdown_links(test), sample)

class TestUrlNodes(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )