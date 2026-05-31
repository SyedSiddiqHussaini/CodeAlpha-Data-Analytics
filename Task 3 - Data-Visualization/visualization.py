import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create images folder
os.makedirs("images", exist_ok=True)

# Load dataset
df = pd.read_csv("data/worldbank_indicators.csv")

print("Dataset Loaded Successfully")
print("Shape:", df.shape)

# ----------------------------
# DATA CLEANING
# ----------------------------

print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# ----------------------------
# VISUALIZATION 1
# Global Remittances Trend
# ----------------------------

yearly_remit = df.groupby("year")["remittances_received_usd"].sum()

plt.figure(figsize=(10,5))
plt.plot(yearly_remit.index, yearly_remit.values)
plt.title("Global Remittances Received Over Time")
plt.xlabel("Year")
plt.ylabel("Remittances Received (USD)")
plt.grid(True)

plt.savefig("images/remittances_trend.png")
plt.show()

# ----------------------------
# VISUALIZATION 2
# Top 10 Countries
# ----------------------------

top10 = (
    df.groupby("country_name")
    ["remittances_received_usd"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))
top10.plot(kind="bar")

plt.title("Top 10 Countries by Remittances Received")
plt.xlabel("Country")
plt.ylabel("USD")

plt.tight_layout()
plt.savefig("images/top10_countries.png")
plt.show()

# ----------------------------
# VISUALIZATION 3
# Region Analysis
# ----------------------------

region_data = (
    df.groupby("region")
    ["remittances_received_usd"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12,5))
region_data.plot(kind="bar")

plt.title("Remittances by Region")
plt.xlabel("Region")
plt.ylabel("USD")

plt.tight_layout()
plt.savefig("images/remittances_by_region.png")
plt.show()

# ----------------------------
# VISUALIZATION 4
# Income Group Analysis
# ----------------------------

income_data = (
    df.groupby("income_group")
    ["remittances_received_usd"]
    .sum()
)

plt.figure(figsize=(8,5))
income_data.plot(kind="bar")

plt.title("Remittances by Income Group")
plt.xlabel("Income Group")
plt.ylabel("USD")

plt.tight_layout()
plt.savefig("images/income_group_analysis.png")
plt.show()

# ----------------------------
# VISUALIZATION 5
# GDP vs Remittances
# ----------------------------

plt.figure(figsize=(8,5))

sns.scatterplot(
    data=df,
    x="gdp_per_capita_usd",
    y="remittances_per_capita_usd"
)

plt.title("GDP Per Capita vs Remittances Per Capita")

plt.tight_layout()
plt.savefig("images/gdp_vs_remittances.png")
plt.show()

# ----------------------------
# VISUALIZATION 6
# Correlation Heatmap
# ----------------------------

numeric_cols = df.select_dtypes(
    include=["float64", "int64"]
)

plt.figure(figsize=(15,10))

sns.heatmap(
    numeric_cols.corr(),
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.savefig("images/correlation_heatmap.png")
plt.show()

# ----------------------------
# VISUALIZATION 7
# Outlier Detection
# ----------------------------

plt.figure(figsize=(8,5))

sns.boxplot(
    x=df["remittances_received_usd"]
)

plt.title("Outlier Detection - Remittances Received")

plt.tight_layout()
plt.savefig("images/outlier_detection.png")
plt.show()

print("\nAll visualizations generated successfully!")