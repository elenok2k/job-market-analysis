# Job Market Analysis Dashboard

Interactive dashboard for analyzing the data analyst job market using Python, SQL, and Streamlit.

---

## Project Overview

This project analyzes job market data for data-related positions.

The dashboard allows users to:
- filter jobs by industry,
- explore salary distributions,
- analyze top companies,
- view key metrics.

---

## Technologies Used

- Python
- Pandas
- SQL (SQLite)
- Matplotlib
- Streamlit

---

## Features

- Data cleaning and preprocessing
- Salary analysis
- Industry filtering
- KPI metrics
- Interactive charts
- Top companies analysis

---

## Dashboard Preview

![Dashboard Screenshot](images/dashboard.png)

---

## Project Structure

```bash
job-market-analysis/
│
├── data/
│   ├── data_jobs.csv
│   └── jobs.db
│
├── notebooks/
│   ├── analysis.ipynb
│   └── sql_analysis.ipynb
│
├── src/
│   └── hh_parser.py
│
├── images/
│   └── dashboard.png
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone repository:

```bash
git clone <your-repo-link>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run dashboard:

```bash
streamlit run app.py
```

---

## Key Insights

- Healthcare and pharmaceutical industries show some of the highest salaries.
- Salary distribution is concentrated in mid-to-high salary ranges.
- Several large tech companies consistently offer top compensation.

---

## Future Improvements

- Deploy dashboard online
- Add more visualizations
- Connect real-time APIs
- Add machine learning salary prediction

---
