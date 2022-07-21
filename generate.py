from ebooklib import epub

if __name__ == '__main__':
    book = epub.EpubBook()

    # Add metadata to te EPUB
    book.set_title('Frank Herbert (Recognitions)')
    book.add_author('Timothy O\'Reilly')
    book.add_metadata('DC', 'publisher',
                      'Frederick Ungar Publishing Co., Inc.')
    book.add_metadata('DC', 'date', '1981-06-01')
    book.set_language('en')
    book.set_identifier('urn:isbn:9780804426664')
    book.add_metadata('DC', 'description', 'The highest praise that can be given to an author is to say that his work awakens unexpected possibilities of thought and feeling. I have written about Frank Herbert from this perspective. His work has touched me, and I have learned from him. To my mind, the most fundamental judgment to be made about a novel is not as a work of art built to abstract standards, but as an act of communication. What does it say to the reader? How does it touch him?')
    book.set_cover("image.jpg", open(
        'images/frank-herbert-cover-230x346.jpg', 'rb').read())

    c1 = epub.EpubHtml(title='Acknowledgements',
                       file_name='contents/chapter_01.xhtml')
    c1.content = open('contents/chapter_01.xhtml', "r").read()
    c1.set_language('en')

    c2 = epub.EpubHtml(title='Introduction: How I Came to Write Frank Herbert',
                       file_name='contents/chapter_02.xhtml')
    c2.content = open('contents/chapter_02.xhtml', "r").read()
    c2.set_language('en')

    c3 = epub.EpubHtml(title='Preface',
                       file_name='contents/chapter_03.xhtml')
    c3.content = open('contents/chapter_03.xhtml', "r").read()
    c3.set_language('en')

    c4 = epub.EpubHtml(title='Chapter 1: Dancing on the Edge',
                       file_name='contents/chapter_04.xhtml')
    c4.content = open('contents/chapter_04.xhtml', "r").read()
    c4.set_language('en')

    book.add_item(c1)
    book.add_item(c2)
    book.add_item(c3)
    book.add_item(c4)

    book.toc = [(epub.Section('Introduction'), (c1, c2, c3)),
                (epub.Section('Chapters'), (c1, c2, c3))]
    #c5,c6,c7,c8,c9,c10,c11,c12,c13,c14

    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    style = open('stylesheets/stylesheet.css', "r").read()

    book_css = epub.EpubItem(
        uid="book_style", file_name="stylesheets/stylesheet.css", media_type="text/css", content=style)
    book.add_item(book_css)

    book.spine = ['cover', c1, 'nav', c2, c3, c4]

    epub.write_epub('boekie.epub', book)
