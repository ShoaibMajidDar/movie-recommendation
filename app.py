import streamlit as st
import pickle

def recommend(movie):
    movie_index = movies_list[movies_list['title']==movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)),reverse = True, key = lambda x:x[1])[1:6]
    for i in movie_list:
        st.write(movies_list.iloc[i[0]].title)
    return

movies_list = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies_title = movies_list['title'].values
st.title('Movie Recommender System')
movie_selected = st.selectbox(
    'Enter a movies name',
    movies_title)
if st.button('recommend'):
    recommend(movie_selected)