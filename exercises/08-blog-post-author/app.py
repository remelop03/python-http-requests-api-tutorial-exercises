import requests

# Your code here
url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
response = requests.get(url)
data = response.json()

# Getting the first post
first_post = data["posts"][0]
        
# Getting the author dictionary
author_dict = first_post["author"]
        
# Getting the author name
author_name = author_dict["name"]

print(author_name)