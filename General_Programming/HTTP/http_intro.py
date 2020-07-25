# what happens when you enter a url?
# 1. DNS lookup - finds where url is located, like a phonebook for the internet
#     - takes names or aliases and turns it into an ip address
# 2. Computer makes a request to a server
# 3. Server processes the request
# 4. Server issues a response

# ^^Request Response Cycle^^

# 200 Response from server means OK (good response)

# HTTP Headers
# - sent with both requests and responses
# - provide additonaly info about the request or response

# Request Headers
# - Accept
# - Cache-Control
# - User-Agent

# Response Headers
# - Access-Control-Allow-Origin
# - Allowed

# Response Status Codes
# - 2xx Success
# - 3xx Redirect
# - 4xx Client Error(your fault?)
# - 5xx Server Error(not your fault?)

# HTTP Verbs
# - GET - useful for retrieving data
#       - data passed in query string
#       - should have no "side-effects"
#       - can be cached
#       - can be bookmarked
# - POST - useful for writing data
#        - data passed in request body
#        - can have "side-effects"
#        - can't be cached
#        - can't be bookmarked

# API - Application Programming Interface
# - allows you to get data from another application without needing to understand how the application works
# - can often send data back in different formats
