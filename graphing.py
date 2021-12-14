"""This will graph our popularity over time as well as the sentiment scores
"""

import plotly.graph_objects as go
import sentiment_analysis as sentiment


def create_sentiment_graph() -> None:
    """Create graphs for sentiment scores during 2020 about online learning
    """
    # calls the sentiment analysis function that was created
    scores = sentiment.month_sentiment()

    # assigns the output of the sentiment function to each month
    january = scores['processed_articles/january_processed_articles.txt']
    february = scores['processed_articles/february_processed_articles.txt']
    march = scores['processed_articles/march_processed_articles.txt']
    april = scores['processed_articles/april_processed_articles.txt']
    may = scores['processed_articles/may_processed_articles.txt']
    june = scores['processed_articles/june_processed_articles.txt']
    july = scores['processed_articles/july_processed_articles.txt']
    august = scores['processed_articles/august_processed_articles.txt']
    september = scores['processed_articles/september_processed_articles.txt']
    october = scores['processed_articles/october_processed_articles.txt']
    november = scores['processed_articles/november_processed_articles.txt']
    december = scores['processed_articles/december_processed_articles.txt']

    # assigns the sentiment scores

    s_january_score = january[0]
    s_february_score = february[0]
    s_march_score = march[0]
    s_april_score = april[0]
    s_may_score = may[0]
    s_june_score = june[0]
    s_july_score = july[0]
    s_august_score = august[0]
    s_september_score = september[0]
    s_october_score = october[0]
    s_november_score = november[0]
    s_december_score = december[0]

    # x values for each graph
    month_in_2020 = ['January', 'February', 'March', 'April', 'May', 'June',
                     'July', 'August', 'September', 'October', 'November', 'December']

    # y values for each respective graph
    sentiment_score = [s_january_score, s_february_score, s_march_score, s_april_score,
                       s_may_score, s_june_score, s_july_score, s_august_score, s_september_score,
                       s_october_score, s_november_score, s_december_score]

    # create the sentiment Graph
    fig = go.Figure()
    fig.update_layout(paper_bgcolor="white")

    # This creates the actual line for the sentiment score
    fig.add_trace(go.Scatter(
        x=month_in_2020,
        y=sentiment_score)
    )

    # creates the layout with font, title, and axis for the sentiment
    fig.update_layout(
        title='Sentiment Scores of Online Learning',
        xaxis_title='Month in 2020',
        yaxis_title='Sentiment Score',
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="Black"
        )
    )

    fig.show()


def create_popularity_graph() -> None:
    """Create graphs for popularity scores during 2020 about online learning
    """
    # calls the sentiment analysis function that was created
    scores = sentiment.month_sentiment()

    # assigns the output of the sentiment function to each month
    january = scores['processed_articles/january_processed_articles.txt']
    february = scores['processed_articles/february_processed_articles.txt']
    march = scores['processed_articles/march_processed_articles.txt']
    april = scores['processed_articles/april_processed_articles.txt']
    may = scores['processed_articles/may_processed_articles.txt']
    june = scores['processed_articles/june_processed_articles.txt']
    july = scores['processed_articles/july_processed_articles.txt']
    august = scores['processed_articles/august_processed_articles.txt']
    september = scores['processed_articles/september_processed_articles.txt']
    october = scores['processed_articles/october_processed_articles.txt']
    november = scores['processed_articles/november_processed_articles.txt']
    december = scores['processed_articles/december_processed_articles.txt']

    # assigns the popularity scores

    p_january_score = january[1]
    p_february_score = february[1]
    p_march_score = march[1]
    p_april_score = april[1]
    p_may_score = may[1]
    p_june_score = june[1]
    p_july_score = july[1]
    p_august_score = august[1]
    p_september_score = september[1]
    p_october_score = october[1]
    p_november_score = november[1]
    p_december_score = december[1]

    # x values for each graph
    month_in_2020 = ['January', 'February', 'March', 'April', 'May', 'June',
                     'July', 'August', 'September', 'October', 'November', 'December']

    popularity_score = [p_january_score, p_february_score, p_march_score, p_april_score,
                        p_may_score, p_june_score, p_july_score, p_august_score, p_september_score,
                        p_october_score, p_november_score, p_december_score]

    # create the popularity Graph

    fig = go.Figure()
    fig.update_layout(paper_bgcolor="white")

    # This creates the actual line for the popularity score
    fig.add_trace(go.Scatter(
        x=month_in_2020,
        y=popularity_score
    ))

    # creates the layout with font, title, and axis for the popularity
    fig.update_layout(
        title='Number of Articles Related to Online Schooling',
        xaxis_title='Month in 2020',
        yaxis_title='Number of Articles',
        legend_title="Legend Title",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="Blue"
        )
    )

    fig.show()


if __name__ == '__main__':
    import python_ta
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    python_ta.check_all(config={
        'allowed-io': ['plotly.graph_objects'],
        'extra-imports': ['plotly.graph_objects', 'sentiment_analysis'],
        'max-line-length': 100,
        'max-args': 6,
        'max-locals': 30,
        'disable': ['R1705'],
    })
