import requests

api_key = "8277a7c63ede4da39277c99ffa4f1af5"
url = ("https://newsapi.org/v2/top-headlines?coun"
       "try=us&category=business&apiKey=8277a7"
       "c63ede4da39277c99ffa4f1af5")

#make a request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

# Access the article title and ddescriptions
for article in content["articles"]:
    print(article["title"])
    print(article["description"])