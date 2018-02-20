# media contains the Movie class
import media
# fresh_tomatoes generates a html page from a list of Movie objects.
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "pictures/toy_story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

predator = media.Movie("Predator",
                       "pictures/predator.jpg",
                       "https://www.youtube.com/watch?v=DrCqEA4r_R4")

conan = media.Movie("Conan the Barbarian",
                    "pictures/conan.jpg",
                    "https://www.youtube.com/watch?v=B3YwzRmBPLY")

lotr_two_towers = media.Movie("Lord of the Rings: The Two Towers",
                              "pictures/lotr_two_towers.jpg",
                              "https://www.youtube.com/watch?v=gXC-jJhFaUI")

movies = [toy_story, predator, conan, lotr_two_towers]

#pass movies list to open_movies_page for html page generation.
fresh_tomatoes.open_movies_page(movies)
