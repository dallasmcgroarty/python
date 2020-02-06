import requests, random
# requests lets us make http requests from python
# url = 'https://www.google.com'
# res = requests.get(url)
# print(f"Your request to {url} came back with status code {res.status_code}")
#print(res.text)

# the following code takes the html received from the requests and puts it in a html file

# f=open("index.html","w+")

# f.write(res.text)
# f.close()

url = "https://icanhazdadjoke.com/"

# res = requests.get(url, headers={"Accept": "application/json"}) #'plain/text'
# print(res.json())

# sending Requests with Params
# query string - example: https://google.com/search?term=dog&type=site

def getJokes(term):
    res = requests.get(
        url+'search',
        headers={"Accept":"application/json"},
        params={"term": term}
    )
    data = res.json()
    if data['results']:
        joke = random.choice(data['results'])
        print(f"I found {len(data['results'])} about {term}. Here is one of them:")
        print(joke['joke'])
    else:
        print(f'Sorry, I couldn\'t find any jokes about {term}')


term = input('Let me tell you a joke! Give me a topic: ')
getJokes(term)