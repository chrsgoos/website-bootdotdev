import unittest
from inline_markdown import extract_markdown_images, extract_markdown_links

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