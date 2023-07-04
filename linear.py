import joblib
import streamlit as st

# Load the saved model
model_path = r"C:\Users\Aashir\Desktop\app\linear_regression_model.joblib"
model = joblib.load(model_path)

def predict_price(area):
    # Make predictions
    predicted_price = model.predict([[area]])
    return predicted_price[0]

def main():
    st.title('Home Price Prediction')
    st.write('Enter the area (in square feet) to get the predicted price')

    # Get user input
    area = st.number_input('Area')

    # Make predictions
    if st.button('Predict'):
        predicted_price = predict_price(area)

        # Display the predicted price
        st.write(f'Predicted Price: $ {predicted_price}')

if __name__ == '__main__':
    main()
