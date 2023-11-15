# Frank Herbert by Timothy O'Reilly
This project contains all the XHTML, CSS and other files for creating an EPUB of the book 'Frank Herbert' written by Timothy O'Reilly and published in 1981. The repo consist of a Python file which generates the EPUB. Outside of the Python script, a book cover and a CSS stylesheet . If you want to edit the CSS, feel free to submit a pull request.

# How to use
To get started, install the requirements in your virtual environment:

```
pip install -r requirements.txt
```

To generate the EPUB, run the Python script:

```
python3 generate_epub.py
```

# License
The text of the book is retrieved from [O'Reilly's website](https://www.oreilly.com/tim/herbert/), where he published the book. In [the intro section](https://www.oreilly.com/tim/herbert/intro.html) of the book, he states that he wrote a letter to the publisher the right of the book belongs to:

>Last year, I wrote to Crossroads/Continuum and asked for a reversion of rights to the book so I could put it up on the Web. My letter went unanswered. Since they didn’t bother to answer, I decided to go ahead and do it anyway, figuring, as they say, that it’s sometimes easier to get forgiveness than permission. If anyone from Crossroads/Continuum notices, please give me a call or drop an email. I’d love to see the book back in print, or if not, at least to have your blessing on this Web version.

Therefore, I've decided to use the CC0-1.0 license.