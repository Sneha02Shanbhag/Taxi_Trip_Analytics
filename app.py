import streamlit as st
import pandas as pd
from pymongo import MongoClient

# ------------------------ PAGE CONFIG ------------------------
st.set_page_config(
    page_title="NYC Taxi Dashboard",
    page_icon="🚕",
    layout="wide"
)

# Force clean light mode UI
st.markdown("""
    <style>
        html { color-scheme: light !important; }
        body { background-color: #ffffff; }
        .metric-card {
            background: #ffffff;
            padding: 18px 20px;
            border-radius: 12px;
            border: 1px solid #e7e7e7;
            text-align: center;
            box-shadow: 0px 2px 5px rgba(0,0,0,0.05);
        }
        h1, h2, h3, h4, h5 { color: #222 !important; }
    </style>
""", unsafe_allow_html=True)

# ------------------------ TITLE ------------------------
st.markdown("""
<div style="text-align:center; margin-bottom: 10px;">
    <h1 style='color:#ffae00;'>🚕 NYC Taxi Trip Analytics Dashboard</h1>
    <p style='color:#555; font-size:17px;'>Explore real taxi trip patterns using MongoDB-powered analytics</p>
</div>
""", unsafe_allow_html=True)

# ------------------------ DB CONNECTION ------------------------
@st.cache_resource
def get_collection():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["taxis"]
    return db["taxi_data"]

collection = get_collection()

# ------------------------ SIDEBAR ------------------------
st.sidebar.title("📊 Dashboard Controls")
view = st.sidebar.selectbox(
    "Select Analysis:",
    [
        "Peak pickup hours",
        "Average trip distance by passenger count",
        "Payment type distribution",
        "Top 10 days with highest trips",
        "Total fare collected by payment type",
        "Average trip distance by hour",
        "Trip distribution by passenger count"
    ]
)

# ------------------------ KPI CARDS ------------------------
# Query counts only once to keep UI fast
total_trips = collection.estimated_document_count()
avg_fare = collection.aggregate([{ "$group": {"_id": None, "value": { "$avg": "$total_amount"}}}])
avg_dist = collection.aggregate([{ "$group": {"_id": None, "value": { "$avg": "$trip_distance"}}}])

avg_fare = list(avg_fare)[0]["value"]
avg_dist = list(avg_dist)[0]["value"]

col1, col2, col3 = st.columns(3)

col1.markdown(f"<div class='metric-card'><h4>Total Trips</h4><h2>{total_trips:,}</h2></div>", unsafe_allow_html=True)
col2.markdown(f"<div class='metric-card'><h4>Avg Fare</h4><h2>${avg_fare:.2f}</h2></div>", unsafe_allow_html=True)
col3.markdown(f"<div class='metric-card'><h4>Avg Distance</h4><h2>{avg_dist:.2f} miles</h2></div>", unsafe_allow_html=True)

st.markdown("---")

# ------------------------ VISUALIZATION HELPER ------------------------
def show(df, index_label):
    st.bar_chart(df.set_index(index_label))
    st.dataframe(df, use_container_width=True)

# ------------------------ QUERY HANDLER ------------------------
if view == "Peak pickup hours":
    q = collection.aggregate([
        {"$project": {"hour": {"$hour": "$tpep_pickup_datetime"}}},
        {"$group": {"_id": "$hour", "Trips": {"$count": {}}}},
        {"$sort": {"_id": 1}}
    ])
    df = pd.DataFrame(q).rename(columns={"_id": "Hour"})
    st.subheader("⏱ Trips by Hour of Day")
    show(df, "Hour")

elif view == "Average trip distance by passenger count":
    q = collection.aggregate([
        {"$group": {"_id": "$passenger_count", "Avg Distance": {"$avg": "$trip_distance"}}},
        {"$sort": {"_id": 1}}
    ])
    df = pd.DataFrame(q).dropna()
    df["_id"] = df["_id"].astype(int)
    df = df.rename(columns={"_id": "Passengers"})
    st.subheader("👥 Avg Distance by Passenger Count")
    show(df, "Passengers")

elif view == "Payment type distribution":
    q = collection.aggregate([
        {"$group": {"_id": "$payment_type", "Trips": {"$count": {}}}},
        {"$sort": {"_id": 1}}
    ])
    df = pd.DataFrame(q).rename(columns={"_id": "Payment Method"})
    st.subheader("💳 Payment Type Usage")
    show(df, "Payment Method")

elif view == "Top 10 days with highest trips":
    q = collection.aggregate([
        {"$project": {"Day": {"$dayOfMonth": "$tpep_pickup_datetime"}}},
        {"$group": {"_id": "$Day", "Trips": {"$count": {}}}},
        {"$sort": {"Trips": -1}},
        {"$limit": 10}
    ])
    df = pd.DataFrame(q).rename(columns={"_id": "Day"})
    st.subheader("📅 Busiest Days of Month")
    show(df, "Day")

elif view == "Total fare collected by payment type":
    q = collection.aggregate([
        {"$group": {"_id": "$payment_type", "Total Fare": {"$sum": "$total_amount"}}},
        {"$sort": {"_id": 1}}
    ])
    df = pd.DataFrame(q).rename(columns={"_id": "Payment Method"})
    st.subheader("💰 Revenue by Payment Method")
    show(df, "Payment Method")

elif view == "Average trip distance by hour":
    q = collection.aggregate([
        {"$project": {"hour": {"$hour": "$tpep_dropoff_datetime"}, "trip_distance": 1}},
        {"$group": {"_id": "$hour", "Avg Distance": {"$avg": "$trip_distance"}}},
        {"$sort": {"_id": 1}}
    ])
    df = pd.DataFrame(q).rename(columns={"_id": "Hour"})
    st.subheader("🌇 Avg Distance by Hour of Day")
    show(df, "Hour")

elif view == "Trip distribution by passenger count":
    q = collection.aggregate([
        {"$group": {"_id": "$passenger_count", "Trips": {"$count": {}}}},
        {"$sort": {"_id": 1}}
    ])
    df = pd.DataFrame(q).dropna()
    df["_id"] = df["_id"].astype(int)
    df.rename(columns={"_id": "Passengers"}, inplace=True)
    st.subheader("👨‍👩‍👧‍👦 Trip Counts by Passenger Number")
    show(df, "Passengers")

st.markdown("---")
st.caption("Designed with 💛 for clean data storytelling.")
