import streamlit as st
import pandas as pd
import pickle
import joblib
import sklearn
import sys

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="wide"
)

model = joblib.load("model/pipeline.pkl")

# ---------------- LOAD MODEL ---------------- #


st.write("Python:", sys.version)
st.write("Scikit-learn:", sklearn.__version__)
st.write("Joblib:", joblib.__version__)

model = joblib.load("model/pipeline.pkl")
# ---------------- LOAD DATA ---------------- #
df = pd.read_csv("data/clean_car.csv")

# ---------------- TITLE ---------------- #
st.title("🚗 AI Car Price Prediction")
st.markdown("Predict the price of a used car using Machine Learning.")

st.divider()

# ---------------- SIDEBAR ---------------- #
st.sidebar.header("Enter Car Details")

company = st.sidebar.selectbox(
    "Company",
    sorted(df["company"].unique())
)

car_name = st.sidebar.selectbox(
    "Car Name",
    sorted(df[df["company"] == company]["name"].unique())
)

year = st.sidebar.selectbox(
    "Year",
    sorted(df["year"].unique(), reverse=True)
)

fuel = st.sidebar.selectbox(
    "Fuel Type",
    sorted(df["fuel_type"].unique())
)

kms = st.sidebar.number_input(
    "Kilometers Driven",
    min_value=0,
    value=30000,
    step=1000
)

predict = st.sidebar.button("🚀 Predict Price")

# ---------------- MAIN AREA ---------------- #

col1, col2 = st.columns(2)

with col1:

    st.subheader("Selected Car")

    st.write("**Company:**", company)
    st.write("**Car:**", car_name)
    st.write("**Year:**", year)
    st.write("**Fuel:**", fuel)
    st.write("**KM Driven:**", kms)

with col2:

    st.subheader("Prediction")

    if predict:

        input_df = pd.DataFrame(
            [[car_name, company, year, kms, fuel]],
            columns=[
                "name",
                "company",
                "year",
                "kms_driven",
                "fuel_type"
            ]
        )

        prediction = model.predict(input_df)[0]

        st.success("Prediction Completed ✅")

        price = int(prediction)

        # Lakh aur Crore conversion
        if price >= 10000000:   # 1 Crore = 1,00,00,000
            display_price = f"₹ {price:,} ({price/10000000:.2f} Crore)"
        else:
            display_price = f"₹ {price:,} ({price/100000:.2f} Lakh)"

        st.metric(
            label="Estimated Price",
            value=display_price
        )

        st.divider()

        st.success(f"💰 Estimated Value: {display_price}")

        st.info(f"📊 Approximate Market Price: {display_price}")

# ---------------- DATASET ---------------- #

st.subheader("Dataset Preview")

st.dataframe(df.head())

# ---------------- STATS ---------------- #

st.subheader("Dataset Statistics")

c1, c2, c3 = st.columns(3)

c1.metric("Cars", len(df))
c2.metric("Companies", df["company"].nunique())
c3.metric("Fuel Types", df["fuel_type"].nunique())

# ---------------- FOOTER ---------------- #

st.markdown("---")
st.caption("Made with ❤️ using Streamlit + Scikit-Learn")
