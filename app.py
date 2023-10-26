import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8c7cb75bb820ba2bb2da4ffe68da46b0&language=en-US".format(movie_id)
    data = requests.get(url)
    data=data.json()
    poster_path=data['poster_path']
    full_path="https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    b=(similarity[index])
    distances= sorted(list(enumerate(b)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in distances[1:6]:
        movies_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movies_id))
    return recommended_movies,recommended_movies_posters

st.header('Movie Recommender System')
movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')
selected_movie_name= st.selectbox(
    'How would you Like to be contacted?',
    movies['title'].values)

if st.button('Recommend'):
    recommended_movies,recommended_movies_posters = recommend(selected_movie_name)

    col1,col2,col3,col4,col5 = st.beta_columns(5)
    with col1:
        st.header(recommended_movies[0])
        st.image(recommended_movies_posters[0])
    with col2:
        st.header(recommended_movies[1])
        st.image(recommended_movies_posters[1])
    with col3:
        st.header(recommended_movies[2])
        st.image(recommended_movies_posters[2])
    with col4:
        st.header(recommended_movies[3])
        st.image(recommended_movies_posters[3])
    with col5:
        st.header(recommended_movies[4])
        st.image(recommended_movies_posters[4])





