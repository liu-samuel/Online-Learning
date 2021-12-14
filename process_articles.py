"""Process the articles into usable forms
"""

import json
import newspaper

# variable designed to store list of months to be iterated through when converting txt to json
MONTH = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
         'august', 'september', 'october', 'november', 'december']


def process_articles() -> None:
    """Process the articles in the articles directory, returning a json file mapping each date to a list containing
    the text of each article that was published on that day.
    """
    for month in MONTH:
        # converting txt file to json file for each month
        with open(f'articles/{month}_articles.txt', 'r') as fobj:
            # data variable used to store json files with raw data dictionary
            data = json.load(fobj)

        # dict mapping dates to lists of articles
        master = {}
        # looping through the dates in data
        for date, raw_articles in data.items():
            # initializing a new variable as an empty list
            processed_articles = []
            # looping through the values of the dictionary in data
            for raw_article in raw_articles:
                # storing article url in Article object from newspaper
                processed_article = newspaper.Article(raw_article['web_url'])
                processed_article.download()
                processed_article.parse()
                processed_articles.append(processed_article.text)
                print(f'Processed "{processed_article.title}" published on {date}')
            # creating a dictionary mapping the date to a list of processed articles
            master[date] = processed_articles
        # dumps master dict in txt file for each month in MONTH
        with open(f'processed_articles/{month}_processed_articles.txt', 'w') as outfile:
            json.dump(master, outfile)

