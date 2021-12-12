import json
import newspaper

# CHANGE THIS
MONTH = 'march'

with open(f'articles/{MONTH}_articles.txt', 'r') as fobj:
    data = json.load(fobj)

# dict mapping dates to lists of articles
master = {}
for date, raw_articles in data.items():
    processed_articles = []
    for raw_article in raw_articles:
        processed_article = newspaper.Article(raw_article['web_url'])
        processed_article.download()
        processed_article.parse()
        processed_articles.append(processed_article.text)
        print(f'Processed "{processed_article.title}" published on {date}')
    master[date] = processed_articles

with open(f'{MONTH}_processed_articles.txt', 'w') as outfile:
    json.dump(master, outfile)

