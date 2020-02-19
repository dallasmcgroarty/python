# navigating with beautiful soup
# via tags
# - parent
# - contents
# - next_sibling
# - previous_sibling

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
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""
# function to parse the html string
soup = BeautifulSoup(html, "html.parser")
# data = soup.body.contents[1].next_sibling.next_sibling
# data = soup.find(class_= 'special').parent
# data = soup.find(id='first').find_next_sibling()
# data = soup.select('[data-example]')[1].find_previous_sibling().find_previous_sibling()
data = soup.find('h3').find_parent()
print(data)