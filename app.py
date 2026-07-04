import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="wide"
)

# ---------------- LOAD MODEL & DATA ---------------- #
@st.cache_resource
def load_model():
    return joblib.load("model/pipeline (1).pkl")

@st.cache_data
def load_data():
    return pd.read_csv("data/clean_car.csv")

try:
    model = load_model()
    df = load_data()
except FileNotFoundError as e:
    st.error(f"❌ Required file not found: {e}")
    st.info("Make sure 'model/pipeline.pkl' and 'data/clean_car.csv' exist in your project.")
    st.stop()

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
kms = int(kms)

predict = st.sidebar.button("🚀 Predict Price")

with st.sidebar.expander("Debug Info"):
    import sklearn
    st.write("Scikit-learn:", sklearn.__version__)
    st.write("Joblib:", joblib.__version__)

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
        try:
            input_df = pd.DataFrame(
                [[car_name, company, year, kms, fuel]],
                columns=["name", "company", "year", "kms_driven", "fuel_type"]
            )

            prediction = model.predict(input_df)[0]
            price = int(prediction)

            # Lakh / Crore conversion
            if price >= 10000000:
                display_price = f"₹ {price:,} ({price/10000000:.2f} Crore)"
            else:
                display_price = f"₹ {price:,} ({price/100000:.2f} Lakh)"

            st.success("Prediction Completed ✅")
            st.metric(label="Estimated Price", value=display_price)

        except Exception as e:
            st.error(f"Prediction failed: {e}")
    else:
        st.info("Fill in the details and click **Predict Price** to see the result.")

# ---------------- DATASET ---------------- #
st.divider()
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
