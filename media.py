class Video:
    """General purpose video class"""
    def __init__(self, title):
        self.title = title


class Movie(Video):

    """Movie class initializes with a title, image url, and trailer url"""

    def __init__(self, movie_title, movie_image_url,  movie_trailer_url):
        Video.__init__(self, movie_title)
        self.trailer_youtube_url = movie_trailer_url
        self.poster_image_url = movie_image_url
