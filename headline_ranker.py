import scraping_hacker_news


def rank_and_drop():
    articles = []

    articles.extend(scraping_hacker_news.title_lister())

    # Method needs to be defined here. Word list
    # should come from outside function

    word_list = [word.capitalize() for word in ['AI', 'Artificial Intelligence', 'Elon', 'competitive', 'AGI', 'Machine Learning', "SQL" 'ML', 'Post-Modernism', 'Post Modernism', 'UBI', 'Universal Basic Income', 'python', 'py', 'programming']]
    word_list = set(word_list)

    for article in articles:
        words = article.title.split()
        for word in words:
            article.rank += (word.capitalize() in word_list)
    articles = sorted(articles, key=lambda article:
                      article.rank, reverse=True)
    articles = [article for article in articles if article.rank > 0]
    return articles
