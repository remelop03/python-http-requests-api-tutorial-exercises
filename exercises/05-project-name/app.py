import requests

url = "https://assets.breatheco.de/apis/fake/sample/project1.php"
response = requests.get(url)

# Your code here
dict = response.json()
name = dict["name"]
print(name)