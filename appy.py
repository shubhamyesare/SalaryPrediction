import streamlit as st
from predict import show_predict_page
from explore import show_explore_page
from plot import show_plot_page
from dashboard import show_dashboard_page

st.sidebar.title('Salary Prediction')

st.set_option('deprecation.showPyplotGlobalUse', False)
page = st.sidebar.selectbox("Explore Or Predict", ("Accuracy Table","Predict", "Explore","Plot"))


if page == "Accuracy Table":
    show_dashboard_page()
elif page == "Predict":
    show_predict_page()
elif page=="Explore":
    show_explore_page()
elif page=='Plot':
    show_plot_page()


    