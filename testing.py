"""test that b"""
import newspaper
from GoogleNews import GoogleNews
import csv

import requests
import json
from time import sleep
from pprint import pprint


class BadResponseError(Exception):
    """Exception raised when NYT api returns a response that is not 'OK'."""


MIN_WORD_COUNT = 200

master_articles = {}
start_day = ''
end_day = ''
for i in range(1, 30):
    if i < 9:
        start_day = '0' + str(i)
        end_day = '0' + str(i + 1)
    elif i == 9:
        start_day = '0' + str(i)
        end_day = str(i + 1)
    else:
        start_day = str(i)
        end_day = str(i + 1)
    url = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?' \
           'q=online learning' \
           '&api-key=bgNmOAdMP9A4Lo08qoxVhZvFO6v1JTBS' \
           f'&begin_date=202004{start_day}' \
           f'&end_date=202004{end_day}' \
           '&page=1'

    response = requests.get(url).json()
    try:
        if response['status'] != 'OK':
            raise BadResponseError
    except BadResponseError:
        print(f'Bad Response: {response}')
        quit()

    articles = []
    for article in response['response']['docs']:
        if article['word_count'] >= MIN_WORD_COUNT:
            articles.append(article)

    master_articles[f'202001{start_day}'] = articles
    print(f'Got {len(articles)} articles for {start_day}')
    sleep(6)

with open('articles.txt', 'w') as outfile:
    json.dump(master_articles, outfile)

# googlenews = GoogleNews(lang='en', region='US', start='01/15/2020', end='01/16/2020')
# googlenews.search('online school')
# print(googlenews.total_count())
# googlenews.get_page(2)
# results_pg_2 = googlenews.results()
# googlenews.get_page(3)
# results_pg_3 = googlenews.results()
#
# print('done')


queries = [
    'online learning',
    'online school',
    'zoom university',
    'zoom',
    'google classroom',
    'google meet',
    'video conference',
    'video conferencing'
]
main_queries = [
    'online learning',
    'online school'
]

