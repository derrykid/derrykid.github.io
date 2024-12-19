import time


class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.time = time.ctime()

    def __str__(self):
        return f"Title: {self.title} and {self.author}"