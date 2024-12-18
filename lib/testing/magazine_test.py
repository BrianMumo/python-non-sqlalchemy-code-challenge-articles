class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    # Property for `name`
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Name must be a string between 2 and 16 characters.")
        self._name = value

    # Property for `category`
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Category must be a non-empty string.")
        self._category = value

    # Returns all articles for this magazine
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    # Returns all unique authors for this magazine
    def contributors(self):
        return list(set(article.author for article in self.articles()))

    # Returns the titles of all articles in this magazine
    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    # Returns authors with more than two articles for this magazine
    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        return [author for author in set(authors) if authors.count(author) > 2] or None

    # Class method that returns the magazine with the most articles
    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        article_count = {magazine: len(magazine.articles()) for magazine in cls.all}
        return max(article_count, key=article_count.get)
