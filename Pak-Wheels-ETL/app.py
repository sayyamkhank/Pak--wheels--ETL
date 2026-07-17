import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="Car Sales Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------
# LOAD DATA
# ---------------------------
@st.cache_data
def load_data():
    return pd.read_csv("./output/clean.csv")

df = load_data()

# ---------------------------
# HEADER
# ---------------------------
st.title("🚗 Car Sales Analysis Dashboard")
st.markdown("### Explore key insights from your cleaned dataset")
st.divider()

# ---------------------------
# SIDEBAR MENU
# ---------------------------
st.sidebar.header("🔍 Select Analysis")
menu = st.sidebar.radio(
    "",
    ["Brand-wise Avg Price", "Mileage vs Price", "Fuel Type Distribution",
     "Engine Size vs Price", "Year-wise Count"]
)

# ---------------------------
# CHART RENDER FUNCTION
# ---------------------------
def show_chart(fig):
    st.pyplot(fig)
    st.divider()

# ---------------------------
# ANALYSIS 1 — Brand-wise Average Price
# ---------------------------
if menu == "Brand-wise Avg Price":

    st.header("📊 Brand-wise Average Car Price")

    result = df.groupby("brand")["prices"].mean().sort_values()

    col1, col2 = st.columns([1,1])

    # Left = Table
    with col1:
        st.subheader("Table")
        st.dataframe(result, use_container_width=True)

    # Right = Chart
    with col2:
        st.subheader("Bar Chart")
        fig, ax = plt.subplots(figsize=(10, 6))
        result.plot(kind="bar", ax=ax)
        ax.set_ylabel("Average Price (PKR)")
        ax.set_title("Brand-wise Average Prices")
        show_chart(fig)

# ---------------------------
# ANALYSIS 2 — Mileage vs Price
# ---------------------------
elif menu == "Mileage vs Price":

    st.header("📈 Mileage vs Price")

    col1, col2 = st.columns([1,1])

    with col1:
        st.subheader("Sample Data")
        st.dataframe(df[["mileage", "prices"]].head(20), use_container_width=True)

    with col2:
        st.subheader("Scatter Plot")
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.scatter(df["mileage"], df["prices"], alpha=0.5)
        ax.set_xlabel("Mileage (km)")
        ax.set_ylabel("Price (PKR)")
        ax.set_title("Mileage Impact on Price")
        show_chart(fig)

# ---------------------------
# ANALYSIS 3 — Fuel Type Distribution
# ---------------------------
elif menu == "Fuel Type Distribution":

    st.header("⛽ Fuel Type Distribution")

    fuel_counts = df["fuel_type"].value_counts()

    col1, col2 = st.columns([1,1])

    with col1:
        st.subheader("Table")
        st.dataframe(fuel_counts, use_container_width=True)

    with col2:
        st.subheader("Pie Chart")
        fig, ax = plt.subplots(figsize=(7, 7))
        fuel_counts.plot(kind="pie", autopct="%1.1f%%", ax=ax, startangle=90)
        ax.set_ylabel("")
        ax.set_title("Fuel Type Share")
        show_chart(fig)

# ---------------------------
# ANALYSIS 4 — Engine Size vs Price
# ---------------------------
elif menu == "Engine Size vs Price":

    st.header("⚙️ Engine Size vs Price")

    col1, col2 = st.columns([1,1])

    with col1:
        st.subheader("Sample Data")
        st.dataframe(df[["engine", "prices"]].head(20), use_container_width=True)

    with col2:
        st.subheader("Scatter Plot")
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.scatter(df["engine"], df["prices"], alpha=0.6)
        ax.set_xlabel("Engine cc")
        ax.set_ylabel("Price (PKR)")
        ax.set_title("Engine Size Impact on Car Price")
        show_chart(fig)

# ---------------------------
# ANALYSIS 5 — Year-wise Count
# ---------------------------
elif menu == "Year-wise Count":

    st.header("📅 Year-wise Listing Count")

    year_counts = df["year"].value_counts().sort_index()

    col1, col2 = st.columns([1,1])

    with col1:
        st.subheader("Table")
        st.dataframe(year_counts, use_container_width=True)

    with col2:
        st.subheader("Bar Chart")
        fig, ax = plt.subplots(figsize=(10, 6))
        year_counts.plot(kind="bar", ax=ax)
        ax.set_xlabel("Year")
        ax.set_ylabel("Count")
        ax.set_title("Cars Listed Per Year")
        show_chart(fig)
