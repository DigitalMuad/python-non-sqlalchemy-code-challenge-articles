class Article:
    def __init__(self, author, magazine, title: str):
        # Validate and set the title
        if not isinstance(title, str):
            raise TypeError("Title must be of type str")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters, inclusive")
        
        # Prevent modification of title after instantiation
        if hasattr(self, "_title"):
            raise AttributeError("Title cannot be modified after instantiation")
        
        # Set the title (private attribute)
        self._title = title

        # Set the author and magazine
        self.author = author  # Uses the author setter for validation
        self.magazine = magazine  # Uses the magazine setter for validation

        # Add the article to the author's and magazine's lists
        self.author._articles.append(self)
        self.magazine._articles.append(self)

    @property
    def title(self):
        """Returns the article's title (read-only)."""
        return self._title

    @title.setter
    def title(self, value):
        """Prevents modification of the title after instantiation."""
        raise AttributeError("Title cannot be modified after instantiation")

    @property
    def author(self):
        """Returns the author object for the article."""
        return self._author

    @author.setter
    def author(self, new_author):
        """Sets the author object for the article with validation."""
        if not isinstance(new_author, Author):
            raise TypeError("Author must be of type Author")
        self._author = new_author

    @property
    def magazine(self):
        """Returns the magazine object for the article."""
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        """Sets the magazine object for the article with validation."""
        if not isinstance(new_magazine, Magazine):
            raise TypeError("Magazine must be of type Magazine")
        self._magazine = new_magazine

class Author:
    def __init__(self, name: str):
        # Validate and set the name
        if not isinstance(name, str):
            raise TypeError("Name must be of type str")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        
        # Prevent modification after instantiation
        if hasattr(self, "_name"):
            raise AttributeError("Cannot modify name after instantiation")
        
        # Set the name (private attribute)
        self._name = name

        # Initialize an empty list to store articles
        self._articles = []

    @property
    def name(self):
        """Returns the author's name."""
        return self._name

    @name.setter
    def name(self, value):
        """Prevents modification of the name after instantiation."""
        raise AttributeError("Cannot modify name after instantiation")

    def articles(self):
        """Returns a list of all the articles the author has written."""
        return self._articles

    def magazines(self):
        """Returns a unique list of magazines the author has contributed to."""
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title: str):
        """Creates and returns a new Article instance associated with this author and magazine."""
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        """Returns a unique list of categories of magazines the author has contributed to."""
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    def __init__(self, name: str, category: str):
        # Validate and set the name and category
        self.name = name
        self.category = category

        # Initialize an empty list to store articles
        self._articles = []

    @property
    def name(self):
        """Returns the magazine's name."""
        return self._name

    @name.setter
    def name(self, value):
        """Sets the magazine's name with validation."""
        if not isinstance(value, str):
            raise TypeError("Name must be of type str")
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        self._name = value

    @property
    def category(self):
        """Returns the magazine's category."""
        return self._category

    @category.setter
    def category(self, value):
        """Sets the magazine's category with validation."""
        if not isinstance(value, str):
            raise TypeError("Category must be of type str")
        if len(value) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = value

    def articles(self):
        """Returns a list of all the articles the magazine has published."""
        return self._articles

    def contributors(self):
        """Returns a unique list of authors who have written for this magazine."""
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        """Returns a list of titles of all articles written for this magazine."""
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        """Returns a list of authors who have written more than 2 articles for this magazine."""
        author_counts = {}
        for article in self._articles:
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        return contributing_authors if contributing_authors else None


