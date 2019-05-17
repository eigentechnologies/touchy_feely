import re

from nltk.sentiment.vader import SentimentIntensityAnalyzer


true_feeler = SentimentIntensityAnalyzer()


class Feeler:
    """Feeler for a piece of text"""

    def __init__(self, text):
        self._text = pre_process_text(text)
        self._feeling = None

    @property
    def text(self):
        return self._text

    @property
    def feeling(self):
        return self._feeling

    def feel(self):
        self._feeling = true_feeler.polarity_scores(self._text)


def pre_process_text(text: str) -> str:
    text = re.sub("(?<=[A-Za-z_])\.(?=[A-Za-z_])", " ", text)
    text = re.sub("[_@\n]", " ", text)
    return text
