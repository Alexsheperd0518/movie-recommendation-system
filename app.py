from flask import Flask, render_template, request
import numpy as np
from main import movies_name, recommend
from genre import genre_list, genres
from year import year_wise
from popularity import top_list, popular
from rating import predict_movies,user_list


app = Flask(__name__)

# this is code is for home page 
@app.route('/',methods = ["GET","POST"])
def index():
    final_movies_names=np.insert(movies_name,0,"select-options")
    return render_template('index.html', movies_name=final_movies_names)

@app.route('/result', methods = ["GET","POST"])
def index2():
    final_movies_names=np.insert(movies_name,0,"select-options")
    select = request.form.get("select_movie")
    if select == "select-options":
        return render_template('index.html',movies_name=final_movies_names, select=select)
    else:
        names,poster = recommend(select)
        return render_template('index.html', movies_name=final_movies_names, select=select, posters=zip(poster,names))



# This code is for genre page    
@app.route('/genre',methods = ["GET","POST"])
def movies_genre():
    genre = request.form.get("genre_name")
    names,poster = genres(genre)
    return render_template('genre.html', genre_list = genre_list, genre = genre, movies_genre_poster = zip(poster,names))



# This code is for year page    
@app.route('/year',methods = ["GET","POST"])
def movies_year():
    year = request.form.get("select_year")
    if year is None:
        return render_template('year.html')
    else:
        names,poster = year_wise(year)
        return render_template('year.html', year_wise_movies = zip(poster, names))



# This code is for popular page    
@app.route('/popular',methods = ["GET","POST"])
def popular_movies():
    pop = request.form.get("top-movie")
    return render_template('popularity.html', top_list=top_list)

@app.route('/result2',methods = ["GET","POST"])
def popular_movies2():
    pop = request.form.get("top-movie")
    if pop == "select-options":
        return render_template('popularity.html', top_list=top_list, pop=pop)
    else:
        names,poster = popular(pop)
        return render_template('popularity.html', top_list=top_list, pop=pop, top_movies=zip(poster,names))



# This code is for rating page
@app.route('/rating',methods = ["GET","POST"])
def rating():
    user_id = request.form.get('predict_movie')
    if user_id is None:
        return render_template('rating.html')
    else:
        names, poster = predict_movies(user_id)
        return render_template('rating.html', user_list=user_list, poster_and_names=zip(poster, names))

    
if __name__ == '__main__':
    app.run(debug=True, port=8000)
