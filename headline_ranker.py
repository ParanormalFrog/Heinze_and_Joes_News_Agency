## some logic that imports search keywords ##
import scraping_hacker_news
import random


def rank_and_drop():
    articles = []

    articles.extend(scraping_hacker_news.title_lister())
    word_list = set(['AI', 'Artificial Intelligence', 'competitive', 'AGI', 'Machine Learning', "SQL" 'ML', 'Post-Modernism', 'Post Modernism', 'UBI', 'Universal Basic Income', 'python', 'py', 'programming'])

    for article in articles:
        words = article.title.split()
        for word in words:
            article.rank += (word in word_list)

    articles = sorted(articles, key=lambda article : article.rank, reverse = True)
    articles = [article for article in articles if aritcle.rank > 0]
    return articles
