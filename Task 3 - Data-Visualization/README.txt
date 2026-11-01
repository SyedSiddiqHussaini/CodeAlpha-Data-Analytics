# Global Remittances & Migration Data Visualization (2000–2023)

## Overview
This project was completed as part of my Data Analytics Internship at CodeAlpha.
The objective was to transform raw World Bank remittance and migration data into meaningful visualisations using Python.
The project explores global remittance trends, country-wise comparisons, regional distributions, income groups, economic relationships, correlations, and outliers through different visualisation techniques.

## Dataset
**Dataset:** Global Remittances & Migration Indicators (2000–2023)
**File:** `worldbank_indicators.csv`

The dataset includes indicators related to:
* Remittances Received
* Remittances Paid
* GDP Indicators
* Population Statistics
* Migration Indicators
* Income Group Information
* Regional Information

## Technologies & Libraries
* **Python** – Programming language
* **Pandas** – Data manipulation and analysis
* **Matplotlib** – Data visualisation
* **Seaborn** – Statistical visualisation
* **NumPy** – Numerical computing (if used in the project)

## Project Workflow
### 1. Data Loading and Cleaning
* Loaded the dataset using Pandas.
* Checked dataset dimensions.
* Identified duplicate records.
* Removed duplicate rows.
* Inspected missing values.

### 2. Data Visualisation
The project includes seven visualisations.
| No. | Visualisation            | Purpose                                                                      |
| --- | ------------------------ | ---------------------------------------------------------------------------- |
| 1   | Global Remittances Trend | Analyses remittance inflows over time.                                       |
| 2   | Top 10 Countries         | Identifies the countries with the highest total remittances received.        |
| 3   | Remittances by Region    | Compares remittance distribution across regions.                             |
| 4   | Income Group Analysis    | Examines remittances across income groups.                                   |
| 5   | GDP vs Remittances       | Explores the relationship between GDP per capita and remittances per capita. |
| 6   | Correlation Heatmap      | Examines correlations among numerical indicators.                            |
| 7   | Outlier Detection        | Uses a box plot to identify potential outliers in remittance data.           |

## Generated Visualisations
All generated graphs are saved automatically inside the `images/` directory.
| Image                       | Description                           |
| --------------------------- | ------------------------------------- |
| `remittances_trend.png`     | Global remittance trends              |
| `top10_countries.png`       | Top 10 remittance-receiving countries |
| `remittances_by_region.png` | Regional comparison                   |
| `income_group_analysis.png` | Income group comparison               |
| `gdp_vs_remittances.png`    | GDP and remittance relationship       |
| `correlation_heatmap.png`   | Correlation analysis                  |
| `outlier_detection.png`     | Remittance outlier detection          |

## How to Run
### 1. Clone the Repository
```bash
git clone https://github.com/SyedSiddiqHussaini/CodeAlpha-Data-Analytics.git
```
### 2. Navigate to the Task 3 Folder
```bash
cd "CodeAlpha-Data-Analytics/Task 3 - Data-Visualization"
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the Script
```bash
python visualization.py
```
**Note:** The script expects the dataset at `data/worldbank_indicators.csv`. Ensure the dataset is available at that location before running it.
The generated visualisations will be saved inside the `images/` folder.

## Key Learnings
Through this project, I gained practical experience in:
* Cleaning datasets by identifying and removing duplicate records.
* Inspecting missing values.
* Grouping and aggregating data using Pandas.
* Creating different types of visualisations.
* Exploring relationships between economic indicators.
* Understanding correlation and outlier detection.
* Presenting data through visual storytelling.

## Internship Details
**Organisation:** CodeAlpha
**Domain:** Data Analytics
**Task:** Data Visualization

**Created by:** Syed Siddiq Hussaini
