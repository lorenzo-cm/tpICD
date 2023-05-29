from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def polarity(phrase : str, analyzer=analyzer)  -> int:
    return analyzer.polarity_scores(phrase)['compound']

def classify(phrase_or_score : str | float , analyzer=analyzer) -> int:
    if isinstance(phrase_or_score, str):
        score = analyzer.polarity_scores(phrase_or_score)['compound']
    else:
        score = phrase_or_score

    if score >= 0.05:
        return 1
    elif score <= -0.05:
        return -1
    else:
        return 0