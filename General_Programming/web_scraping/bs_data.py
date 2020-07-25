# Accessing data in Elements
# get_text - access inner text in an element
# name - tag name
# attrs - dictionary of attributes

from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special super-special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""
# function to parse the html string
soup = BeautifulSoup(html, "html.parser")
el = soup.select('.special')
for e in el:
    print(e.name + '->' + e.get_text())
    print(e.attrs)

attr = soup.find('h3')['data-example']
print(attr)

div = soup.find('div')['id']
print(div)
