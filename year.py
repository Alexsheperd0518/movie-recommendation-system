import pickle
import pandas as pd
import requests

# fetch poster function
def fetch_poster(poster_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=338016ac774f28f30916824466db50bf".format(poster_id))
    data = response.json()
    poster_path = data['poster_path']
    return "https://image.tmdb.org/t/p/w500/" + poster_path

# load the data
movies_list = pickle.load(open('year.pkl','rb'))

# convert th data into dataframe
movies = pd.DataFrame(movies_list)

# recommendation function for year wise movies fetch
def year_wise(year):
    new_movies = movies.loc[movies['release_date'] == year]
    movies_title = new_movies['title']
    
    # top 8 movies
    top_8_movies = movies_title[0:12]

    recommend_movies = []
    recommend_poster = []
    for i in top_8_movies:
        details = movies[movies['title'] == i]
        movies_title = details['title']
        poster_id = details['movie_id']
        recommend_movies.append(movies_title.iloc[0])
        recommend_poster.append(fetch_poster(poster_id.iloc[0]))
    return (recommend_movies,recommend_poster)