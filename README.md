# 📈 Market Forecasting in India  
End-to-end financial volatility forecasting system built with Python, GARCH modelling, SQL databases, ETL pipelines, and FastAPI deployment.

---

## 📌 Project Overview
This project focuses on forecasting market volatility for Indian financial assets using a complete, production-oriented workflow.  
It includes automated data extraction from APIs, cleaning and transformation pipelines, SQL storage, statistical volatility modelling, and deployment through a fully functional FastAPI application.

The goal is to build a reliable, modular, and scalable system that can train volatility models and return forecasts through REST API endpoints.

---

## 🧩 Project Structure
```
Market-Forecasting-in-India/
│
├── main.py
│
├── data/
│   ├── __init__.py
│   └── data.py
│
├── models/
│   └── model.py
│
├── notebooks/
│   ├── EDA.ipynb
│   ├── garch.ipynb
│   └── testing_api.ipynb
│
├── utils/
│   └── config.py
│
├── requirements.txt
└── .gitignore
```

---

## 🛠️ Key Features

### 📡 1. API Integration
- Automated extraction of stock data from **AlphaVantage API**  
- Custom request handling with error checking  
- Conversion of raw JSON responses into structured DataFrames  
- Exception handling for failed API calls or invalid tickers  

---

### 🗄️ 2. Database Management (SQL)
- Fully implemented SQL storage using **SQLite**  
- Complete ETL workflow:
  - **Extract:** Fetch market data from APIs  
  - **Transform:** Clean, validate, and structure financial time series  
  - **Load:** Store data inside SQL tables  
- SQLRepository module for read/write operations  

---

### 📊 3. Volatility Modelling (GARCH)
- Full GARCH modelling pipeline for volatility estimation  
- Automated model training  
- Post-processing of predictions into JSON-friendly format:

```python
{
  "YYYY-MM-DD": volatility_value,
  ...
}
```

- Ensured model consistency and time-series integrity  

---

### ⚙️ 4. System Design & Architecture
- Clear module separation:
  - **data/** → Data extraction & cleaning  
  - **models/** → GARCH modelling & forecasting  
  - **utils/** → Configurations & shared helpers  
  - **main.py** → FastAPI application  
- Modular codebase built for scalability  
- Clean architecture and maintainable design patterns  

---

### 🧹 5. Data Preprocessing & EDA
- Handling missing values  
- Outlier treatment  
- Feature engineering  
- EDA using Jupyter Notebooks  
- Visualization of volatility patterns, returns, and time-series trends  

---

### 🚀 6. API Deployment with FastAPI
FastAPI application exposing two key endpoints:

#### ✅ Train Model  
**POST /fit**  
Triggers ETL, loads data, trains the GARCH model, and stores generated artifacts.

#### ✅ Predict Volatility  
**POST /predict**  
Returns volatility forecasts as JSON output.

- Real-time model serving  
- Input validation  
- Clean, structured responses  

---

## 📦 Installation

```bash
git clone https://github.com/Mo7amedMok5tar/Market-Forecasting-in-India.git
cd Market-Forecasting-in-India
pip install -r requirements.txt
```

---

## ▶️ Running the API

```bash
uvicorn main:app --reload
```

---

## 📡 Example Output

```json
{
  "2024-03-01": 0.0084,
  "2024-03-02": 0.0079,
  "2024-03-03": 0.0068
}
```

---

## 👨‍💻 Author
**Mohamed Mokhtar**  
Machine Learning Engineer | Data Scientist  
GitHub: https://github.com/Mo7amedMok5tar

---

## ⭐ Support
If you find this project useful, feel free to star the repository!
