class CustomException(Exception):
    def __init__(self, string):
        self.string = string

    def invoke(self):
        raise CustomException(self.string)
