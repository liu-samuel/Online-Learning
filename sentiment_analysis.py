import os
import ast
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()


def analyze_sentiment(content: str) -> float:
    """
    Function that takes in content (usually paragraphs) and returns an overall sentiment score using the VADER model.
    Returns a float rounded to 3 decimals ranging from -1, to 1
    """

    polarity_sum = 0
    sentences = nltk.sent_tokenize(content)
    for sentence in sentences:
        score = sia.polarity_scores(sentence)
        polarity_sum += score['compound']
        # print(score)
    overall_score = (polarity_sum / len(sentences))
    return overall_score


def month_sentiment() -> list[float]:
    """
    Returns a list of sentiment scores.
    """
    scores = []
    path_of_directory = 'processed_articles'
    articles_in_folder = os.listdir(path_of_directory)  # list of all the processed articles
    for file_name in articles_in_folder:
        articles_file = open(path_of_directory + '/' + file_name, 'r')
        articles = ast.literal_eval(
            articles_file.read())  # read the text inside the file and convert it to a dictionary
        sentiment_sum = 0
        content_counter = 0
        for date in articles:

            if articles[date] != []:
                sentiment_sum += analyze_sentiment(articles[date][0])
                content_counter += 1
        total_sentiment = round(((sentiment_sum / content_counter) * 100), 2)
        scores.append(total_sentiment)
    return scores

