import re

from nltk.sentiment.vader import SentimentIntensityAnalyzer


true_feeler = SentimentIntensityAnalyzer()


class Feeler:
    """
    An empathetic class to feel your code and tell you the truth about how
    awesome you think it is.
    """

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
    """
    Remove the fluff you don't care about and reveal your true meaning.
    :param text:
    :return:
    """
    text = re.sub("(?<=[A-Za-z_])\.(?=[A-Za-z_])", " ", text)
    text = re.sub("[_@\n]", " ", text)
    text = re.sub(
        "(?:def|class|self|cls|import|from|print|return|range|while)", "", text
    )
    return text
