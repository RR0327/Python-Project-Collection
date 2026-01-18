from abc import ABC, abstractmethod
from datetime import datetime


# ====================================
# BASE CLASS (ABSTRACT)
# ====================================
class Media(ABC):
    def __init__(self, title, author, media_id):
        self.title = title
        self.author = author
        self.media_id = media_id

    @abstractmethod
    def get_type(self):
        pass

    def display_info(self):
        return f"{self.get_type()} | {self.title} by {self.author}"


# ====================================
# BOOK CLASS (INHERITANCE)
# ====================================
class Book(Media):
    def __init__(self, title, author, media_id, pages):
        super().__init__(title, author, media_id)
        self.pages = pages

    def get_type(self):
        return "Book"


# ====================================
# DIGITAL RESOURCE CLASS (INHERITANCE)
# ====================================
class DigitalResource(Media):
    def __init__(self, title, author, media_id, file_size):
        super().__init__(title, author, media_id)
        self.file_size = file_size

    def get_type(self):
        return "Digital Resource"


# ====================================
# LIBRARY CLASS (SEARCH INTERFACE)
# ====================================
class Library:
    def __init__(self):
        self.media_collection = []

    def add_media(self, media):
        self.media_collection.append(media)

    def search(self, keyword):
        results = []
        for media in self.media_collection:
            if (
                keyword.lower() in media.title.lower()
                or keyword.lower() in media.author.lower()
            ):
                results.append(media)
        return results


# ====================================
# CHECKOUT SYSTEM (COMPOSITION)
# ====================================
class Checkout:
    def __init__(self, media, user):
        self.media = media  # Composition
        self.user = user
        self.checkout_date = datetime.now()

    def get_details(self):
        return (
            f"User: {self.user}\n"
            f"Item: {self.media.display_info()}\n"
            f"Checked out on: {self.checkout_date.strftime('%Y-%m-%d')}"
        )


# ====================================
# DEMO / MAIN EXECUTION
# ====================================
if __name__ == "__main__":

    library = Library()

    # Add media items
    book1 = Book("Clean Code", "Robert C. Martin", 101, 464)
    book2 = Book("Python Crash Course", "Eric Matthes", 102, 544)
    digital1 = DigitalResource("AI Basics", "Andrew Ng", 201, "50MB")

    library.add_media(book1)
    library.add_media(book2)
    library.add_media(digital1)

    # Search
    print("Search Results for 'Python':")
    results = library.search("Python")
    for item in results:
        print(item.display_info())

    # Checkout (Composition)
    checkout = Checkout(book2, "Rakibul Hassan")
    print("\nCheckout Details:")
    print(checkout.get_details())
