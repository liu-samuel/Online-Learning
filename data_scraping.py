"""Get the data
"""

import requests
import json
from time import sleep

API_KEY = 'bgNmOAdMP9A4Lo08qoxVhZvFO6v1JTBS'
MIN_WORD_COUNT = 200
YEAR = 2020

DAYS_PER_MONTH = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
MONTH_TO_STRING = {
    1: 'january',
    2: 'february',
    3: 'march',
    4: 'april',
    5: 'may',
    6: 'june',
    7: 'july',
    8: 'august',
    9: 'september',
    10: 'october',
    11: 'november',
    12: 'december'
}

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


class BadResponseError(Exception):
    """Exception raised when NYT api returns a response that is not 'OK'."""


def generate_date(year: int, month: int, day: int) -> tuple[str, str]:
    """Return a date string representing the year, month, and day in the format 'YYYYMMDD'
    >>> generate_date(2020, 3, 4)
    ('20200304', '20200305')
    >>> generate_date(2020, 2, 29)
    ('20200229', '20200301')
    >>> generate_date(2020, 12, 31)
    ('20201231', '20210101')

    Preconditions:
        - 1 <= day <= 31
        - Day is a valid integer for that month, i.e. not February 30
        - 1 <= month <= 12
        - year has four digits and has actually occurred
    """
    begin_year_str = str(year)
    # begin dates
    if month < 10:
        begin_month_str = '0' + str(month)
    else:
        begin_month_str = str(month)
    if day < 10:
        begin_day_str = '0' + str(day)
    else:
        begin_day_str = str(day)
    # end dates
    end_day_str = str(day + 1)
    end_month_str = begin_month_str
    if day < 10:
        end_day_str = '0' + str(day + 1)
    if day == DAYS_PER_MONTH[month]:
        end_day_str = '01'
        end_month = (month % 12) + 1
        if end_month < 10:
            end_month_str = '0' + str(end_month)
        else:
            end_month_str = str(end_month)
    if month == 12 and day == 31:
        end_year_str = str(year + 1)
    else:
        end_year_str = begin_year_str
    begin = begin_year_str + begin_month_str + begin_day_str
    end = end_year_str + end_month_str + end_day_str
    return (begin, end)


def main() -> None:
    """Driver code to actually retrieve the specified articles.
    """
    MONTH = 1
    while MONTH < 13:
        master_articles = {}

        for i in range(1, DAYS_PER_MONTH[MONTH] + 1):
            page = 1
            begin_date, end_date = generate_date(YEAR, MONTH, i)
            url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?' \
                  'q=online learning' \
                  f'&api-key={API_KEY}' \
                  f'&begin_date={begin_date}' \
                  f'&end_date={end_date}' \
                  f'&page={page}'

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
            while len(response['response']['docs']) == 10:
                sleep(6)
                page += 1
                url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?' \
                      'q=online learning' \
                      f'&api-key={API_KEY}' \
                      f'&begin_date={begin_date}' \
                      f'&end_date={end_date}' \
                      f'&page={page}'
                response = requests.get(url).json()
                for article in response['response']['docs']:
                    if article['word_count'] >= MIN_WORD_COUNT:
                        articles.append(article)

            master_articles[f'{begin_date}'] = articles
            print(f'Got {len(articles)} articles for {begin_date}')
            sleep(6)

        with open(f'articles/{MONTH_TO_STRING[MONTH]}_articles.txt', 'w') as outfile:
            outfile.truncate(0)
            json.dump(master_articles, outfile)
        MONTH += 1


if __name__ == '__main__':
    main()
