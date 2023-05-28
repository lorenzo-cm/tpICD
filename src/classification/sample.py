"""
Sample phrases
"""

import pandas as pd
import seaborn as sns
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


phrases_list = [
    "The cat jumped over the moon.",
    "A stitch in time saves nine.",
    "Two wrongs don't make a right.",
    "The early bird catches the worm.",
    "All that glitters is not gold.",
    "Actions speak louder than words.",
    "Don't count your chickens before they hatch.",
    "The pen is mightier than the sword.",
    "When in Rome, do as the Romans do.",
    "I have a big hair"
]

negative_phrases_list = [
    "This is a disaster!",
    "I can't stand it anymore.",
    "Everything is going wrong.",
    "I'm so frustrated.",
    "Nothing ever goes my way.",
    "I feel so miserable.",
    "I'm completely fed up.",
    "This is the worst day ever.",
    "I'm so disappointed.",
    "I can't catch a break."
]

positive_phrases_list = [
    "You're doing great!",
    "Keep up the good work!",
    "You're awesome!",
    "You're making progress!",
    "You've got this!",
    "You're an inspiration!",
    "You're making a difference!",
    "You're on the right track!",
    "You're capable of amazing things!",
    "You're making it happen!",
]


def vader_sample_test():
    """
    Function to test Vader
    """

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
        
        df = pd.DataFrame(phrases_list + negative_phrases_list + positive_phrases_list , columns=['phrases'])
        

        

    return 'ac'