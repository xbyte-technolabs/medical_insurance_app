import streamlit as st
import pandas as pd
import time
import base64
import joblib


# Load the model
model = joblib.load("insurance.joblib")
data = pd.read_csv("insurance.csv")

#sidebar radio button
menu=st.sidebar.radio("Menu",['Home','Insurance Cost'])

# Sidebar image
st.sidebar.image("you.png", use_column_width=True)


if menu=='Home':
    
    st.title('General Overview')

    # Image
    st.image("prediction.png")

    st.write("""
    Welcome to the Medical Insurance Cost Prediction App! This application is designed to help users estimate their medical insurance costs based on various personal and demographic factors. The prediction model has been trained on a dataset of insurance charges and takes into account the following factors:
    - **Age**: The age of the individual.
    - **Sex**: The gender of the individual (male or female).
    - **BMI**: Body Mass Index, a measure of body fat based on height and weight.
    - **Children**: Number of children/dependents covered by the insurance.
    - **Smoker**: Whether the individual is a smoker (yes or no).
    - **Region**: The region where the individual lives (southwest, southeast, northwest, northeast).

    ### Dataset Information
    The dataset used for training the model contains information on medical insurance costs for various individuals along with their demographic information. Here is a brief overview of the dataset:
    """)

    st.write("Shape of a dataset",data.shape)
    st.write('### Tabular data of insurance')
    # st.header('Tabular data of insurance')
    if st.checkbox("Tabular data"):
        st.table(data.head())

    # graph = st.selectbox('Select Graph',['Bar','Histograph'])
    # if graph == 'Bar':
    #     fig, ax = plt.subplots()
    #     sns.barplot(data,x='sex',y='charges')
    #     st.pyplot(fig)

if menu=='Insurance Cost':

    # Load the model
    # with open('insurance.sav', 'rb') as model_file:
    #     model = pickle.load(model_file)


    # Title
    st.title('Medical Insurance Cost Prediction')
    # st.image('medical.png')


    # Input fields
    st.header('Enter the details:',divider='rainbow')



    age = st.number_input('Age', min_value=18, max_value=65, value=25) 
    sex = st.selectbox('Sex', ['male', 'female'])
    bmi = st.number_input('BMI', min_value=14.0, max_value=54.0, value=25.0)
    children = st.number_input('Number of children', min_value=0, max_value=5, value=0)
    smoker = st.selectbox('Smoker', ['yes', 'no'])
    region = st.selectbox('Region', ['southwest', 'southeast', 'northwest', 'northeast'])

    # Map input to model input
    sex = 1 if sex == 'male' else 0
    smoker = 1 if smoker == 'yes' else 0
    region_mapping = {'southwest': 3, 'southeast': 2, 'northwest': 1, 'northeast': 0}
    region = region_mapping[region]

    # Prediction
    if st.button('Predict'):
        input_data = pd.DataFrame([[age, sex, bmi, children, smoker, region]],
                                columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])
        

        # with st.spinner('Wait for it...'):
        #     time.sleep(2)
        # st.balloons()

        progress_text = "Prediction in progress. Please wait.."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.02)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        my_bar.empty()
        # st.balloons()


        prediction = model.predict(input_data)
        output = f'Predicted Insurance Cost : {prediction[0]:.2f}'
        st.markdown(f"<h6 style='font-size:20px;'>{output.strip()}</h1>", unsafe_allow_html=True)