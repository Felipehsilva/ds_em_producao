# Ds_em_Producao
ds_em_producao
This repository contains a Data Science project focused on store sales prediction, with a workflow that simulates a production environment. The main objective is to demonstrate the steps and considerations involved in building and deploying a Machine Learning model.

## About the Project
The ds_em_producao project addresses the challenge of predicting future store sales using historical data and store characteristics. It is structured into modules (represented by the notebooks mXX_vYY_store_sales_prediction.ipynb) that cover different phases of a data science project lifecycle, from initial exploration to preparation for production.

## Features
Exploratory Data Analysis (EDA): Deep understanding of sales, store, and holiday datasets.

Feature Engineering: Creation of new variables from raw data to improve model performance.

Data Preprocessing: Handling missing values, encoding categorical variables, and feature scaling.

Model Building and Training: Development of Machine Learning models for sales prediction.

Model Evaluation: Metrics to assess model performance.

Production Workflow Simulation: Modular structure that can be adapted for production environments.

## Repository Structure
data/: Contains raw and processed datasets (e.g., train.csv, test.csv, store.csv).

img/: Stores images and plots generated during the analysis.

model/: Intended for storing trained models or model artifacts.

mXX_vYY_store_sales_prediction.ipynb: Jupyter notebooks representing different modules or versions of the sales prediction project.


# Files

train.csv - historical data including Sales
test.csv - historical data excluding Sales
sample_submission.csv - a sample submission file in the correct format
store.csv - supplemental information about the stores

# Data fields

Most of the fields are self-explanatory. The following are descriptions for those that aren't.

Id ------------------  				an Id that represents a (Store, Date) duple within the test set
Store -------------------			a unique Id for each store
Sales -------------------			the turnover for any given day (this is what you are predicting)
Customers -------------------		the number of customers on a given day
Open -------------------			an indicator for whether the store was open: 0 = closed, 1 = open
StateHoliday -------------------	indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. Note that all schools are closed on public holidays and weekends. a = public 										holiday, b = Easter holiday, c = Christmas, 0 = None

SchoolHoliday -------------------	indicates if the (Store, Date) was affected by the closure of public schools
StoreType -------------------		differentiates between 4 different store models: a, b, c, d
Assortment -------------------		describes an assortment level: a = basic, b = extra, c = extended
CompetitionDistance --------------	distance in meters to the nearest competitor store
CompetitionOpenSince[Month/Year] -  gives the approximate year and month of the time the nearest competitor was opened
Promo -------------------			indicates whether a store is running a promo on that day
Promo2 -------------------			Promo2 is a continuing and consecutive promotion for some stores: 0 = store is not participating, 1 = store is participating
Promo2Since[Year/Week] ------		describes the year and calendar week when the store started participating in Promo2
PromoInterval -------------------	describes the consecutive intervals Promo2 is started, naming the months the promotion is started anew. E.g. "Feb,May,Aug,Nov" means each round starts in February, May, August, 									November of any given year for that store
