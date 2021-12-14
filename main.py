"""Main file which retrieves all the articles, processes the articles, performs sentiment analysis on
the articles, and creates the graphs of number of articles and sentiment scores."""


from scrape_articles import scrape_articles
from process_articles import process_articles
from graphing import create_graphs


scrape_articles()
process_articles()
create_graphs()
