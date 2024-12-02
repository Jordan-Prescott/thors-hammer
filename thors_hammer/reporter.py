from .api import API


class Reporter:
    def __init__(self, api: API):
        self.api = api
