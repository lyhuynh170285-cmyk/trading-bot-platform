class ExchangeRequired(Exception):
    def __init__(self, *args):

        self.message = "An exchange must be included in the request."

    def __str__(self):
        return f"{self.message}"

    def __repr__(self):
        return self.__class__.__name__
