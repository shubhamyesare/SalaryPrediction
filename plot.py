import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import streamlit as st

def clean_education(x):
        if 'Bachelor’s degree' in x:
            return 'Bachelor’s degree'
        if 'Master’s degree' in x:
            return 'Master’s degree'
        if 'Professional degree' in x or 'Other doctoral' in x:
            return 'Post grad'
        return 'Less than a Bachelors'

def clean_emp(x):
        if 'Employed full-time' in x:
            return 'full-time'
        if 'Independent contractor, freelancer, or self-employed' in x:
            return 'self-employed'
        if 'Employed part-time' in x :
            return 'part-time'
        return 'other'

def clean_exp(x):
        if x=='More than 50 years':
            return 50
        if x=='Less than 1 year':
            return 0.5
        return float(x)

def shorten_categories(categories, range1):
        categorical_map = {}
        for i in range(len(categories)):
            if categories.values[i] >= range1:
                categorical_map[categories.index[i]] = categories.index[i]
            else:
                categorical_map[categories.index[i]] = 'Other'
        return categorical_map
@st.cache
def load_data ():
    df=pd.read_csv('survey_results_public.csv')
    df=df[['Country','Age','EdLevel','YearsCodePro','Employment','ConvertedComp']]
    df=df.rename({'ConvertedComp':'Salary','YearsCodePro':'ProfessionalExp'},axis=1)
    df = df[df["Salary"].notnull()]
    df['Age']=df['Age'].astype('float')
    df['Age'].fillna(df['Age'].mean(),inplace=True)
    df = df[df["Age"]>=21]
    df = df[df['Age']<=70]
    df['EdLevel']=df['EdLevel'].fillna(df['EdLevel'].mode()[0])

    

    df['EdLevel'] = df['EdLevel'].apply(clean_education)
    df['Employment']=df['Employment'].fillna(df['Employment'].mode()[0])

    
    df['Employment'] = df['Employment'].apply(clean_emp)

    
    df['ProfessionalExp']=df['ProfessionalExp'].apply(clean_exp)

    df['ProfessionalExp']=df['ProfessionalExp'].astype('float')
    df['ProfessionalExp'].fillna(df['ProfessionalExp'].mean(),inplace=True)

    
    country_map = shorten_categories(df.Country.value_counts(), 400)
    df['Country'] = df['Country'].map(country_map)

    df = df[df["Salary"] <= 220000]
    df = df[df["Salary"] >= 10000]

    a=df[(df['Country']=='United Kingdom') & (df['Salary']>130000)].index
    df.drop(a,inplace=True)
    b=df[(df['Country']=='Spain') & (df['Salary']>80000)].index
    df.drop(b,inplace=True)
    c=df[(df['Country']=='Netherlands') & (df['Salary']>110000)].index
    df.drop(c,inplace=True)
    d=df[(df['Country']=='Germany') & (df['Salary']>115000)].index
    df.drop(d,inplace=True)
    e=df[(df['Country']=='Canada') & (df['Salary']>130000)].index
    df.drop(e,inplace=True)
    f=df[(df['Country']=='Other') & (df['Salary']>100000)].index
    df.drop(f,inplace=True)
    g=df[(df['Country']=='Italy') & (df['Salary']>55000)].index
    df.drop(g,inplace=True)
    h=df[(df['Country']=='Brazil') & (df['Salary']>40000)].index
    df.drop(h,inplace=True)
    i=df[(df['Country']=='France') & (df['Salary']>80000)].index
    df.drop(i,inplace=True)
    j=df[(df['Country']=='Sweden') & (df['Salary']>80000)].index
    df.drop(j,inplace=True)
    k=df[(df['Country']=='India') & (df['Salary']>40000)].index
    df.drop(k,inplace=True)
    l=df[(df['Country']=='Poland') & (df['Salary']>70000)].index
    df.drop(l,inplace=True)
    m=df[(df['Country']=='Australia') & (df['Salary']>130000)].index
    df.drop(m,inplace=True)
    n=df[(df['Country']=='Russian Federation') & (df['Salary']>50000)].index
    df.drop(n,inplace=True)
    return df

df = load_data()

def show_plot_page():
    html_temp='''
    <div style='background-color:tomato';><p style='font=size:40px'>Software Developer Salary Prediction</p></div>
    '''
    st.markdown(html_temp,unsafe_allow_html=True)


    st.write(
        """
    ### Stack Overflow Developer Survey 2020
    """
    )
    if st.checkbox("Pie Plot"):
	    all_columns = df.columns.to_list()
	    column_to_plot = st.selectbox("Select 1 Column",all_columns,key='a')
	    pie_plot = df[column_to_plot].value_counts().plot.pie(autopct="%1.1f%%")
	    st.write(pie_plot)
	    st.pyplot()

    if st.checkbox("Bar Plot"):
	    all_columns = df.columns.to_list()
	    column_to_plot = st.selectbox("Select 1 Column",all_columns,key='b')
	    bar_plot = df[column_to_plot].value_counts().plot.bar()
	    st.write(bar_plot)
	    st.pyplot()

    if st.checkbox("Line Plot"):
	    all_columns = df.columns.to_list()
	    column_to_plot = st.selectbox("Select 1 Column",all_columns,key='c')
	    line_plot = df[column_to_plot].value_counts().plot.line()
	    st.write(line_plot)
	    st.pyplot()

    if st.checkbox("Histogram Plot"):
	    all_columns = df.columns.to_list()
	    column_to_plot = st.selectbox("Select 1 Column",all_columns,key='d')
	    hist_plot = sns.distplot(df[column_to_plot].value_counts())
	    st.write(hist_plot)
	    st.pyplot()

    if st.checkbox("Box Plot"):
	    
	    box_plot = sns.boxplot(data=df,x='Salary',y='Country')
	    st.write(box_plot)
	    st.pyplot()
    
    if st.checkbox("Scatter Plot"):
	    
	    scatter_plot = sns.scatterplot(data=df,x='ProfessionalExp',y='Salary')
	    st.write(scatter_plot)
	    st.pyplot()
    
    
    