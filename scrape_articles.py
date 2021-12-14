"""Query the NYT Article Search API for every day in 2020. Store all articles returned by the
queries in .txt files in json format in the articles directory.
"""


import json
from time import sleep
import requests

# config variables
API_KEY = 'bgNmOAdMP9A4Lo08qoxVhZvFO6v1JTBS'
MIN_WORD_COUNT = 200
YEAR = 2020
DAYS_PER_MONTH = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30,
                  12: 31}
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


def generate_date(year: int, month: int, day: int) -> tuple[str, str]:
    """Return a tuple containing strings representing the year, month, and day in the format
    'YYYYMMDD' of the start date and end date corresponding to that day.
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


def scrape_articles() -> None:
    """Driver code to actually retrieve the specified articles.
    """
    # iterate through every month in 2020
    month = 1
    while month < 13:
        # master dictionary object mapping strings of dates to lists of raw articles published on
        # those dates. We will dump this object into a .txt file at the end
        master_articles = {}

        # iterate through every day in the month
        for i in range(1, DAYS_PER_MONTH[month] + 1):
            page = 1
            begin_date, end_date = generate_date(YEAR, month, i)
            # construct the request to the NYT API
            url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?' \
                  'q=online learning' \
                  f'&api-key={API_KEY}' \
                  f'&begin_date={begin_date}' \
                  f'&end_date={end_date}' \
                  f'&page={page}'

            # make request to NYT API
            response = requests.get(url).json()

            # put every article from the API response that has at least MIN_WORD_COUNT into an
            # accumulator list
            articles = []
            for article in response['response']['docs']:
                if article['word_count'] >= MIN_WORD_COUNT:
                    articles.append(article)
            # if there is a second page of results, put those articles into the accumulator list
            # as well
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

            # map the accumulator list of articles to the date that they were published.
            master_articles[f'{begin_date}'] = articles
            print(f'Got {len(articles)} articles for {begin_date}')
            sleep(6)

        # dump master_articles into a .txt file which holds all articles for that month
        with open(f'articles/{MONTH_TO_STRING[month]}_articles.txt', 'w') as outfile:
            outfile.truncate(0)
            json.dump(master_articles, outfile)
        # repeat for the next month...
        month += 1


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['requests', 'json', 'time'],
        'allowed-io': ['scrape_articles'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
