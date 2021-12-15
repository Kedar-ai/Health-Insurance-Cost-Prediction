import streamlit as st
import joblib
import math
from PIL import Image

st.set_page_config(page_title='Medical Insurance',page_icon='🇰🇧')

def predict_insurance_cost(age,sex,bmi,children,smoker,region):
    prediction=model.predict([[age,sex,bmi,children,smoker,region]])
    print(math.ceil(prediction[0]))
    return math.ceil(prediction[0])

st.sidebar.subheader('')
st.slider.image:st.sidebar.image('https://th.bing.com/th/id/R.fd3c94794b16db3334f59f584cf738a1?rik=JEH6n2QE0eyZJw&riu=http%3a%2f%2f2.bp.blogspot.com%2f-qz-_t55J9xw%2fUZPwlV-5GDI%2fAAAAAAAAB-s%2fZ-2hswaCp8I%2fs1600%2fHealth%2bInsurance.jpg&ehk=ycJufRgN47XeXIFxSapTdQGYO9ruKXf61lGlil3gh2o%3d&risl=&pid=ImgRaw&r=0',use_column_width=True)
menu = ['Application', 'About Health Insurance']
choice = st.sidebar.selectbox("", menu)

if choice == "Application":
    html_temp = """
        <div style="background-color:green;padding:20px">
        <h1 style="color:white";text-align:center> Health Insurance Cost Prediction </h1>
        </div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    </style>"""
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.subheader('Predict the cost for your Health Insurance')
    model = joblib.load('Win_RFR_Health_Insurance_1')
    age = st.slider("Enter Your Age",18,100)
    s1 = st.radio("Sex",("Male","Female"))
    if s1 == "Male":
        sex = 1
    else:
        sex = 0
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    bmi = st.number_input("Enter your BMI value")
    children = st.selectbox(label="Enter Number of Children",options=[0,1,2,3,4,5])
    sm = st.radio("Smoker", ("Yes", "No"))
    if sm == 'Yes':
        smoker = 1
    else:
        smoker = 0
    re = st.selectbox("Region", ("southeast","southwest","northeast","northwest"))
    if re == "southeast":
        region = 0
    elif re == "southwest":
        region = 1
    elif re == "northeast":
        region = 2
    else:
        region = 3
    result=""
    if st.button("Predict"):
        result=predict_insurance_cost(age,sex,bmi,children,smoker,region)
        st.subheader('Predicted Amount:')
        st.balloons()
        st.success('Expected Insurance cost is {}'.format(result))
if choice == "About Health Insurance":
    hide_streamlit_style = """<style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>"""
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.header('For more information please click on the link below')
    st.write('https://en.wikipedia.org/wiki/Health_insurance')
    st.write('https://www.investopedia.com/terms/h/healthinsurance.asp')


