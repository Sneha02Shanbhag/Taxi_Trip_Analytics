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

Each record includes:
- Pickup & Dropoff timestamps  
- Trip distance  
- Passenger count  
- Pickup & drop location IDs  
- Payment method  
- Fare, tax, tip, and total amount  

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

- pip install -r requirements.txt

## Run the dashboard
- streamlit run app.py

- Dashboard will open in your browser:
- http://localhost:8501
