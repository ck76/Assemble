import requests

r = requests.get("https://github.com/favicon.ico")
print("text"+r.text)
print(r.content)