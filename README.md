# 📊 Rossmann Store Sales Forecasting
👉 **Full project explanation available on my blog:**  
🔗 [Click here](https://dataineverywhere.my-board.org/projects/sales-forecasting-for-rossmann-stores-using-machine-learning/)

## 📌 Project Overview

This project addresses a real-world **retail sales forecasting problem** using historical data from Rossmann, one of the largest drugstore chains in Europe.

The main objective is to predict **daily sales for each store** over a future horizon of **6 weeks (42 days)**, supporting better decision-making in inventory planning, promotions, logistics, and workforce allocation.

Beyond model development, this project also includes the deployment of the trained model through a **Prediction API** and a **Telegram Bot**, allowing users to request forecasts by simply providing a store number.

---

## 🎯 Business Problem

Retail managers need accurate sales forecasts to anticipate demand fluctuations caused by:

- Seasonality and calendar effects  
- Promotional campaigns  
- Holidays (state and school)  
- Store characteristics and assortment  
- Competitive environment  

Without reliable forecasts, retailers may experience overstocking, stockouts, inefficient staffing, and revenue loss.

**Business Goal:**  
Forecast daily sales per store for the next **42 days**, making predictions easily accessible through an automated interface.

---

## 📂 Dataset

The dataset is provided by Kaggle as part of the **Rossmann Store Sales** competition.

### Data Fields Description

Most of the dataset fields are self-explanatory. Below are the key variables used in this project:

- **Id** – Unique *(Store, Date)* identifier (test set)
- **Store** – Unique store identifier  
- **Sales** – Daily sales (target variable)  
- **Customers** – Number of customers per day  
- **Open** – Store open indicator (`0` = closed, `1` = open)  
- **StateHoliday** – State holiday indicator (`a`, `b`, `c`, `0`)  
- **SchoolHoliday** – Indicates school holiday impact  
- **StoreType** – Store model (`a`, `b`, `c`, `d`)  
- **Assortment** – Assortment level (`a` = basic, `b` = extra, `c` = extended)  
- **CompetitionDistance** – Distance to nearest competitor (meters)  
- **CompetitionOpenSinceMonth / Year** – Competitor opening date  
- **Promo** – Promotion indicator  
- **Promo2** – Consecutive promotion participation  
- **Promo2SinceYear / Week** – Promo2 start date  
- **PromoInterval** – Months when Promo2 starts  

These variables provide rich **temporal, promotional, and store-level information**, allowing the model to capture complex sales patterns.

---

## 🧠 Approach & Methodology

The project follows a complete **end-to-end Data Science pipeline**, implemented and validated in the notebook:

### 1️⃣ Exploratory Data Analysis (EDA)
- Analysis of sales distribution and trends  
- Identification of seasonality patterns  
- Impact of promotions and holidays on sales  
- Store-level behavioral differences  

### 2️⃣ Data Preprocessing
- Handling missing values  
- Renaming and standardizing features  
- Encoding categorical variables  
- Date transformation and time-based features  

### 3️⃣ Feature Engineering
- Day, week, month, and year features  
- Promotion duration and cyclic behavior  
- Competition-related temporal features  
- Business-driven feature creation  

### 4️⃣ Modeling & Validation
- Baseline models (Linear Regression and Regularized models)
- Cross-validation strategy for fair model comparison
- Selection of non-linear models due to complex relationships in the data

---

## 🤖 Machine Learning Model

The final model selected for this project is the **XGBRegressor**, based on its superior performance during cross-validation.

### Why XGBRegressor?

XGBoost was chosen because it:

- Captures complex non-linear relationships  
- Handles large-scale tabular data efficiently  
- Models interactions between promotions, seasonality, and store attributes  
- Delivers strong predictive performance with controlled overfitting  

### Model Details

- **Algorithm:** XGBoost Regressor  
- **Task:** Regression (Sales Forecasting)  
- **Target Variable:** `Sales`  
- **Validation Strategy:** Cross-validation  
- **Evaluation Metrics:** RMSE,MAPE, MAE  

The trained model is serialized and used for inference in the prediction service.

---

## 🏗️ Solution Architecture

The solution is designed following a **modular and scalable architecture**, simulating a real production environment.
User (Telegram)
↓
Telegram Bot
↓
Prediction API
↓
XGBoost Model
↓
Sales Forecast (6 weeks)
↓
Telegram Response


### Architecture Components

- **Data Layer:** Kaggle dataset and processed features  
- **Model Layer:** Trained XGBRegressor  
- **API Layer:** Service responsible for loading the model and running inference  
- **Interface Layer:** Telegram Bot for user interaction  

---

## 🤖 Telegram Bot for Sales Forecasting

The Telegram Bot allows non-technical users to request sales forecasts.

### Bot Features
- Input: Store number  
- Output: Sales forecast for the next **6 weeks**  
- Simple command-based interaction  
- Integrated with the trained ML model  

### Example
/25
---

## 🛠️ Tools & Technologies

- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  
- XGBoost  
- Jupyter Notebook  
- FastAPI / Flask (API)  
- Telegram Bot API  

---
## 🤖 Telegram Bot for Sales Forecasting

To make the sales forecasting solution easily accessible and closer to a real business environment, this project includes the development of a **Telegram Bot** integrated with the trained machine learning model.

The bot allows users to request sales forecasts by simply providing a **store number**, without the need for technical knowledge or direct interaction with the model or codebase.

---

### 🎯 Bot Purpose

The Telegram Bot serves as a lightweight user interface that bridges the gap between the **machine learning model** and **business users**, enabling fast and intuitive access to predictions.

It demonstrates how a data science solution can be operationalized and delivered through a commonly used messaging platform.

---

### ⚙️ How It Works

1. The user sends a command to the Telegram Bot with a store identifier  
2. The bot forwards the request to the prediction service  
3. The trained **XGBRegressor** model performs inference  
4. The forecasted sales for the next **6 weeks (42 days)** are returned  
5. The bot sends the prediction back to the user in a readable format  

---

### 🧩 Bot Features

- Input: **Store number**
- Output: **Daily or aggregated sales forecast for the next 6 weeks**
- Simple command-based interaction
- Integrated with the machine learning prediction pipeline
- Designed for non-technical users

---

### 💬 Example Interaction

User: /25
Bot: Sales forecast for Store 25 (next 6 weeks):
Week 1: €XX,XXX
Week 2: €XX,XXX

## 🚀 Business Impact

This solution enables retailers to:

- Improve inventory and logistics planning  
- Optimize promotional strategies  
- Allocate workforce more efficiently  
- Access forecasts quickly through an automated system  

The project demonstrates how **Machine Learning can be operationalized**, moving from experimentation to real-world usage.

---

## 📌 Future Improvements

- Incorporate advanced time series models (Prophet, LSTM)  
- Add model monitoring and retraining pipelines (MLOps)  
- Improve feature importance explainability  
- Deploy using Docker and cloud services  

---

## 👤 Author

**Felipe Henrique**  
Data Science | Machine Learning | Predictive Analytics

