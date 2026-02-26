class Author:
    """Represents an author who can have multiple books through contracts."""
    
    all = []  # Class attribute to track all Author instances

    def __init__(self, name):
        """Initialize an Author with a name and add them to the class registry."""
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        self.name = name
        Author.all.append(self)

    def contracts(self):
        """Return a list of all contracts associated with this author."""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """Return a list of all books associated with this author via contracts."""
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Create and return a new Contract between this author and the given book."""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Return the total royalties earned by this author across all contracts."""
        return sum(contract.royalties for contract in self.contracts())



class Book:
    """Represents a book that can have multiple authors through contracts."""
    
    all = []  # Class attribute to track all Book instances

    def __init__(self, title):
        """Initialize a Book with a title and add it to the class registry."""
        if not isinstance(title, str):
            raise Exception("Title must be a string.")
        self.title = title
        Book.all.append(self)

    def contracts(self):
        """Return a list of all contracts associated with this book."""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Return a list of all authors associated with this book via contracts."""
        return [contract.author for contract in self.contracts()]



class Contract:
    """Represents a contract linking an Author to a Book with a date and royalties."""
    
    all = []  

    def __init__(self, author, book, date, royalties):
        """Initialize a Contract and add it to the class registry."""
    
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        """Validate that author is an instance of Author."""
        if not isinstance(value, Author):
            raise Exception("author must be an instance of Author.")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        """Validate that book is an instance of Book."""
        if not isinstance(value, Book):
            raise Exception("book must be an instance of Book.")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        """Validate that date is a string."""
        if not isinstance(value, str):
            raise Exception("date must be a string.")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        """Validate that royalties is an integer."""
        if not isinstance(value, int):
            raise Exception("royalties must be an integer.")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts matching the given date."""
        return [contract for contract in cls.all if contract.date == date]
