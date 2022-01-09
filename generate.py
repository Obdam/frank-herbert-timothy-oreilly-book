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

    c1 = epub.EpubHtml(
        title='Introduction: How I Came to Write Frank Herbert',
        file_name='contents/chapter_01.xhtml',
        lang='en')

    c2 = epub.EpubItem()
    # c1.content = u'<html><head></head><body><h1>Introduction</h1><p>Introduction paragraph where i explain what is happening.</p></body></html>'
    book.add_item(c1)

    epub.write_epub('boekie.epub', book)
    # print(c1.get_content())
