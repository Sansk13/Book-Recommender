import pickle 
import streamlit as st
import numpy as np
import pandas as pd
st.header("Books Recommender System")
model=pickle.load(open('recommender/model.pkl','rb'))
books=pickle.load(open('recommender/book_name.pkl','rb'))
pivot=pickle.load(open('recommender/book_pivot.pkl','rb'))
rating=pickle.load(open('recommender/final_rating.pkl','rb'))

def fetch_poster(suggestion):
   book_name=[]
   ids_index=[]
   poster_url=[]

   for book_id in suggestion:
      book_name.append(pivot.index[book_id])
   for name in book_name[0]:
      ids=np.where(rating['title']==name)[0][0]
      ids_index.append(ids)
   for idx in ids_index:
      url= rating.iloc[idx]['img_url']
      poster_url.append(url)
   return poster_url
      
      
   
def recommend_book(book_name):
  book_list=[]
  book_id=np.where(pivot.index==book_name)[0][0]
  distance,suggestion=model.kneighbors(pivot.iloc[book_id,:].values.reshape(1,-1),n_neighbors=11)
  
  poster_url= fetch_poster(suggestion)
  for i in range(len(suggestion)):
    bookss=pivot.index[suggestion[i]]
  for j in bookss:
    book_list.append(j)
  return book_list,poster_url


selected_book=st.selectbox("Type or select a book from the dropdown",books)

if st.button('Show Recommendation'):
    recommended_books,poster_url= recommend_book(selected_book)
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10  = st.columns(10)
    with col1:
        st.text(recommended_books[1])
        st.image(poster_url[1])
    with col2:
        st.text(recommended_books[2])
        st.image(poster_url[2])

    with col3:
        st.text(recommended_books[3])
        st.image(poster_url[3])
    with col4:
        st.text(recommended_books[4])
        st.image(poster_url[4])
    with col5:
        st.text(recommended_books[5])
        st.image(poster_url[5])
    with col6:
        st.text(recommended_books[6])
        st.image(poster_url[6])
    with col7:
        st.text(recommended_books[7])
        st.image(poster_url[7])
    with col8:
        st.text(recommended_books[8])
        st.image(poster_url[8])
    with col9:
        st.text(recommended_books[9])
        st.image(poster_url[9])
    with col10:
        st.text(recommended_books[10])
        st.image(poster_url[10])