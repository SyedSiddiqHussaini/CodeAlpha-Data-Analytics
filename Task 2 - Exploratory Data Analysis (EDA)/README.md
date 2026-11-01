# Task 2: Exploratory Data Analysis (EDA)

## Overview
This project was completed as part of my Data Analytics Internship at CodeAlpha.
The objective was to explore the World Bank Indicators dataset and investigate patterns in global economic and social indicators using Python.
The analysis focuses on GDP per capita, life expectancy, remittances, inflation, unemployment, and other key indicators.

## Dataset
**Dataset:** `worldbank_indicators.csv`
The dataset contains World Bank indicators covering different economic and social measurements.

## Technologies & Libraries
* Python
* Pandas – Data loading, inspection, grouping and correlation analysis.
* Matplotlib – Data visualisation.
* Seaborn – Statistical visualisation and correlation heatmaps.

## Project Workflow
### 1. Data Loading and Inspection
* Loaded the CSV dataset using Pandas.
* Examined dataset dimensions using `shape`.
* Inspected column data types and dataset information using `info()`.
### 2. Missing Value Analysis
* Identified missing values across dataset columns.
* Displayed the top 10 columns with the highest number of missing values.
### 3. Exploratory Data Visualisation
The project includes four visualisations:

**A. GDP per Capita Distribution**
Used a histogram with a KDE curve to examine the distribution of GDP per capita and identify potential anomalies.
**B. GDP vs Life Expectancy**
Created a scatter plot to explore the relationship between GDP per capita and life expectancy.
**C. Global Remittances Trend**
Used a line chart to analyse changes in total global remittances received over time.
**D. Correlation Heatmap**
Created a correlation heatmap to examine relationships between selected economic and social indicators.

## Generated Visualisations
The script generates the following output files:
* `gdp_distribution.png`
* `gdp_vs_life_expectancy.png`
* `remittances_trend.png`
* `correlation_heatmap.png`

## How to Run
### 1. Install Dependencies
```bash
pip install pandas matplotlib seaborn
```
### 2. Run the Python Script
```bash
python eda_remittiances.py
```
Make sure `worldbank_indicators.csv` is available in the same directory as the Python script.

### 3. View Results
The generated graphs will be displayed and saved as PNG files.

## Key Learnings
Through this project, I gained practical experience in:
* Loading and inspecting datasets using Pandas.
* Understanding dataset structure and data types.
* Identifying missing values.
* Performing exploratory data analysis.
* Grouping data and analysing trends.
* Creating statistical visualisations.
* Understanding correlation between different indicators.

## Internship Details
**Organisation:** CodeAlpha
**Domain:** Data Analytics
**Task:** Exploratory Data Analysis (EDA)
