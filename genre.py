import pickle
import pandas as pd
import numpy as np
import requests

# fetch poster function
def fetch_poster(poster_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=338016ac774f28f30916824466db50bf".format(poster_id))
    data = response.json()
    poster_path = data['poster_path']
    return "https://image.tmdb.org/t/p/w500/" + poster_path

# load the data
movies_list = pickle.load(open('genres.pkl','rb'))

# convert th data into dataframe
movies = pd.DataFrame(movies_list)

# select box
genre_list = ['select-option','Action','Drama','Fantasy','Adventure','Thriller','Crime','War','Animation','Mystery','ScienceFiction','Comedy','Horror','Romance','History','Music','Documentary','Western','Foreign']

# recommendation function
def genres(genre):
    recommended_movies = []
    for x in movies["genres"]:
        if genre in x:
            get_index = list(movies['genres']).index(x)
            recommended_movies.append(movies['title'][get_index])
    find_unique_movies = set(recommended_movies)
    unique_movies = list(find_unique_movies)

    # Top movies
    top_movies = unique_movies[0:8]
   
    # fetch the posters
    recommend_movies = []
    recommend_poster = []
    for i in top_movies:
        details = movies[movies['title'] == i]
        movie_title = details['title']
        poster_id = details['movie_id']
        recommend_movies.append(movie_title.iloc[0])
        recommend_poster.append(fetch_poster(poster_id.iloc[0]))
    return (recommend_movies, recommend_poster)