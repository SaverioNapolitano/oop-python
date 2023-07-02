class CaseString:
    def __init__(self, string, upper):
        self.string = string
        self.upper = upper

    # @property
    # def string(self):
    #    return self._string

    # @string.setter
    # def string(self, value):
    #    self._string = value

    def set_upper(self, upper):
        self.upper = upper

    def set_string(self, string):
        self.string = string

    def get_string(self):
        return self.string.upper() if isinstance(self.string, str) and self.upper else self.string
