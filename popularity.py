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
movies_list = pickle.load(open('popularity.pkl','rb'))

# convert th data into dataframe
movies = pd.DataFrame(movies_list)

# Sort the DataFrame by popularity score in descending order
new_movies = movies.sort_values(by='Popularity_Score', ascending=False)

# Movies name
top_4_movies = new_movies['title'][0:4]
top_8_movies = new_movies['title'][4:12]
top_12_movies = new_movies['title'][12:24]
top_16_movies = new_movies['title'][24:40]
top_20_movies = new_movies['title'][40:60]

#select-Box
top_list = ['select-options','Top 4 movies','Top 8 movies','Top 12 movies','Top 16 movies','Top 20 movies']
pop = top_list

# recommendation function for popular movies
def popular(pop):
    # empty list
    recommend_movies = []
    recommend_poster = []

    if pop == 'Top 4 movies':
        for i in top_4_movies:
            details = movies[movies['title'] == i]
            movie_title = details['title']
            poster_id = details['movie_id']
            recommend_movies.append(movie_title.iloc[0])
            recommend_poster.append(fetch_poster(poster_id.iloc[0]))
        return (recommend_movies,recommend_poster)

    elif pop =='Top 8 movies':   
        for i in top_8_movies:
            details = movies[movies['title'] == i]
            movie_title = details['title']
            poster_id = details['movie_id']
            recommend_movies.append(movie_title.iloc[0])
            recommend_poster.append(fetch_poster(poster_id.iloc[0]))
        return (recommend_movies,recommend_poster)
    
    elif pop =='Top 12 movies':   
        for i in top_12_movies:
            details = movies[movies['title'] == i]
            movie_title = details['title']
            poster_id = details['movie_id']
            recommend_movies.append(movie_title.iloc[0])
            recommend_poster.append(fetch_poster(poster_id.iloc[0]))
        return (recommend_movies,recommend_poster)

    elif pop =='Top 16 movies':   
        for i in top_16_movies:
            details = movies[movies['title'] == i]
            movie_title = details['title']
            poster_id = details['movie_id']
            recommend_movies.append(movie_title.iloc[0])
            recommend_poster.append(fetch_poster(poster_id.iloc[0]))
        return (recommend_movies,recommend_poster)
    
    elif pop =='Top 20 movies':   
        for i in top_20_movies:
            details = movies[movies['title'] == i]
            movie_title = details['title']
            poster_id = details['movie_id']
            recommend_movies.append(movie_title.iloc[0])
            recommend_poster.append(fetch_poster(poster_id.iloc[0]))
        return (recommend_movies,recommend_poster)