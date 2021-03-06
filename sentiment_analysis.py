"""
File that contains functions to perform sentiment analysis
"""
# imports
import os
import ast
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download(['vader_lexicon', 'punkt'
               ])  # download vader lexicon nltk package


def analyze_sentiment(content: str) -> float:
    """
    Function that takes in content (usually paragraphs) and
    returns an overall sentiment score using the VADER model.
    Returns a float rounded to 3 decimals ranging from -1, to 1
    """
    sia = SentimentIntensityAnalyzer()  # create the sentiment analyzer
    polarity_sum = 0
    sentences = nltk.sent_tokenize(content)  # breaks up the content into list of = sentences.
    for sentence in sentences:  # loop through each sentence
        score = sia.polarity_scores(sentence)  # get the polarity score of the sentence
        polarity_sum += score['compound']  # add the score to the sum
    overall_score = (polarity_sum / len(sentences))  # calculate the overall score of the article
    return overall_score


def month_sentiment() -> dict[str: (float, int)]:
    """
    Returns a dictionary of the file name / month to the score and the number of articles.
    """
    scores = {}
    path_of_directory = 'processed_articles'
    articles_in_folder = os.listdir(path_of_directory)  # list of all the processed articles
    for file_name in articles_in_folder:
        if file_name[-3:] == 'txt':  # ensure that we are only looping through text files
            with open(path_of_directory + '/' + file_name, 'r') as articles_file:
                articles = ast.literal_eval(
                    articles_file.read())  # read the text inside the file and convert it to a dict
                sentiment_sum = 0
                content_counter = 0
                for date in articles:
                    if articles[date] != []:  # ensure that there are articles in that day
                        for content in articles[date]:
                            # loop through all the articles in that day
                            sentiment_sum += analyze_sentiment(content)
                            # analyze the sentiment of the article
                            content_counter += 1  # increase the content counter

                if content_counter == 0:  # check if there are articles in the month
                    total_sentiment = 0
                else:
                    total_sentiment = round(((sentiment_sum / content_counter) * 100),
                                            2)  # calculate the average sentiment for the month
                scores[articles_file.name] = (total_sentiment,
                                              content_counter)
                # assign the dictionary with the file name of the key
                # and the value being a tuple of total sentiment and the content count
    return scores


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['os', 'ast', 'nltk', 'nltk.sentiment'],
        'allowed-io': ['month_sentiment'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
