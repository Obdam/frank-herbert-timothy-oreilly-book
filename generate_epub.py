from ebooklib import epub

book = epub.EpubBook()

# Add metadata
book.add_author("Timothy O'Reilly")
book.set_title('Frank Herbert')
book.set_identifier('9780804426664')
book.set_language('en')
book.set_cover('frank_herbert_cover_230x346.jpg', open(
    'static/frank_herbert_cover_230x346.jpg', 'rb').read())

chapters = {
    1: 'How I Came to Write Frank Herbert',
    2: 'Preface',
    3: 'Chapter 1: Dancing on the Edge',
    4: 'Chapter 2: Under Pressure',
    5: 'Chapter 3: From Concept to Fable',
    6: 'Chapter 4: The Hero',
    7: 'Chapter 5: Rogue Gods',
    8: 'Chapter 6: An Ecology of Consciousness',
    9: 'Chapter 7: The Worm Turns',
    10: 'Chapter 8: Transcending the Human',
    11: 'Chapter 9: How It All Begins Again',
    12: 'Notes',
    13: 'Bibliography',
    14: 'Index',
}

book.toc = []
book.spine = ['cover', 'nav']

for key, value in chapters.items():
    chapter = epub.EpubHtml(title=f'{value}',
                            file_name=f'./contents/chapter_{key}.xhtml',
                            content=open(f'./contents/chapter_{key}.xhtml', 'r').read())
    book.add_item(chapter)

    book.toc.append(
        epub.Link(href=f'./contents/chapter_{key}.xhtml', title=f'{value}', uid=f'chapter_{key}'))

    book.spine.append(chapter)

# Add CSS file
book.add_item(epub.EpubItem(uid='style_css', file_name='./static/stylesheet.css',
              media_type='text/css', content=open('./static/stylesheet.css', 'r').read()))

book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

# Write the epub file
epub.write_epub('frank_herbert_timothy_oreilly.epub', book, {})
