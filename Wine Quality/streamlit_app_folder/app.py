import streamlit as st
import plotly.express as px
from PIL import Image
import numpy as np
import pandas as pd

import joblib

wine_clf = joblib.load(open("random_forest_wine.pkl","rb"))

def predict_quality(lst):
    predictions = wine_clf.predict([lst])
    return predictions

def get_predict_proba(lst):
    
    probability = wine_clf.predict_proba([lst])
    return probability

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


 
def build_slider(cols):
    values = []

    for col in cols:
        num = 0.0
        num = round(st.number_input(col,min_value = 0.0,max_value = 1.0,step = 0.01),2)
        num = round(st.slider(label = col,min_value=0.0,max_value=1.0,step=0.001,value = num),2)
        
        st.write(num)
        values.append(num)
    return values

def main():
    st.title("Wine Quality Rating")
    menu = ['Home','Monitor','About']

    choices = st.sidebar.selectbox("Menu",menu)
    image = Image.open('wine_pic.jpg')

    st.image(image,caption = "Wine glass")


    if choices == 'Home':
        st.subheader("Home page")
        
        columns = ['Fixed Acidity', 'Volatile Acidity', 'Citric Acid', 'Residual Sugar',
       'Chlorides', 'Free Sulfur Dioxide', 'Total Sulfur Dioxide', 'Density',
       'pH Value', 'Sulphates', 'Alcohol']
        
        values = build_slider(columns)

        if st.button('Rate'):
            local_css("style.css")
            col1,col2 = st.columns(2)
            ratings = predict_quality(values)
            proba = get_predict_proba(values)

            with col1:
                st.success("Orignal Values")
                for col,val in zip(columns,values):
                    col1.markdown(f"{col} : {val}")
            
            with col2:
                st.success("Ratings")
                st.markdown(f"Quality range : 3-8\nQuality rating : {ratings[0]}")

    elif choices == 'Monitor':
        st.subheader("Monitor page")
    
    else:
        st.subheader("About page")





if __name__ == '__main__':
    main()
