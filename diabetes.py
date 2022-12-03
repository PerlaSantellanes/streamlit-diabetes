import numpy as np
import pickle
import streamlit as st

st.session_state['answer'] = ''

st.write(st.session_state)

realans = ['', 'abc', 'edf']

if  st.session_state['answer'] in realans:
    answerStat = "correct"
elif st.session_state['answer'] not in realans:
    answerStat = "incorrect"

st.write(st.session_state)
st.write(answerStat)

# Load the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# Create a function for Prediction
def diabetes_prediction(input_data):

    # Change the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'La persona no es diabetica'
    else:
      return 'La persona es diabetica'
  
def main():
    
    # Give a title
    st.title('Aplicación Web de predicción de diabetes')
    
    # To get the input data from the user
    Pregnancies = st.text_input('Número de Embarazos')
    Glucose = st.text_input('Nivel de Glucosa')
    BloodPressure = st.text_input('Valor de presión arterial (mmHg)')
    SkinThickness = st.text_input('Valor del grosor cutaneo del triceps (mm)')
    Insulin = st.text_input('Nivel de insulina (mu U/ml)')
    BMI = st.text_input('Valor de IMC')
    DiabetesPedigreeFunction = st.text_input('Valor de función de pedigrí de diabetes (probabilidad de diabetes segun antecedentes familiares)')
    Age = st.text_input('Edad de la persona')
    
    # Code for Prediction
    diagnosis = ''
    
    # Create a button for Prediction
    
    if st.button('Resultado de prueba de diabetes'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()
