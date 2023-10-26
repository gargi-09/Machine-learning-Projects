# UI for Home loan approval project using streamlit
import streamlit as st
import pandas as pd
import numpy as np

import joblib
model = joblib.load(open("classifier_model.pkl", "rb"))
def predict_func(doc):
    results = model.predict([doc])
    return results
def main():
    st.title("Dream Housing Finance")