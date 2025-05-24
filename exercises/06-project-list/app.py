import requests

# Your code here
url = "https://assets.breatheco.de/apis/fake/sample/project_list.php"
response = requests.get(url)
project_list = response.json()
second_name = project_list[1]["name"]
print(second_name)