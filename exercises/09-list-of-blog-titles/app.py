import requests

def get_titles(web_page):
    # Your code here
    titles = []
    response = requests.get(url)
    data = response.json()
    post = data["posts"]
    return post

url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
print(get_titles(url))