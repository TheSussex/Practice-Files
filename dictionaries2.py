# make an empty list for movies
movies = []

# make 20 movie samples
for movie_no in range(20):
    new_movie = {'title': 'King of Boys', 'genre': 'family drama'}
    movies.append(new_movie)

# show the first 5 movies
for movie in movies[:5]:
    print(movie)
    print("...")

# show how many movies have been created
print("Total number of movies: " + str(len(movies)))
