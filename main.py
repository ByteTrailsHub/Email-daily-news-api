import requests
from send_email import send_email

api_key = (Your API_KEY)
url = ("https://newsapi.org/v2/top-headlines?coun"
       "try=us&category=business&apiKey=YOUR"
       "API_KEY=en")

#make a request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

# Access the article title and descriptions
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = ("Subject: Today's news" + "\n" + body
                + article["title"] + "\n" + str(article["description"])
                + "\n" + article["url"] + 2*"\n")

body = body.encode("utf-8")
send_email(message=body)
