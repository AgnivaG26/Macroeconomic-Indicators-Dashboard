# World Economic Indicators Dashboard

[![Status: Complete](https://img.shields.io/badge/status-complete-success)](#)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425e.svg)](https://www.python.org/)
[![Framework: Streamlit](https://img.shields.io/badge/Framework-Streamlit-ff69b4.svg)](https://streamlit.io/)

## 1. Live Dashboard

This project is a dynamic and interactive dashboard that visualizes key macroeconomic indicators for countries around the world. The live application is deployed and can be accessed here:

[**🚀 View the Live Interactive Dashboard**](https://macroeconomic-indicators-dashboard-itenwyd2gubkzavbepzd52.streamlit.app/)

## 2. Project Overview

This dashboard is built with **Python** and **Streamlit** and uses data from the World Bank. It provides enhanced data analysis and visualization capabilities beyond the standard World Bank website, making economic trends easier to explore, compare, and export.

### Key Features
* **Multi-Country Comparison:** Compare the performance of multiple countries side-by-side on a single chart for any key indicator (GDP Growth, Trade, etc.).
* **Dynamic Filters:** Use interactive sliders and dropdowns to filter data by country and year range, instantly updating all charts and metrics.
* **Choropleth Maps:** Visualize a selected indicator on an interactive world map for any year, allowing for quick identification of global and regional trends.
* **Data Export:** Easily download the filtered data for a single country, a multi-country comparison, or a specific indicator for all countries with a single click.
* **Clean and Robust Data:** The backend script, `data_cleaning.py`, handles data cleaning, including fixing missing values and preparing the data for seamless use in the dashboard.

---
## 3. How to Run Locally

To run this dashboard on your own machine, follow these steps.

#### Prerequisites
* Python 3.8+
* The required libraries. Install them using pip:
    ```bash
    pip install streamlit pandas plotly
    ```
* The raw CSV data files from the World Bank. Download the six required CSVs (GDP Growth, Exports, Imports, Agriculture, Industry, Services) and save them in your project folder.

#### Steps
1.  **Run the Data Cleaner:** This script will load and prepare your raw CSV data, saving a cleaned file named `cleaned_data.pkl`. Run it once from your terminal:
    ```bash
    python data_cleaning.py
    ```

2.  **Run the Dashboard:** Once the cleaned data file is generated, you can start the Streamlit app from your terminal:
    ```bash
    streamlit run dashboard.py
    ```
This will open the interactive dashboard in your web browser.

---
## 4. Project Files

* `dashboard.py`: The main Streamlit application script.
* `data_cleaning.py`: The script for cleaning and preparing the data.
* `cleaned_data.pkl`: The cleaned, ready-to-use data file created by `data_cleaning.py`.
* `gdp_growth.csv`, `exports.csv`, etc.: The raw data files downloaded from the World Bank.