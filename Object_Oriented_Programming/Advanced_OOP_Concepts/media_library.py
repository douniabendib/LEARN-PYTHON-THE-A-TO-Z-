# Inheritance approach
class Media:
    # Implement Media class
    def __init__(self, title, creator, year):
        self.title = title
        self.creator = creator
        self.year = year
    
    def display_info(self):
        return f"{self.__class__.__name__}: {self.title} {self.creator} ({self.year})"


class Book(Media):
    def display_info(self):
        return f"Book: {self.title} by {self.creator} ({self.year})"

class Movie(Media):
    # Implement Movie class
    def display_info(self):
        return f"Movie: {self.title} directed by {self.creator} ({self.year})"


class MusicAlbum(Media):
    def display_info(self):
        return f"Music Album: {self.title} by {self.creator} ({self.year})"


# Composition approach
class Media:
    # Implement Media class
    def __init__(self, title, creator, year):
        self.title = title
        self.creator = creator
        self.year = year
        
class MediaItem:
    def __init__(self, media_type, title, creator, year):
        self.media_type = media_type
        self.media = Media(title, creator, year)

    def display_info(self):
        if self.media_type == "Book":
            return f"Book: {self.media.title} by {self.media.creator} ({self.media.year})"
        elif self.media_type == "Movie":
            return f"Movie: {self.media.title} directed by {self.media.creator} ({self.media.year})"
        elif self.media_type == "Music Album":
            return f"Music Album: {self.media.title} by {self.media.creator} ({self.media.year})"

class BookComposition(MediaItem):
    def __init__(self, title, creator, year):
        super().__init__("Book", title, creator, year)

class MovieComposition(MediaItem):
    def __init__(self, title, creator, year):
        super().__init__("Movie", title, creator, year)

class MusicAlbumComposition(MediaItem):
    def __init__(self, title, creator, year):
        super().__init__("Music Album", title, creator, year)


# Test code 
def test_media_classes():
    # Test inheritance approach
    book = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    movie = Movie("The Matrix", "Wachowski Sisters", 1999)
    album = MusicAlbum("Abbey Road", "The Beatles", 1969)
    
    assert book.display_info() == "Book: The Hobbit by J.R.R. Tolkien (1937)"
    assert movie.display_info() == "Movie: The Matrix directed by Wachowski Sisters (1999)"
    assert album.display_info() == "Music Album: Abbey Road by The Beatles (1969)"
    
    # Test composition approach
    book_comp = BookComposition("Dune", "Frank Herbert", 1965)
    movie_comp = MovieComposition("Inception", "Christopher Nolan", 2010)
    album_comp = MusicAlbumComposition("Thriller", "Michael Jackson", 1982)
    
    assert book_comp.display_info() == "Book: Dune by Frank Herbert (1965)"
    assert movie_comp.display_info() == "Movie: Inception directed by Christopher Nolan (2010)"
    assert album_comp.display_info() == "Music Album: Thriller by Michael Jackson (1982)"
    
    print("All tests passed!")


test_media_classes()
