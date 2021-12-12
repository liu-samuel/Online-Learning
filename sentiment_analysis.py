import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
contents = ['Schools Are Closing Classrooms on Fridays. Parents Are Furious. Desperate to keep teachers, some districts have turned to remote teaching for one day a week — and sometimes more. Families have been left to find child care.',
    'There have already been successful transitions amongst many universities. For example, Zhejiang University managed to get more than 5,000 courses online just two weeks into the transition using “DingTalk ZJU”. The Imperial College London started offering a course on the science of coronavirus, which is now the most enrolled class launched in 2020 on Coursera.'
]

def analyze_sentiment(content: str)  -> float:
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
    overall_score = polarity_sum / len(sentences)
    return round(overall_score, 3)
    # TODO: Can return a tuple with % score and whether it is positive or negative. i.e("positive", 86)


# Example usage
for content in contents:
    print(analyze_sentiment(content))
