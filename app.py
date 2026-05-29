import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------
# PAGE TITLE
# -----------------------

st.title("Job Market Analysis Dashboard")

# -----------------------
# LOAD DATA
# -----------------------

df = pd.read_csv("data/data_jobs.csv")

# -----------------------
# DATA CLEANING
# -----------------------

df = df.drop("Unnamed: 0", axis=1)

df["Salary Estimate"] = df["Salary Estimate"].str.replace(
    "(Glassdoor est.)",
    "",
    regex=False
)

df["Salary Estimate"] = df["Salary Estimate"].str.replace(
    "$",
    "",
    regex=False
)

df["Salary Estimate"] = df["Salary Estimate"].str.replace(
    "K",
    "",
    regex=False
)

# Split salary range
df[["min_salary", "max_salary"]] = (
    df["Salary Estimate"]
    .str.split("-", expand=True)
)

# Convert to numeric
df["min_salary"] = pd.to_numeric(
    df["min_salary"],
    errors="coerce"
)

df["max_salary"] = pd.to_numeric(
    df["max_salary"],
    errors="coerce"
)

# Average salary
df["avg_salary"] = (
    df["min_salary"] + df["max_salary"]
) / 2

# Clean company names
df["company_clean"] = (
    df["Company Name"]
    .str.split("\n")
    .str[0]
)

# -----------------------
# SIDEBAR FILTER
# -----------------------

industries = sorted(
    df["Industry"]
    .dropna()
    .unique()
)

selected_industry = st.sidebar.selectbox(
    "Select Industry",
    industries
)

# -----------------------
# FILTER DATA
# -----------------------

filtered_df = df[
    df["Industry"] == selected_industry
]

# -----------------------
# KPI METRICS
# -----------------------

avg_salary = round(
    filtered_df["avg_salary"].mean(),
    1
)

vacancies_count = filtered_df.shape[0]

companies_count = (
    filtered_df["company_clean"]
    .nunique()
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Salary",
    f"{avg_salary}K"
)

col2.metric(
    "Vacancies",
    vacancies_count
)

col3.metric(
    "Companies",
    companies_count
)

# -----------------------
# DATA PREVIEW
# -----------------------

st.subheader("Dataset Preview")

st.dataframe(filtered_df.head())

# -----------------------
# TOP COMPANIES CHART
# -----------------------

st.subheader(
    f"Top Companies in {selected_industry}"
)

top_companies = (
    filtered_df["company_clean"]
    .value_counts()
    .head(10)
)

fig, ax = plt.subplots(figsize=(10, 6))

top_companies.sort_values().plot(
    kind="barh",
    ax=ax
)

plt.tight_layout()

st.pyplot(fig)

# -----------------------
# SALARY DISTRIBUTION
# -----------------------

st.subheader("Salary Distribution")

fig, ax = plt.subplots(figsize=(10, 5))

filtered_df["avg_salary"].hist(
    bins=20,
    ax=ax
)

plt.xlabel("Salary")

plt.ylabel("Count")

plt.tight_layout()

st.pyplot(fig)

# -----------------------
# TOP PAYING COMPANIES
# -----------------------

st.subheader("Top Paying Companies")

top_salary_companies = (
    filtered_df
    .groupby("company_clean")["avg_salary"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

st.dataframe(top_salary_companies)