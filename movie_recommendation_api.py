import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import requests

# Load movie data and similarity matrix
movies = pickle.load(open('artificats/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artificats/similarity.pkl', 'rb'))

# Initialize FastAPI app
app = FastAPI()

# Fetch movie poster from TMDb API
def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=2bfb46befba62805a9129e55cb2de2da'
    data = requests.get(url).json()
    poster_path = data.get('poster_path', '')
    if poster_path:
        return f"http://image.tmdb.org/t/p/w500{poster_path}"
    return None

# Recommendation function
def recommend(movie):
    if movie not in movies['title'].values:
        return [], []

    index = movies[movies['title'] == movie].index[0]
    distances = sorted(enumerate(similarity[index]), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    recommended_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

# Request model for input validation
class MovieRequest(BaseModel):
    movie: str

# Define API endpoint
@app.post("/recommend")
async def get_recommendations(request: MovieRequest):
    recommended_movies, recommended_posters = recommend(request.movie)
    if recommended_movies:
        return {"movies": recommended_movies, "posters": recommended_posters}
    return {"error": "Movie not found"}

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Movie Recommendation API"}
