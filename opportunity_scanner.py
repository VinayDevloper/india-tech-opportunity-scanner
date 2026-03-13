import requests
import os

API_KEY = os.getenv("NEWS_API_KEY")

url = "https://newsapi.org/v2/everything"



params = {
    "q": "technology OR startup OR AI OR semiconductor",
    "language": "en",
    "pageSize": 20, 
    "apiKey": API_KEY
}

response = requests.get(url, params=params)

data = response.json()
articles = data["articles"]
print("----- TECH OPPORTUNITY SIGNALS -----")

keywords = ["AI", "startup", "robotics", "semiconductor"]

count = 1
for article in articles:
    title= article.get("title", "")

    for word in keywords:
        if word.lower() in title.lower():
            print(f"{count}.{title}")
            count+=1
            break


            