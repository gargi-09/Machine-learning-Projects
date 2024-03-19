import streamlit as st
import joblib

import pandas as pd
import numpy as np

import plotly.express as pex

pipe_lr = joblib.load(open("logistic_model.pkl","rb"))

def predict_class(doc):
    results = pipe_lr.predict(doc)
    return results

def get_predict_proba(doc):
    results = pipe_lr.predict_proba([doc])
    return results

def make_radio(cols):
    values = []
    for col,opt in cols.items():
        
        res = st.radio(col,opt,index=None)
        values.append(res)
    return values

def make_num_input(cols):
    values=[]
    for col in cols:
        res = st.number_input(label=col,min_value=0.0,step=1.,format="%.1f")
        values.append(res)
    return values

def main():
    st.title("Home Loan Approval App")
    st.write("Fill the following fields--")
    cols1 = {'Married':[0,1],'Dependents':[0,1,2,3],'Education':[0,1],'Self Employed':[0,1]}
    doc = make_radio(cols1)

    cols2 = ["Applicant Income","Coapplicant Income","Loan Amount","Loan Amount Term"]
    res = make_num_input(cols2)
    doc.extend(res)

    cols3 = {"Credit_History":[0,1]	,"Gender_Male":[0,1],"Property_Semiurban":[0,1],"Property_Urban":[0,1]}
    doc.extend(make_radio(cols3))


    if st.button('Check'):
        prediction = predict_class([doc])
        proba = get_predict_proba(doc)
        col1,col2 = st.columns(2)
        with col1:
            if prediction==1:
                st.success("Approval Status:")
                st.markdown(f"The loan application has been approved.")
            else:
                st.error("Approval status:")
                st.markdown("Unfortunately, your loan application could not be approved.")
            
        with col2:
            st.success("Probability Chart:")
            proba_df = pd.DataFrame(proba,columns=pipe_lr.classes_)
            proba_df_clean = proba_df.T.reset_index()
            proba_df_clean.rename(columns={'index':'Classes',0:'Probabilities'},inplace=True)
            fig = pex.bar(proba_df_clean,x='Classes',y='Probabilities',color='Classes',
                          hover_data='Classes',
                          title="Probability distribution")
            st.plotly_chart(fig,use_container_width=True)
            st.write(f"Confidence : {round(np.max(proba),0)}")
if __name__=='__main__':
    main()
