import webbrowser

#This Class is for storing movie data.

class Movie():

    def __init__(self, title, storyline, image, trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = image
        self.trailer_youtube_url = trailer

    def play_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
