
#  Author: Chris Adamson
# Project: Movie Trailer Website

import media
import fresh_tomatoes

amazon_img_url = "https://images-na.ssl-images-amazon.com/images/M"

# Create, and initialize the Training Day movie object
img = "MV5BMDZkMTUxYWEtMDY5NS00ZTA5LTg3MTItNTlkZWE1YWRjYjMwL2ltYWdlL" + \
      "2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg"

training_day = media.Movie("Training Day",
                           "%s/%s" % (amazon_img_url, img),
                           "https://youtu.be/DXPJqRtkDP0")

# Create, and initialize the Fight Club movie object
img = "MV5BZGY5Y2RjMmItNDg5Yy00NjUwLThjMTEtNDc2OGUzNTBiYmM1XkEyXkFqcGdeQXV" + \
      "yNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg"

fight_club = media.Movie("Fight Club",
                         "%s/%s" % (amazon_img_url, img),
                         "https://youtu.be/SUXWAEX2jlg")

# Create, and initialize the 99 Homes movie object
img = "MV5BMTgyODExMDc0M15BMl5BanBnXkFtZTgwMjY2ODg4NTE@._V1_UX182_CR0," + \
      "0,182,268_AL_.jpg"

ninety_nine_homes = media.Movie("99 Homes",
                                "%s/%s" % (amazon_img_url, img),
                                "https://youtu.be/Vh0piQN1_LY")

# Create, and initialize the 13 hours movie object
img = "MV5BMjU3OTQ5NDc3Ml5BMl5BanBnXkFtZTgwOTEwNTkxNzE@._V1_UX182_CR0" + \
      ",0,182,268_AL_.jpg"

thirteen_hours = media.Movie("13 hours",
                             "%s/%s" % (amazon_img_url, img),
                             "https://youtu.be/5MBjAN7jqsQ")

# Create, and initialize the coyote ugly movie object
img = "MV5BMTk1NzM1ODg4OF5BMl5BanBnXkFtZTcwMTQ3OTgyMQ@@._V1_UY268_CR3," + \
      "0,182,268_AL_.jpg"

coyote_ugly = media.Movie("Coyote Ugly",
                          "%s/%s" % (amazon_img_url, img),
                          "https://youtu.be/I6vLz1TjeVY")

# Create, and initialize the breach movie object
img = "MV5BMzY1NjgxMjk0Ml5BMl5BanBnXkFtZTcwOTc4NzI0MQ@@._V1_UX182_CR0," + \
      "0,182,268_AL_.jpg"

breach = media.Movie("Breach",
                     "%s/%s" % (amazon_img_url, img),
                     "https://youtu.be/9JPmiGTT6tI")


movie_list = [training_day,
              fight_club,
              ninety_nine_homes,
              thirteen_hours,
              coyote_ugly,
              breach]

fresh_tomatoes.open_movies_page(movie_list)
