import requests
url = "https://assets.breatheco.de/apis/fake/sample/time.php"
response = requests.get(url)
dict = response.json() 
hour = dict["hours"]
min  = dict["minutes"]
sec  = dict["seconds"]
print(f"Current time: {hour} hrs {min} min and {sec} sec")