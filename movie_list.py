import films
import fresh_tomatoes

#Movie information is stored in this file.

secret_life_of_pets = films.Movie('Secret Life of Pets',
                                  'Cartoon movie about the secret lives of pets.',
                                  'https://upload.wikimedia.org/wikipedia/en/6/64/The_Secret_Life_of_Pets_poster.jpg',
                                  'https://www.youtube.com/watch?v=eWI_Jsw9qUs')

the_revenant = films.Movie('The Revenant',
                          'A Movie About Survival.',
                          'http://t1.gstatic.com/images?q=tbn:ANd9GcS5yuCSZqK5Hha5lElqZr2SCYVY-sYycKZ8PJ8POfNQkOmSuo5B',
                          'https://www.youtube.com/watch?v=LoebZZ8K5N0')

noah = films.Movie('Noah',
                   "A movie about Noah's Ark",
                   'http://t3.gstatic.com/images?q=tbn:ANd9GcT4IYO9GtUV9x3mJzdQZdAEssks3B7nF78AMR5EwokOiA1F0Lun',
                   'https://www.youtube.com/watch?v=_OSaJE2rqxU')

london_has_fallen = films.Movie('London Has Fallen',
                                'A movie about London under attack',
                                'http://t1.gstatic.com/images?q=tbn:ANd9GcTkGHLEqDWPJIR5aewHrJcJSuejZ4u-ft-a4E1IwIL7qOYhKkEz',
                                'https://www.youtube.com/watch?v=3AsOdX7NcJs')



movie_array = [secret_life_of_pets, the_revenant, noah, london_has_fallen]

fresh_tomatoes.open_movies_page(movie_array)
