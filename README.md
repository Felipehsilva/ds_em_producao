# 📊 Rossmann Store Sales Forecasting

## 📌 Project Overview

This project focuses on solving a **retail sales forecasting problem** using historical data from Rossmann, one of the largest drugstore chains in Europe. The goal is to predict **daily sales for individual stores** over a future time horizon, supporting better operational and strategic decisions.

In addition to the predictive model, this project includes the development of a **Telegram Bot** that allows users to request sales forecasts by simply providing a **store number**, making the solution accessible and practical for real-world usage.

---

## 🎯 Business Problem

Retail managers need accurate sales forecasts to anticipate demand variations caused by:

- Seasonality and time-based patterns  
- Promotional campaigns  
- Holidays (state and school)  
- Store characteristics and assortment  
- Competitive environment  

Without reliable predictions, retailers may face stockouts, overstocking, inefficient staffing, and revenue loss.

**Objective:**  
Forecast daily sales for each store for the next **6 weeks (42 days)** and deliver these predictions through an automated and user-friendly interface.

---

## 📂 Dataset

The dataset is provided by Kaggle as part of the **Rossmann Store Sales** competition.

It contains historical daily sales data along with store-level and external features, including:

- `Store` – Unique store identifier  
- `Date` – Sales date  
- `Sales` – Daily sales (target variable)  
- `Customers` – Number of customers  
- `Open` – Store open/closed indicator  
- `Promo`, `Promo2` – Promotion indicators  
- `StateHoliday`, `SchoolHoliday` – Holiday information  
- `StoreType`, `Assortment` – Store characteristics  
- `CompetitionDistance` – Distance to nearest competitor  

---

## 🧠 Approach & Methodology

This project follows a structured **end-to-end Data Science pipeline**:

1. **Exploratory Data Analysis (EDA)**  
   - Sales trends and seasonality  
   - Impact of promotions and holidays  
   - Store-level behavior analysis  

2. **Data Preprocessing**  
   - Handling missing values  
   - Encoding categorical variables  
   - Time-based feature extraction  

3. **Feature Engineering**  
   - Day, week, month, and year features  
   - Promotion duration and frequency  
   - Competition-related features  

4. **Modeling**  
   - Regression and machine learning models  
   - Focus on predictive performance and generalization  

5. **Evaluation**  
   - Metrics such as RMSE and MAE  
   - Model comparison and validation  

---

## 🏗️ Solution Architecture

The solution is designed following a **modular and scalable architecture**, simulating a real production environment.

### Architecture Components:

1. **Data Layer**
   - Historical sales and store metadata from Kaggle
   - Preprocessed and transformed into model-ready features

2. **Machine Learning Model**
   - Trained regression-based model for sales forecasting
   - Responsible for predicting daily sales for each store
   - Serialized and versioned for reproducibility

3. **Prediction Service (API Layer)**
   - A lightweight service responsible for:
     - Loading the trained model
     - Receiving store number requests
     - Running inference and aggregating forecasts
   - Acts as an interface between the model and external consumers

4. **Telegram Bot (User Interface)**
   - Allows users to request predictions via Telegram commands
   - Receives a **store number** as input
   - Sends the forecasted sales for the next **6 weeks**
   - Designed for simplicity and fast interaction

### High-Level Flow:

User (Telegram)
↓
Telegram Bot
↓
Prediction Service (API)
↓
Machine Learning Model
↓
Sales Forecast (6 weeks)
↓
Telegram Bot Response


This architecture demonstrates how a machine learning solution can be **operationalized and consumed through a messaging platform**, bridging the gap between data science and business applications.

---

## 🤖 Telegram Bot for Sales Forecasting

To make the solution more practical and closer to a real production environment, a **Telegram Bot** is implemented.

### Bot Features:
- Users can request sales forecasts by providing a **store number**
- The bot returns the predicted sales for the next **6 weeks**
- Simple and intuitive interface for non-technical users
- Model inference integrated with the trained machine learning pipeline

### Example Interaction:
User: /predict 25
Bot: Sales forecast for Store 25 (next 6 weeks):
Week 1: €XX,XXX
Week 2: €XX,XXX
...

---

## 📈 Results & Insights

The final model is able to capture:

- Strong seasonal patterns in sales  
- The impact of promotions on revenue  
- Differences in performance across store types  

The Telegram Bot enables fast access to these insights, making forecasts actionable and easy to consume.

---

## 🛠️ Tools & Technologies

- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  
- Jupyter Notebook  
- Telegram Bot API  

---

## 🚀 Business Impact

This solution allows retailers to:

- Quickly access sales forecasts per store  
- Optimize inventory and logistics planning  
- Improve workforce allocation  
- Support strategic and operational decisions  

The project highlights the application of **Machine Learning, Time Series Forecasting, and Model Deployment** in a real retail scenario.

---

## 📌 Future Improvements

- Use advanced time series models (Prophet, LSTM)  
- Improve promotion-related feature engineering  
- Deploy the prediction service as a REST API  
- Add authentication, logging, and monitoring  
- Automate retraining pipelines (MLOps)  

---

## 👤 Author

**Felipe Henrique**  
Data Science | Machine Learning | Predictive Analytics  

Feel free to explore more projects on my GitHub profile.

