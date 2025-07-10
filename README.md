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

# Dataset Description

The dataset contains various fields providing information about store sales, customer numbers, store status, and promotional activities. Most fields are self-explanatory, but here's a detailed description for those that might need more clarification:

Id: A unique identifier for a (Store, Date) pair within the test set.

Store: A unique ID assigned to each store.

Sales: The total turnover for any given day. This is the target variable you are predicting.

Customers: The total number of customers on a given day.

Open: An indicator showing whether the store was open on a particular day. 0 means closed, and 1 means open.

StateHoliday: Indicates a state holiday. Typically, most stores are closed on these days.

a: Public holiday

b: Easter holiday

c: Christmas

0: None (not a state holiday)

SchoolHoliday: Indicates if the (Store, Date) combination was affected by public school closures.

StoreType: Differentiates between four distinct store models: a, b, c, and d.

Assortment: Describes the assortment level of the store.

a: Basic

b: Extra

c: Extended

CompetitionDistance: The distance in meters to the nearest competitor store.

CompetitionOpenSince[Month/Year]: Provides the approximate year and month when the nearest competitor store opened.

Promo: Indicates whether a store was running a promotion on that specific day.

Promo2: Represents a continuing and consecutive promotion for some stores.

0: The store is not participating in Promo2.

1: The store is participating in Promo2.

Promo2Since[Year/Week]: Describes the year and calendar week when the store began participating in Promo2.

PromoInterval: Describes the consecutive intervals when Promo2 starts, naming the months the promotion is renewed. For example, "Feb,May,Aug,Nov" means each round of Promo2 starts in February, May, August, and November of any given year for that particular store.
