import pickle
import pandas as pd
import requests
from surprise import Dataset, Reader, KNNBasic
from surprise.accuracy import rmse
from surprise.model_selection import cross_validate, train_test_split

# load the data
movies_list = pickle.load(open('rating.pkl','rb'))

# convert th data into dataframe
movies = pd.DataFrame(movies_list)

# Define a reader and load the data
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(movies[['userId', 'movie_id','rating']], reader)

# Split the data into training and testing sets
trainset, testset = train_test_split(data, test_size=0.2)

# Create a KNNBasic model (similarity measure configuration)
sim_options = {"name": "pearson_baseline", "shrinkage": 0} # no shrinkage
model = KNNBasic(sim_options = sim_options)

# Train the model on the training set
model.fit(trainset)

# Make predictions on the test set
predictions = model.test(testset)

# Evaluate the model using RMSE (Root Mean Squared Error)
rmse_val = rmse(predictions)

# user list
user_list = [str(temp)  for temp in range(1,46)]
user_list.insert(0,"Select-options")

# fetch poster function
def fetch_poster(poster_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=338016ac774f28f30916824466db50bf".format(poster_id))
    data = response.json()
    poster_path = data['poster_path']
    return "https://image.tmdb.org/t/p/w500"+poster_path

# recommendation function for raitng wise movies fetch
def predict_movies(id):
    print("type",type(id))
    
    
    user_id = int(id)
    user_ratings = []

    for item_id in movies['movie_id'].unique():
        user_ratings.append((item_id, model.predict(user_id, item_id).est))


    
    # top rating in decending order 
    user_ratings.sort(key=lambda x: x[1], reverse=True)

    

    # convert the predticted data into dataframe
    predict_data = pd.DataFrame(user_ratings)
    predicted_movie_id = predict_data[0][0:12]



    # append the movies data new list 
    predicted_movies_details = []
    for x in predicted_movie_id:
        predicted_movies_details.append(movies[movies['movie_id'] == x])

    # convert the predicted_movies_details into dataframe    
    movie_details = pd.concat(predicted_movies_details, ignore_index= True)

   
    # recommend the movies name
    recommend_movies = []
    for x in movie_details['title']:
        recommend_movies.append(x)

    # fetch the movies poster

    recommend_poster = []
    for y in movie_details['movie_id']:
        recommend_poster.append(fetch_poster(y))

    return [recommend_movies, recommend_poster]
