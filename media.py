
#  Author: Chris Adamson
# Project: Movie Trailer Website

class Movie():
    """
    Defines a movie object with various characteristics such as the
    movie title, image URL, and youtube trailer.
    """

    def __init__(self, movie_title, image_url, trailer_youtube):
        """
        initializes the movie object with the title, image url,
        and youtube trailer
        """
        self.title = movie_title
        self.poster_image_url = image_url
        self.trailer_youtube_url = trailer_youtube

    def __str__(self):
        """
        Returns a string representation of this movie instance
        """
        movie_str = "movie title: %s, image url: %s, youtube id: %s"

        return movie_str.format(self.title,
                                self.poster_image_url,
                                self.trailer_youtube_url)
