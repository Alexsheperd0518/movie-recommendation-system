import pickle
import pandas as pd
import requests

# fetch poster function
def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=338016ac774f28f30916824466db50bf".format(movie_id))
    data = response.json()
    poster_path = data['poster_path']
    return "https://image.tmdb.org/t/p/w500" + poster_path

# recommendation function
def recommend(movies_name):
    movie_index = movies[movies['title'] == movies_name].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:13]

    recommend_movies = []
    recommend_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movie_id))
    return (recommend_movies, recommend_poster)

# load the data
movies_list = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# convert th data into dataframe
movies = pd.DataFrame(movies_list)

# movies name list
movies_name = movies['title'].values

# calling the recommend function
names, poster = recommend(movies_name)