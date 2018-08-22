import scraping_hacker_news
import re

def rank_and_drop():
    articles = []
    articles.extend(scraping_hacker_news.title_lister())

    keywords = [word for word in ['Facebook', 'Computer Science', 'JavaScript', 'AI', 'Artificial Intelligence', 'Elon', 'competitive', 'AGI', 'Machine Learning', "SQL" 'ML', 'Post-Modernism', 'Post Modernism', 'UBI', 'Universal Basic Income', 'Python', 'py', 'Programming', 'Google']]
    keywords = set(keywords)

    for article in articles:
        for keyword in keywords:
            if re.search(r'\b' + keyword.lower() + r'\b', article.title.lower()):
                article.rank += 1
                article.matches.append(keyword)
    articles = sorted(articles, key=lambda article: article.rank, reverse=True)
    articles = [article for article in articles if article.rank > 0]
    return articles