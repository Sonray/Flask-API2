from flask import Flask
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def index():
    newsapi = NewsApiClient(api_key='93b88e88b50744049520cbd817770986')
    top_headlines = newsapi.get_top_headlines('bbc-news,the-verge')

    articles = top_headlines['articles']

    description = []
    news = []
    image = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        news.append(myarticles['description'])
        news.append(myarticles['urlToImage'])



