from flask import Flask, render_template
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
        description.append(myarticles['description'])
        image.append(myarticles['urlToImage'])

    myList = zip(news, description, image)

    return render_template('index.html', context = myList)
