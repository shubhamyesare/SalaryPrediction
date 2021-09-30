import streamlit as st
import pickle
import numpy as np
st.set_option('deprecation.showPyplotGlobalUse', False)

def load_model():
    with open('project.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

gb = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]
le_emp=data['le_emp']


def show_predict_page():
    html_temp='''
    <div style='background-color:tomato';><p style='font=size:35px'>Software Developer Salary Prediction</p></div>
    '''
    st.markdown(html_temp,unsafe_allow_html=True)

    st.write("""### We need some information to predict the salary""")

    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )

    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

    employe = (
        'full-time',
        'self-employed',
        'part-time',
    )

    country = st.selectbox("Country", countries)
    age = st.slider("Age", 18, 70, 21)

    education = st.selectbox("Education Level", education)

    expericence = st.slider("Years of Experience", 0, 50, 0)

    employe = st.selectbox('Employment',employe)

    ok = st.button("Calculate Salary")
    if ok:
        X = np.array([[country,age,education, expericence,employe ]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 2] = le_education.transform(X[:,2])
        X[:, 4] = le_emp.transform(X[:,4])
        X = X.astype(float)

        salary = gb.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")
