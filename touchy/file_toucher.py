class FileToucher:
    """
    A cold, emotionless class that will touch a file by a given filename and
    wrench the code from within, laying bare your bleak, depressing prose.
    """
    def __init__(self, filename):
        self._filename = filename
        self._text = None

    @property
    def filename(self):
        return self._filename

    @property
    def text(self):
        return self._text

    def touch(self):
        with open(self._filename, "r") as t:
            self._text = t.read()
