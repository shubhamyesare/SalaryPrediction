import streamlit as st
def show_dashboard_page():
    html_temp='''
    <div style='background-color:tomato';><p style='font=size:35px'>Software Developer Salary Prediction</p></div>
    <div class="col-div-8">
		<div class="box-8">
		<div class="content-box ">
		<p>Machine Learning Models Used and  Accuracy</p>
		<br>
		<table border='1'>
    <tbody>
    <tr>
    <th style='background-color:green';>GradientBoosting</th>
    <th style='background-color:green';>GB</th>
    <th style='background-color:green';>65 %</th>
    </tr>
    <tr>
    <th>DecisionTree</th>
    <th>DT</th>
    <th>65 %</th>
    </tr>
    <tr>
    <th>XGBoost</th>
    <th>XGB</th>
    <th>64 %</th>
    </tr>
    <tr>
    <th>K-Nearest Neighbors</th>
    <th>KNN</th>
    <th><span class="cat">58 %</span></th>
    </tr>
    <tr>
    <th>RandomForest Regressor</th>
    <th>RF</th>
    <th>58 %</th>
    </tr>
    <tr>
    <th>AdaBoost</th>
    <th>ADA</th>
    <th>56 %</th>
    </tr>
    <tr>
    <th>Linear Regression</th>
    <th>LR</th>
    <th>34 %</th>
    </tr>
    
    
    
    
    
    '''
    st.markdown(html_temp,unsafe_allow_html=True)
