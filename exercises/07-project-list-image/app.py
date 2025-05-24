import requests

# Your code here
url = "https://assets.breatheco.de/apis/fake/sample/project_list.php"
response = requests.get(url)
project_list = response.json()
image_url = project_list[2]["images"][2]
print(image_url)