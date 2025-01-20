# MOVIE RECOMMENDATION SYSTEM API

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : ROHAN KUMAR GUPTA

*INTERN ID* : CT4MKNM

*DOMAIN* : BACKEND WEB DEVELOPMENT

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTOSH

## DESCRIPTION OF TASK  IN 500 WORDS

The Movie Recommendation System API is a project designed to provide users with personalized movie recommendations based on machine learning techniques. The goal of this project is to create an efficient, scalable, and user-friendly API that can be integrated into various applications such as web and mobile platforms to enhance the user experience in discovering new movies. The recommendation system uses content-based filtering to suggest movies that are similar to the ones users prefer.

### Project Overview

The project is developed using Python, with key technologies including **FastAPI**, **Streamlit**, and **pickle** for model storage and retrieval. The movie dataset consists of a list of movie titles along with their respective similarity scores, which are preprocessed and stored for quick access. The API allows users to input a movie title, and it returns a list of recommended movies along with their respective posters fetched from the TMDb (The Movie Database) API.

### Technologies Used

1. **Python:** The core programming language used for development.
2. **FastAPI:** A modern, high-performance web framework for building APIs.
3. **Streamlit:** Initially used for UI purposes but later refactored into an API.
4. **Pickle:** For storing and loading the trained similarity matrix and movie data.
5. **Requests:** Used to interact with the TMDb API for fetching movie posters.
6. **Uvicorn:** An ASGI server used to run the FastAPI application.

### Features

1. **Movie Recommendation:**

   - Users can input a movie title and receive a list of recommended movies.
   - The recommendations are based on content similarity computed using cosine similarity.

2. **Poster Fetching:**

   - The API integrates with the TMDb API to fetch high-quality movie posters, enhancing the visual appeal of recommendations.

3. **API Integration:**

   - The API can be integrated with any frontend application, making it highly versatile.

4. **Scalability:**

   - Designed to handle multiple requests concurrently with high performance.

### Working of the System

1. The system loads a pre-trained similarity matrix and a list of movies using the `pickle` library.
2. When a user submits a movie title, the system finds its index in the dataset.
3. The cosine similarity values are used to rank other movies in the dataset.
4. The top 5 most similar movies are selected and their details, including posters, are fetched.
5. The API responds with a JSON object containing the recommended movie names and their corresponding poster URLs.

### How to Use

1. Clone the repository and install dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the API server:
   ```bash
   uvicorn movie_recommendation_api:app --host 0.0.0.0 --port 8000 --reload
   ```
3. Access the API documentation at `http://127.0.0.1:8000/docs`.
4. Send a POST request to `/recommend` with a movie title to get recommendations.

Example request using `curl`:
```bash
curl -X POST "http://127.0.0.1:8000/recommend" -H "Content-Type: application/json" -d '{"movie":"Inception"}'
```

Example response:
```json
{
  "movies": ["Interstellar", "The Dark Knight", "Tenet", "Memento", "The Prestige"],
  "posters": [
    "http://image.tmdb.org/t/p/w500/example1.jpg",
    "http://image.tmdb.org/t/p/w500/example2.jpg",
    "http://image.tmdb.org/t/p/w500/example3.jpg",
    "http://image.tmdb.org/t/p/w500/example4.jpg",
    "http://image.tmdb.org/t/p/w500/example5.jpg"
  ]
}
```

### Conclusion

This project demonstrates how machine learning and web development can be combined to create a powerful and useful application. The Movie Recommendation System API provides an easy way for users to discover movies they might enjoy, and it can be expanded with additional features such as collaborative filtering and user-based recommendations in the future.

# OUTPUT

Upon running the API and making a request with a movie title, the output consists of the top 5 recommended movies along with their posters. The output is returned in JSON format, which can be easily consumed by various front-end applications.

![Image](https://github.com/user-attachments/assets/8bb36ca4-7618-409e-9b48-2c6dc1619cd0)

![Image](https://github.com/user-attachments/assets/4b82b610-bb3f-4021-996a-0b8517aaff44)