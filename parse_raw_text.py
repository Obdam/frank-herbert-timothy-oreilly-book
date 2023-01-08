from bs4 import BeautifulSoup
from pathlib import Path

# Split the raw text into a list of paragraphs
raw_text = Path('chapter_9_raw.txt').read_text()
paragraphs = raw_text.split('\n\n')

# Create an empty BeautifulSoup object to hold the xhtml-tagged paragraphs
soup = BeautifulSoup('', 'html.parser')
body = soup.new_tag('body')

# Iterate over the paragraphs, enclosing each one in the appropriate xhtml tags
for paragraph in paragraphs:
  p = soup.new_tag('p')
  p.string = paragraph
  body.append(p)

# Add the body to the html tag
html = soup.new_tag('html')
html.append(body)

# Use the prettify method to properly indent the xhtml tags
pretty_html = html.prettify()

with open('chapter_9.xhtml', 'w') as f:
  f.write(pretty_html)
