import pandas as pd
import numpy as np
from scipy import stats

url="netflix.csv"
df = pd.read_csv(url)

# Step 2: Handle missing values by filling them with column means
df.fillna(df.mean(numeric_only=True), inplace=True)

df.drop_duplicates(inplace=True)

q1 = df["release_year"].quantile(0.25)
q3 = df["release_year"].quantile(0.75)
iqr = q3-q1
lb = q1 - 1.5 * iqr
ub = q3 + 1.5 * iqr
df=df[(df["release_year"] >= lb) & (df["release_year"] <= ub)]

print(df.head())
df.to_csv("cleaned_dataset.csv", index=False)

print("Dataset cleaned and saved as 'cleaned_dataset.csv'.")
