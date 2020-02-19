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

# function to grab a specific class/name/data/attribute from the html
d = soup.select("[data-example]")

# function to get all tags in the html
f = soup.find_all("div")

# get classes
c = soup.find_all(class_ = "special")

# get id
i = soup.find(id='first')

# get attrs
a = soup.find_all(attrs={'data-example':'yes'})

#get using css selectors
css = soup.select('#first')
css = soup.select('.special')

print(d)
print(f)
print(c)
print(i)
print(a)
print(css)
