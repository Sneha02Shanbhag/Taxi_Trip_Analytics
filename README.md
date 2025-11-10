# 🚕 NYC Taxi Trip Data Analytics Dashboard

This project analyzes real New York City Yellow Taxi trip data and visualizes key insights using **MongoDB** and a **Streamlit dashboard**.  
The dataset contains millions of trip records, making it ideal for demonstrating large-scale data processing, database storage, and interactive data analytics.

---

## 📌 Features

| Feature | Description |
|--------|-------------|
| **Data Ingestion** | Loads taxi trip data from Parquet format using Pandas |
| **Database Storage** | Stores ~3.7M+ records in MongoDB for scalable querying |
| **Interactive Dashboard** | Streamlit-based UI for viewing analytics dynamically |
| **Visual Insights** | Bar charts showing trends by time, payment type, passengers, etc. |

---

## 🗂 Dataset

NYC Yellow Taxi Trip Records (May 2024)  
Source: TLC Trip Record Data  
Format: `.parquet`

## 🗂 Dataset Information

This project uses the **NYC Yellow Taxi Trip Record Data (May 2024)** published by the New York City Taxi & Limousine Commission (TLC).

### Dataset Size
- **Total Rows:** ~3,723,833 trips
- **Total Columns:** 19 features
- **Storage Format:** Parquet (`.parquet`)
- **Database Storage:** Inserted into MongoDB collection (`taxis.taxi_data`)

### Features (Columns)

| Column | Description |
|--------|-------------|
| **VendorID** | ID of the taxi vendor company |
| **tpep_pickup_datetime** | Pickup timestamp of the trip |
| **tpep_dropoff_datetime** | Dropoff timestamp of the trip |
| **passenger_count** | Number of passengers on board |
| **trip_distance** | Distance traveled in miles |
| **RatecodeID** | Rate code used to calculate fare |
| **store_and_fwd_flag** | Whether trip record was stored & forwarded |
| **PULocationID** | Pickup zone ID (NYC zone lookup) |
| **DOLocationID** | Dropoff zone ID (NYC zone lookup) |
| **payment_type** | Payment method (1=Credit Card, 2=Cash, etc.) |
| **fare_amount** | Base fare amount charged |
| **extra** | Extra charges (late-night, etc.) |
| **mta_tax** | NYC MTA standard tax |
| **tip_amount** | Tip paid by passenger |
| **tolls_amount** | Toll charges added during trip |
| **improvement_surcharge** | Standard surcharge applied |
| **total_amount** | Final trip amount billed |
| **congestion_surcharge** | Congestion zone fee (if applicable) |
| **Airport_fee** | Additional airport pickup/drop fee |

### Data Characteristics
- **Time-series dataset** containing city mobility patterns
- Contains **both numerical + categorical data**
- Suitable for **trend analysis, demand patterns, fare prediction, and transportation analytics**
---

## 🛠️ Tech Stack

| Component | Technology Used |
|----------|----------------|
| Programming Language | Python 3 |
| Data Handling | Pandas, PyArrow |
| Database | MongoDB |
| Database Driver | PyMongo |
| Visualization Dashboard | Streamlit |
| Charts | Streamlit native charts / Matplotlib |

---

## ⚙️ Project Workflow

1. Load parquet dataset using Pandas  
2. Perform initial data exploration and cleaning  
3. Insert trip data into MongoDB collection  
4. Build Streamlit dashboard to query MongoDB and generate visual insights  

---

## 🔧 Installation & Setup

### 1. Clone the repository
```bash
git clone <your-repo-link>
cd <project-folder>
```

## Requirements
create a file requirements.txt with following contents:
- pandas==2.2.1
- pyarrow==15.0.0
- pymongo==4.6.1
- streamlit==1.31.1
- matplotlib==3.8.2
- fastparquet==2024.2.0
  
```bash
pip install -r requirements.txt
```
---

## Run the dashboard
```bash
streamlit run app.py
```
- Dashboard will open in your browser:
- http://localhost:8501
