import streamlit as st
import pandas as pd

from src.model import load_model

st.set_page_config(
    page_title="Real Estate Price Predictor",
    page_icon="🏠"
)


# Page title
st.title("Real Estate Price Prediction")

st.write(
    "Enter the property details below to estimate the property price."
)


# Load trained model
try:
    model = load_model(
        "models/real_estate_model.pkl"
    )

except Exception as error:
    st.error(
        "Error loading model: "
        + str(error)
    )
    st.stop()


# User inputs in two columns
col1, col2 = st.columns(2)

with col1:
    year_sold = st.number_input(
        "Year Sold",
        min_value=1900,
        max_value=2100,
        value=2025
    )

    property_tax = st.number_input(
        "Property Tax",
        min_value=0.0,
        value=200.0
    )

    insurance = st.number_input(
        "Insurance",
        min_value=0.0,
        value=1000.0
    )

    beds = st.number_input(
        "Number of Bedrooms",
        min_value=1,
        max_value=10,
        value=2
    )

    baths = st.number_input(
        "Number of Bathrooms",
        min_value=1,
        max_value=10,
        value=1
    )

    sqft = st.number_input(
        "Square Feet",
        min_value=100,
        value=1500
    )


with col2:
    year_built = st.number_input(
        "Year Built",
        min_value=1800,
        max_value=2100,
        value=2000
    )

    lot_size = st.number_input(
    "Lot Size",
    min_value=0,
    value=6000,
    step=100
     )

    basement = st.selectbox(
        "Basement",
        ["No", "Yes"]
    )

    popular = st.selectbox(
        "Popular Area",
        ["No", "Yes"]
    )

    recession = st.selectbox(
        "Recession Period",
        ["No", "Yes"]
    )

    property_type = st.selectbox(
        "Property Type",
        ["House", "Condo"]
    )
    
# Convert text choices into numbers
basement_value = 1 if basement == "Yes" else 0
popular_value = 1 if popular == "Yes" else 0
recession_value = 1 if recession == "Yes" else 0
condo_value = 1 if property_type == "Condo" else 0


# Calculate property age
property_age = year_sold - year_built


if st.button("Predict Price"):
    if year_built > year_sold:
        st.error("Year Built cannot be greater than Year Sold.")

    else:
        try:
            # Create one row with the same columns used during model training
            input_data = pd.DataFrame({
                "year_sold": [year_sold],
                "property_tax": [property_tax],
                "insurance": [insurance],
                "beds": [beds],
                "baths": [baths],
                "sqft": [sqft],
                "year_built": [year_built],
                "lot_size": [lot_size],
                "basement": [basement_value],
                "popular": [popular_value],
                "recession": [recession_value],
                "property_age": [property_age],
                "property_type_Condo": [condo_value]
            })

            # Predict price
            prediction = model.predict(input_data)

            st.success(
                f"Estimated Property Price: ${prediction[0]:,.2f}"
            )

        except Exception as error:
            st.error(f"Prediction error: {error}")