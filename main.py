import requests
from send_email import send_email

api_key = "8277a7c63ede4da39277c99ffa4f1af5"
url = ("https://newsapi.org/v2/top-headlines?coun"
       "try=us&category=business&apiKey=8277a7"
       "c63ede4da39277c99ffa4f1af5")

#make a request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

# Access the article title and ddescriptions
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)