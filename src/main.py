from textnode import TextNode, TextType

def main():
    test = TextNode("This is a test anchor", TextType.LINK, "https://boot.dev")
    print(test)


main()